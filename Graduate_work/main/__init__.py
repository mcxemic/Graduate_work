from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors


def generate_sets(type_distribution, count_set, count_devices, mean_duration_P, deviation_duration_Q, C, gen_algo):
    sets = []
    print("generate_sets", type_distribution, count_devices, count_set, mean_duration_P, deviation_duration_Q, C)
    for _ in range(count_set):
        sets.append([])
    for j in range(count_set):
        sets[j].extend(
            create_task_for_multiply_machine(type_distribution, count_devices[j], mean_duration_P, deviation_duration_Q,
                                             C, gen_algo))
    return sets


def create_task_for_multiply_machine(type_distribution, count_devices, mu, sigma, C, gen_algo):
    sets_of_machine = []
    for _ in range(count_devices):
        sets_of_machine.extend(create_task_for_one_machine(type_distribution, mu, sigma, C, gen_algo))
    sets_of_machine.sort()
    return sets_of_machine


def create_task_for_one_machine(type_distribution, mu, sigma, c, gen_algo):
    import random
    normal_distribution_set = choose_distribution(type_distribution, mu, sigma, c)
    machine = [int(i) for i in normal_distribution_set]
    if sum(machine) < c:
        if c - sum(machine) > 0:
            machine.append(c - sum(machine))
        else:
            machine.append(1)

    if random.randint(0, 1) == 1 and gen_algo == '2':
        machine.append(1)
    machine.sort()
    return machine


def create_set_distribution(method, mu, sigma, c):
    normal = []
    while c > mu + 2 * sigma:
        x = method(mu, sigma)

        if x > 0:
            normal.append(x)
        else:
            normal.append(1)
        c -= x
    if c > 0:
        normal.append(c)
    return normal


def create_normal_distribution(mu, sigma, size=1):
    from numpy.random import normal
    x = normal(mu, sigma, size)
    if x > 0:
        return int(x)
    else:
        return 1


def create_uniform_distribution(mu, sigma, size=1):
    import numpy
    new_sigma = ((12 * sigma ** 2 + 1) ** (1 / 2) - 1) / 2
    x = numpy.random.uniform(low=mu - new_sigma, high=mu + new_sigma, size=size)
    if x > 0:
        return int(x)
    else:
        return 1


def choose_distribution(type_distribution, mu, sigma, c):
    if type_distribution == '1':
        return create_set_distribution(create_normal_distribution, mu, sigma, c)
    elif type_distribution == '2':
        return create_set_distribution(create_uniform_distribution, mu, sigma, c)


