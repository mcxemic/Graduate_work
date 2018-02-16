from Classifier.create_classifier import *


def classifier_interface():
    print("Hello! Input scope of the duration of classifier.")
    duration_args = duration_input()
    print("Scattering scope")
    scattering_args = scattering_input()
    print("Monotonous scope")
    monotonuos_args = monotonuos_input()
    duration, monotonuos, scattering = create_classifier(duration_args, monotonuos_args, scattering_args)
    print(duration.__dict__, monotonuos.__dict__, scattering.__dict__)


if __name__ == '__main__':
    classifier_interface()
