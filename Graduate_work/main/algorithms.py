import numpy as np


def calculate_task_table_from_productivity_factors(tasks_lists, productivity_factors):
    # p - count of task. k - vector productivity factors
    # transform two vector to matrix with task * productivity
    output_table = []
    productivity_factors.sort()
    tasks_lists.sort()
    print(productivity_factors, tasks_lists)

    for j in range(len(productivity_factors)):
        row = []
        for i in range(len(tasks_lists)):
            row.append(tasks_lists[i] * productivity_factors[j])
        output_table.append(row)
    output_table = np.array(output_table)
    output_table = output_table.T
    return output_table


def calculate_second_table(table):
    newtable = []
    for i in range(table.shape[0]):
        row = []
        for j in range(table.shape[1]):
            row.append(1 / table[i, j])
        newtable.append(row)
    newtable = np.array(newtable)
    return newtable


def A1(count_of_machine, count_of_tasks, task_table_with_coefficient):
    task_of_machine = []
    list_of_used_time_of_every_machine = list(count_of_machine * [0])
    # create dict for every machine in task
    for _ in range(0, count_of_machine):
        machine = {}
        task_of_machine.append(machine)
    # distribute tasks for every machine with magic algorithms from the Heaven
    for j in range(count_of_tasks):
        index = list_of_used_time_of_every_machine.index(min(list_of_used_time_of_every_machine))
        list_of_used_time_of_every_machine[index] += np.asscalar(task_table_with_coefficient[j][index])
        task_of_machine[index].update({j + 1: np.asscalar(task_table_with_coefficient[j][index])})
    return task_of_machine


def A2(m, n, table, RealC, f, p):
    task_of_machine = []
    for i in range(0, m):
        machine = {}
        task_of_machine.append(machine)

    for j in range(0, n):
        index = f.index(max(f))  # index with max f
        RealC[index] += table[j][index]  # fill C
        f[index] -= p[j]
        task_of_machine[index].update({j + 1: table[j][index]})
    # output_result_algorithm(task_of_machine)

    return task_of_machine


def optimization2(k, e, sigma, C):
    print('\n----------------------------------------------------------------')
    print('Second optimization')
    T = []
    for i in range(len(k)):
        T.append((C - k[i] * e[i]))
    opt = [0] * len(k)
    x = [0] * len(k)
    counter = 0
    sigma2 = round(sigma, 0)
    sigma2 = int(sigma2)
    print(int(sigma2))
    for i in range(sigma2):
        for i in range(len(k)):
            opt[i] = k[i] * (e[i] - x[i])
        index = opt.index(max(opt))
        x[index] += 1
        T[index] += k[index]
        counter += 1
    print(counter)
    print("X = ", x)
    return x


def optimization1(sigma, e, k, C):
    print('\n----------------------------------------------------------------')
    print('First optimization')
    T = []
    for i in range(len(k)):
        T.append((C - k[i] * e[i]))
    FirstT = T.copy()
    Tq = T.copy()
    for i in range(len(k)):
        Tq[i] += k[i]
    x = [0] * len(k)
    sigma2 = round(sigma, 0)
    print(int(sigma2))
    sigma2 = int(sigma2)
    print(int(sigma2))
    for i in range(sigma2):
        index = Tq.index(min(Tq))
        Tq[index] += k[index]
        x[index] += 1
    for i in range(len(k)):
        T[i] += x[i] * k[i]
    print("X = ", x)
    return x, FirstT


def run_algorithms(productivity_factors, sets, set_id, type_algorithm):
    print("productivity ", productivity_factors, "sets ", sets)
    schedules = []
    if type_algorithm == '1':
        for i in range(len(sets)):
            task_table_with_coefficient = calculate_task_table_from_productivity_factors(sets[i],
                                                                                         productivity_factors[i])
            schedules.append(
                A1(len(productivity_factors[i]), len(sets[i]), task_table_with_coefficient))

    # Get data from DB

    # Run algorithms
    # Write to algorithm table
    write_to_alorithms_table(set_id, schedules)


def write_to_alorithms_table(task_id, schedules):
    print("schedules", schedules)
    from ..models import Algorithm
    from .. import db
    import json
    for i in schedules:
        print(type(i[0]), i[0])
        sched_JSON = json.dumps(i)
        print('JSON ', sched_JSON)
        alg = Algorithm(task_id=task_id, initial_timetable=sched_JSON)
        db.session.add(alg)
        db.session.commit()
