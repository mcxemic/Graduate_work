from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors


def generate_sets(type_distribution, count_set, count_devices, mean_duration_P, deviation_duration_Q, C):
    sets = []
    print("generate_sets", type_distribution, count_devices, count_set, mean_duration_P, deviation_duration_Q, C)
    for _ in range(count_set):
        sets.append([])
    for j in range(count_set):
        sets[j].extend(
            create_task_for_multiply_machine(type_distribution, count_devices[j], mean_duration_P, deviation_duration_Q,
                                             C))
    return sets


def create_set_normal_distribution(mu, sigma, c):
    normal = []
    while c > mu + 2 * sigma:
        x = create_normal_distribution(mu, sigma)
        normal.append(x)
        c -= x
    return normal


# TODO rewrite or delete
def create_normal_distribution(mu, sigma, size=1):
    from numpy.random import normal
    x = normal(mu, sigma, size)
    if x > 0:
        return int(x)
    else:
        return 1


def create_task_for_multiply_machine(type_distribution, count_devices, mu, sigma, C):
    sets_of_machine = []
    for i in range(count_devices):
        sets_of_machine.extend(create_task_for_one_machine(type_distribution, mu, sigma, C))
    sets_of_machine.sort()
    return sets_of_machine


def create_task_for_one_machine(type_distribution, mu, sigma, c):
    print("create task for one machine", type_distribution, mu, sigma, c)
    normal_distribution_set = choose_distribution(type_distribution, mu, sigma, c)
    machine = [int(i) for i in normal_distribution_set]
    if sum(machine) < c:
        machine.append(c - sum(machine))
    machine.sort()
    return machine


def normal_distribution(mean, deviation, size=1):
    import numpy as np
    print(mean, deviation, size, ' normal distr')
    mac = np.random.normal(mean, deviation, size)

    return mac


def create_uniform_distribution(mu, sigma, size):
    import numpy
    new_sigma = (12 * sigma ** 2 + 1) ** (1 / 2) - 1
    return numpy.random.uniform(low=mu - new_sigma, high=mu + new_sigma, size=size)


def choose_distribution(type_distribution, mu, sigma, c):
    print('type', type_distribution)
    if type_distribution == '1':
        return create_set_normal_distribution(mu, sigma, c)
    elif type_distribution == '2':
        return create_uniform_distribution(mu, sigma, int(c / mu))
