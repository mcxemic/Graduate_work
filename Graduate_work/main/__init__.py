from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors


def big_fucking_function(count_set, count_devices, mean_duration_P, deviation_duration_Q, C):
    sets = []
    for _ in range(count_set):
        sets.append([])
    for j in range(len(count_devices)):
        sets[j].append(set_of_machine(count_devices[j], mean_duration_P, deviation_duration_Q, C))
    return sets


def create_normal_distribution(mu, sigma, size=1):
    import numpy.random as np
    x = np.normal(mu, sigma, size)
    return int(x)


def set_of_machine(count_devices, mu, sigma, C):
    sets_of_machine = []
    for i in range(count_devices):
        sets_of_machine.append(create_machine(mu, sigma, C))
    return sets_of_machine


def create_machine(mu, sigma, c):
    machine = []
    while sum(machine) < c:
        if sum(machine) < c - mu - sigma:
            machine.append(create_normal_distribution(mu, sigma))
        else:
            machine.append(c - sum(machine))
    return machine
