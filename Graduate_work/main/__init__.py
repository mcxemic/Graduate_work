from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors


def generate_sets(type_distribution, count_set, count_devices, mean_duration_P, deviation_duration_Q, C):
    sets = []
    for _ in range(count_set):
        sets.append([])
    for j in range(count_set):
        sets[j].extend(
            create_task_for_multiply_machine(type_distribution, count_devices[j], mean_duration_P, deviation_duration_Q,
                                             C))
    return sets


# TODO rewrite or delete
def create_normal_distribution(mu, sigma, size=1):
    from numpy.random import normal
    x = normal(mu, sigma, size)
    if x > 0:
        if x > mu + 2 * sigma:
            return int(mu + 2 * sigma)
        else:
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
    normal_distribution_set = choose_distribution(type_distribution, mu, sigma, int(c / mu) - 1)
    machine = [int(i) for i in normal_distribution_set]
    if sum(machine) < c:
        machine.append(c - sum(machine))
    machine.sort()
    return machine


def normal_distribution(mean, deviation, size=1):
    import numpy as np
    mac = np.random.normal(mean, deviation, size)
    return mac


def create_uniform_distribution(mu, sigma, size):
    import numpy
    return numpy.random.uniform(low=mu - 2 * sigma, high=mu + 2 * sigma, size=size)


def choose_distribution(type_distribution, mu, sigma, c):
    if type_distribution == '1':
        return normal_distribution(mu, sigma, int(c / mu) - 1)
    elif type_distribution == '2':
        return create_normal_distribution(mu, sigma, int(c / mu))
