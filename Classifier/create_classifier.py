from .DurationClassifier import *
from .MonotonousClassifier import *
from .ScatteringClassifier import *


def create_classifier(duration_args, monotonous_args, scattering_args):
    # create exampler of three classifier

    duration = DurationClassifier(duration_args[0], duration_args[1],
                                  duration_args[2], duration_args[3], duration_args[4])
    monotonous = MonotonousClassifier(monotonous_args[0], monotonous_args[1],
                                      monotonous_args[2], monotonous_args[3], monotonous_args[4],
                                      monotonous_args[5], monotonous_args[6],
                                      monotonous_args[7], monotonous_args[8], monotonous_args[9])
    scattering = ScatteringClassifier(scattering_args[0], scattering_args[1],
                                      scattering_args[2], scattering_args[3], scattering_args[4])

    return duration, monotonous, scattering


def duration_input():
    # TODO check for nonzero numeric increasing (test)
    # TODO add exception checking
    duration_args = []
    duration_args.append(input("XS = "))
    duration_args.append(input("S = "))
    duration_args.append(input("M = "))
    duration_args.append(input("L = "))
    duration_args.append(input("XL = "))
    return duration_args


def monotonuos_input():
    # TODO check for nonzero numeric increasing (test)
    # TODO add exception checking
    monotonuos_args = []
    monotonuos_args.append(input("from XS = "))
    monotonuos_args.append(input("to XS = "))
    monotonuos_args.append(input("from S = "))
    monotonuos_args.append(input("to S = "))
    monotonuos_args.append(input("from M = "))
    monotonuos_args.append(input("to M = "))
    monotonuos_args.append(input("from L = "))
    monotonuos_args.append(input("to L = "))
    monotonuos_args.append(input("from XL = "))
    monotonuos_args.append(input("to XL = "))

    return monotonuos_args


def scattering_input():
    # TODO check for nonzero numeric increasing (test)
    # TODO add exception checking
    scattering_args = []
    scattering_args.append(input("XS = "))
    scattering_args.append(input("S = "))
    scattering_args.append(input("M = "))
    scattering_args.append(input("L = "))
    scattering_args.append(input("XL = "))
    return scattering_args
