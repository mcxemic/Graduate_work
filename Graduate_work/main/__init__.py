from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors


def generate_sets(count_set, count_devices, mean_duration_P, deviation_duration_Q, C):
    sets = []
    print("Count set ", count_set)
    for _ in range(count_set):
        sets.append([])
    for j in range(len(count_devices)):
        sets[j].append(set_of_machine(count_devices[j], mean_duration_P, deviation_duration_Q, C))
    return sets


def create_normal_distribution(mu, sigma, size=1):
    x = normal_distribution_with_limit(start=mu - 2 * sigma, finish=mu + 2 * sigma, mean=mu, deviation=sigma, size=size)
    if x > 0:
        if x > mu + 2 * sigma:
            return int(mu + 2 * sigma)
        else:
            return int(x)
    else:
        return 1


def set_of_machine(count_devices, mu, sigma, C):
    sets_of_machine = []
    for i in range(count_devices):
        sets_of_machine.append(create_machine(mu, sigma, C))
    return sets_of_machine


def create_machine(mu, sigma, c):
    machine = []
    while sum(machine) < c:
        if sum(machine) < c - mu - sigma:
            machine.append(abs(create_normal_distribution(mu, sigma)))
        else:
            machine.append(c - sum(machine))
    return machine


def normal_distribution_with_limit(start, finish, mean, deviation, size):
    arr = get_truncated_normal(mu=mean, sigma=deviation, low=start, up=finish)
    return arr.rvs(size)


def get_truncated_normal(mu=0, sigma=1, low=0, up=10):
    from scipy.stats import truncnorm
    return truncnorm(
        (low - mu) / sigma, (up - mu) / sigma, loc=mu, scale=sigma)


def create_uniform_distribution(mu, sigma, size):
    import numpy
    return numpy.random.uniform(low=mu - 2 * sigma, high=mu + 2 * sigma, size=size)
