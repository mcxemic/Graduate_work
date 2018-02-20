from .DurationClassifier import *
from .Exceptions import *
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
    #
    # TODO check for nonzero numeric increasing (test)

    try:
        duration_args = []

        XS = int(input("XS = "))
        if isinstance(XS, int) and XS > 0:
            duration_args.append(XS)
        else:
            raise NegativeException()

        S = int(input("S = "))
        if isinstance(S, int) and S > 0:
            duration_args.append(S)
        else:
            raise NegativeException()

        M = int(input("M = "))
        if isinstance(M, int) and M > 0:
            duration_args.append(M)
        else:
            raise NegativeException()

        L = int(input("L = "))
        if isinstance(L, int) and L > 0:
            duration_args.append(L)
        else:
            raise NegativeException()

        XL = int(input("XL = "))
        if isinstance(XS, int) and XL > 0:
            duration_args.append(XL)
        else:
            raise NegativeException()

        # TODO rewrite lambda

        return duration_args

    except NegativeException as e:
        print(type(e))
        print(e)
        print("Input valid numbers!")
    except ValueError as e:
        print(type(e))
        print(e)
        print("Input valid numbers!")


def monotonuos_input():
    # TODO check for nonzero numeric increasing (test)

    try:
        monotonuos_args = []

        fromXS = int(input("from XS = "))
        if isinstance(fromXS, int) and fromXS > 0:
            monotonuos_args.append(fromXS)
        else:
            raise NegativeException("Unexpected value")

        toXS = int(input("to XS = "))
        if isinstance(toXS, int) and toXS > 0:
            monotonuos_args.append(toXS)
        else:
            raise NegativeException("Unexpected value")

        fromS = int(input("from S = "))
        if isinstance(fromS, int) and fromS > 0:
            monotonuos_args.append(fromS)
        else:
            raise NegativeException("Unexpected value")

        toS = int(input("to S = "))
        if isinstance(toS, int) and toS > 0:
            monotonuos_args.append(toS)
        else:
            raise NegativeException("Unexpected value")

        fromM = int(input("from M = "))
        if isinstance(fromM, int) and fromM > 0:
            monotonuos_args.append(fromM)
        else:
            raise NegativeException("Unexpected value")

        toM = int(input("to M = "))
        if isinstance(toM, int) and toM > 0:
            monotonuos_args.append(toM)
        else:
            raise NegativeException("Unexpected value")

        fromL = int(input("from L = "))
        if isinstance(fromL, int) and fromL > 0:
            monotonuos_args.append(fromL)
        else:
            raise NegativeException("Unexpected value")

        toL = int(input("to L = "))
        if isinstance(toL, int) and toL > 0:
            monotonuos_args.append(toL)
        else:
            raise NegativeException("Unexpected value")

        fromXL = int(input("from XL = "))
        if isinstance(fromXL, int) and fromXL > 0:
            monotonuos_args.append(fromXL)
        else:
            raise NegativeException("Unexpected value")

        toXL = int(input("from XL = "))
        if isinstance(toXL, int) and toXL > 0:
            monotonuos_args.append(toXL)
        else:
            raise NegativeException("Unexpected value")

        # TODO rewrite lambda

        return monotonuos_args
    except NegativeException as e:
        print(type(e))
        print(e)
        print("Input valid numbers!")
    except ValueError as e:
        print(type(e))
        print(e)
        print("Input valid numbers!")


def scattering_input():
    # TODO check for nonzero numeric increasing (test)

    try:
        scattering_args = []

        XS = int(input("XS = "))
        if isinstance(XS, int) and XS > 0:
            scattering_args.append(XS)
        else:
            raise NegativeException()

        S = int(input("S = "))
        if isinstance(S, int) and S > 0:
            scattering_args.append(S)
        else:
            raise NegativeException()

        M = int(input("M = "))
        if isinstance(M, int) and M > 0:
            scattering_args.append(M)
        else:
            raise NegativeException()

        L = int(input("L = "))
        if isinstance(L, int) and L > 0:
            scattering_args.append(L)
        else:
            raise NegativeException()

        XL = int(input("XL = "))
        if isinstance(XS, int) and XL > 0:
            scattering_args.append(XL)
        else:
            raise NegativeException()

        # TODO rewrite lambda

        return scattering_args
    except NegativeException as e:
        print(type(e))
        print(e)
        print("Input valid numbers!")
    except ValueError as e:
        print(type(e))
        print(e)
        print("Input valid numbers!")
