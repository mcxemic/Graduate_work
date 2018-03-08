from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors


def create_normal_distribution(a, b, size, distribution):
    average = int((b - a) / 2)
    import numpy as np
    np.random.normal(average, distribution, size)
    pass


def create_uniform_distribution(a, b, size):
    import numpy.random as np
    return [int(x) for x in np.uniform(a, b, size)]
