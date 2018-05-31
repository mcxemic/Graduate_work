import numpy as np


def calculate_task_table_from_productivity_factors(tasks_lists, productivity_factors):
    # p - count of task. k - vector productivity factors
    # transform two vector to matrix with task * productivity
    output_table = []
    productivity_factors.sort()
    tasks_lists.sort()
    tasks_lists.reverse()
    # print(productivity_factors, tasks_lists)

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


def output_result_algorithm(result):
    for i in enumerate(result):
        pass
        # print('Machine ', i[0] + 1, i[1])


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
    output_result_algorithm(task_of_machine)
    return task_of_machine


def A2(count_of_machine, count_of_task, table, tasks_list, C_foreach_machine):
    task_of_machine = []
    list_of_used_time_of_every_machine = list(count_of_machine * [0])
    #print("tasks" + tasks_list)
    for _ in range(0, count_of_machine):
        machine = {}
        task_of_machine.append(machine)

    for j in range(0, count_of_task):
        index = C_foreach_machine.index(max(C_foreach_machine))  # index with max f
        list_of_used_time_of_every_machine[index] += np.asscalar(table[j][index])  # fill C
        C_foreach_machine[index] -= tasks_list[j]
        task_of_machine[index].update({j + 1: np.asscalar(table[j][index])})
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


def run_algorithms(productivity_factors, sets, task_id, C):
    from .optimization_algorithms import get_finall_T, create
    import time
    schedules_first_alg = []
    schedules_secoond_alg = []

    for i in range(len(sets)):
        task_table_with_coefficient = calculate_task_table_from_productivity_factors(sets[i],
                                                                                     productivity_factors[i])
        schedules_first_alg.append(
            A1(len(productivity_factors[i]), len(sets[i]), task_table_with_coefficient))

    for i in range(len((sets))):
        task_table_with_coefficient = calculate_task_table_from_productivity_factors(sets[i],
                                                                                     productivity_factors[i])
        C_foreach_machine = list(map(lambda i: C / i, productivity_factors[i]))
        schedules_secoond_alg.append(A2(len(productivity_factors[i]), len(sets[i]),
                                        task_table_with_coefficient, sets[i], C_foreach_machine))

    # Get data from DB

    # Run algorithms
    # Write to algorithm table
    write_to_alorithms_table(task_id, schedules_first_alg, schedules_secoond_alg)

    # create optimization
    for i in range(len(sets)):
        start1 = time.time()
        final_T_first, keys1, ideal1 = get_finall_T(schedules_first_alg[i], productivity_factors[i])
        optimizationed_schedule1,max_proj1,relative_projection1,iteration_count1 = create(keys1, ideal1, productivity_factors[i], final_T_first)
        print("Iteration count 1 {}".format(iteration_count1))
        stop1 = time.time()
        write_to_optimization_table(task_id, optimizationed_schedule1, max_proj1, stop1 - start1,relative_projection1,iteration_count1)
        start2 = time.time()
        final_T_second, keys2, ideal2 = get_finall_T(schedules_secoond_alg[i], productivity_factors[i])
        optimizationed_schedule2,max_proj2,relative_projection2,iteration_count2 = create(keys2, ideal2, productivity_factors[i], final_T_second)
        print("Iteration count 2 {}".format(iteration_count2))
        stop2 = time.time()
        write_to_optimization_table(task_id,optimizationed_schedule2,max_proj2,stop2-start2,relative_projection2,iteration_count2)

def write_to_alorithms_table(task_id, schedule1, schedule2):
    from ..models import Algorithm
    from .. import db
    import json
    for i in range(len(schedule1)):
        # print('schedule1  {0}   schedule {1}'.format(schedule1, schedule2))
        # print('1 len {0}, type {1}  schedule {2}'.format(len(schedule1), type(schedule1[0]), schedule1[i][0]), i)
        #print('2 len {0}, type {1}  schedule {2}'.format(len(schedule2), type(schedule2[0]), schedule2[i][0]))
        sched_JSON1 = json.dumps(schedule1[i])
        sched_JSON2 = json.dumps(schedule2[i])
        alg = Algorithm(task_id=task_id, initial_timetable_first_alg=sched_JSON1,
                        initial_timetable_second_alg=sched_JSON2)
        db.session.add(alg)
        db.session.commit()


def write_to_optimization_table(task_id,algorithm,projection,runtime,relative_projection,iteration_count):
    from ..models import Task
    import json
    from .. import db

    algo = json.dumps(algorithm)
    tsk = Task.query.filter_by(id=task_id).first()
    tsk.first_Optimization = algo
    tsk.first_projection = projection
    tsk.first_lead_time = runtime
    tsk.first_relatively_projection = relative_projection
    tsk.first_iteration_count = iteration_count
    db.session.commit()