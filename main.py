from Classifier.create_classifier import *
from Generator.input_data import *

def classifier_interface():
    print("Hello! Input scope of the duration of classifier.")
    duration_args = duration_input()
    print("Scattering scope")
    scattering_args = scattering_input()
    print("Monotonous scope")
    monotonuos_args = monotonuos_input()
    duration, monotonuos, scattering = create_classifier(duration_args, monotonuos_args, scattering_args)
    print(duration.__dict__, monotonuos.__dict__, scattering.__dict__)


def generation_input():
    start, stop, step, count = input_devices()
    devices = create_devices(start, stop, step, count)
    print(devices)



if __name__ == '__main__':
    classifier_interface()
    # generation_input()
