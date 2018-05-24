#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
1. Визначаємо тривалості зайнятості пристроїв
2. Визначаємо 3 множини -- резерву, відхиленя та оптимуму
3. Знаходимо машину з максимальним відхиленням
4. Знаходимо машину з максимальним резервом
5. Вибираємо їх для обміну
6. Будуємо матрицю для знаходження Тета за формулою Theta = pj1/k1 - pj2/k2 де Тета > 0
7. Шукаємо max(Zi/ki+Ej/kj-Theta) Де Z - максимальний виступ E - максимальний резерв
8. Якщо розклад оптимальний то закінчити, інакше повторити

1. Перша створимо лист з довжинами
2. Функція яка за допомогою листа з довжинами та ідеального розкладу повертає три листа пустих, з резервом, з відхиленням

"""


def projection(now_T,final_T):
    for i in range(len(now_T)):
        yield abs(now_T[i]-final_T[i])

def get_deviation(length_for_each_machine, ideal):
    deviation = [round(i - ideal, 3) if i > ideal else 0 for i in length_for_each_machine]
    reserve = [round(ideal - i, 3) if i < ideal else 0 for i in length_for_each_machine]
    normally = [0 if i == ideal else -1 for i in length_for_each_machine]
    return deviation, reserve, normally


def swap(best_machine, worse_machine, best_machine_coefficient, worse_machine_coefficient, best_task_to_swap,
         worse_task_to_swap):
    i = best_machine.index(best_task_to_swap)
    j = worse_machine.index(worse_task_to_swap)
    new_worse = best_machine[i] / best_machine_coefficient * worse_machine_coefficient
    new_best = worse_machine[j] / worse_machine_coefficient * best_machine_coefficient
    best_machine[i], worse_machine[j] = new_best, new_worse
    return best_machine, worse_machine


def get_deviation_for_each_machine(machine, ideal):
    return abs(sum(machine) - ideal)


def get_matrix_of_swap_coefficien(best_machine, worse_machine, best_machine_coefficient, worse_machine_coefficient):
    # print(worse_machine,best_machine,worse_machine_coefficient,best_machine_coefficient)
    matrix_of_swap_coefficient = []
    worse_machine.sort(reverse=True)
    best_machine.sort(reverse=True)

    for i in worse_machine:
        for j in best_machine:
            Theta = i / worse_machine_coefficient - j / best_machine_coefficient
            if Theta > 0:
                matrix_of_swap_coefficient.append((Theta, i, j))
    # print(matrix_of_swap_coefficient)
    return matrix_of_swap_coefficient


def get_task_from_task_coefficient(matrix_swap_coefficient, worse_machine_coefficient, best_machine_coefficient,
                                   best_machine_deviation, worse_machine_deviation):
    constant = worse_machine_deviation / worse_machine_coefficient + best_machine_deviation / best_machine_coefficient

    swap_coef = [constant - i[0] for i in matrix_swap_coefficient]
    swap_index = swap_coef.index(max(swap_coef))
    worse_task_to_swap = matrix_swap_coefficient[swap_index][1]
    best_task_to_swap = matrix_swap_coefficient[swap_index][2]
    return worse_task_to_swap, best_task_to_swap


def get_T(ideal, fraction_part, coefficient):
    for i in range(len(fraction_part)):
        # print("C* {0} e[{1}]: {2} k[{1}]: {3} k*e {4}".format(ideal,i,fraction_part[i],coefficient[i], fraction_part[i]*coefficient[i]))
        yield round(ideal - fraction_part[i] * coefficient[i], 2)


def find_min_T(T_coefficient, coefficient):
    for i in range(len(coefficient)):
        yield T_coefficient[i] + coefficient[i]


def list_t_with_coefficient(coefficient, list_t):
    for i in range(len(list_t)):
        yield list_t[i] + coefficient[i]


def create_optimization(sigma, coefficient, list_T):
    if sigma > 0:
        # print(sigma)
        main_T = list(list_t_with_coefficient(coefficient, list_T))
        # print('main T {}'.format(main_T))
        min_T_coefficient_index = main_T.index(min(main_T))
        list_T[min_T_coefficient_index] += coefficient[min_T_coefficient_index]
        # print('list T {0}'.format(list_T))
        create_optimization(sigma - 1, coefficient, list_T)

    return [round(i, 2) for i in list_T]
    # find minimum Ti+ki
    # add to machine k[i]
    # go to recursion with sigma-1 and new main_T


def get_task_from_keys(keys, coefficient):

    for i in range(len(keys)):
        for j in keys[i]:
            yield round(j / coefficient[i], 0)


def create_ideal_c(tasks, coefficient):
    sum_f = 0
    for j in tasks:
        sum_s = 0
        for i in coefficient:
            sum_s += 1 / (i * j)
        sum_f += 1 / sum_s
    return round(sum_f, 4)


def get_finall_T(list_schedules, coefficient):
    # get keys from input dict initial timetable
    # print('Get Finall t list_schedules {}  coefficient {}'.format(list_schedules,coefficient))
    keys = [list(i.values()) for i in list_schedules]
    # get task from keys for calculate ideal value
    #print('get task from keys keys {} coefficient {}'.format(keys,coefficient))
    task = list(get_task_from_keys(keys, coefficient))
    ideal = create_ideal_c(task, coefficient)
    c_for_each_machine = [round(ideal / i, 3) for i in coefficient]
    int_c_for_each_machine = [int(i) for i in c_for_each_machine]
    fraction_c_part_for_each_machine = [round(i - int(i), 3) for i in c_for_each_machine]
    sum_all_task = sum(task)
    sum_int_c_for_each_machine = sum([int(j) for j in int_c_for_each_machine])
    sigma = int(sum_all_task - sum_int_c_for_each_machine)
    list_T = list(get_T(ideal, fraction_c_part_for_each_machine, coefficient))
    final_T = create_optimization(sigma, coefficient, list_T)
    return final_T, keys, ideal



def create(keys, ideal, coefficient, final_T,iter=0):
    now_T = [round(sum(i), 2) for i in keys]
    max_projection = max(projection(now_T, final_T))
    if now_T != final_T and iter<20:
        length_for_each_machine = [sum(i) for i in keys]
        # print('sum for each machine {}'.format(length_for_each_machine))
        deviation_machine, reserve_machine, normally_machine = get_deviation(length_for_each_machine, ideal)
        # print('Deviation for each machine {}    Reserve for each machine {}     Normally for each machine {}'.format(deviation_machine, reserve_machine, normally_machine))
        worse_machine = keys[deviation_machine.index(max(deviation_machine))]
        best_machine = keys[reserve_machine.index(max(reserve_machine))]
        best_machine_coefficient = coefficient[reserve_machine.index(max(reserve_machine))]
        worse_machine_coefficient = coefficient[deviation_machine.index(max(deviation_machine))]
        matrix_swap_coefficient = get_matrix_of_swap_coefficien(best_machine, worse_machine, best_machine_coefficient,
                                                                worse_machine_coefficient)
        best_machine_deviation = get_deviation_for_each_machine(best_machine, ideal)
        worse_machine_deviation = get_deviation_for_each_machine(worse_machine, ideal)
        worse_task_to_swap, best_task_to_swap = get_task_from_task_coefficient(matrix_swap_coefficient,
                                                                               best_machine_coefficient,
                                                                               worse_machine_coefficient,
                                                                               best_machine_deviation,
                                                                               worse_machine_deviation)
        new_best_machine, new_worse_machine = swap(best_machine, worse_machine, best_machine_coefficient,
                                                   worse_machine_coefficient, best_task_to_swap, worse_task_to_swap)
        keys[deviation_machine.index(max(deviation_machine))] = new_worse_machine
        keys[reserve_machine.index(max(reserve_machine))] = new_best_machine

        create(keys, ideal, coefficient, final_T,iter+1)

    return keys, max_projection

