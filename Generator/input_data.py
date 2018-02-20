import random


def input_devices():
    try:
        print("Count of devices")
        count = int(input("Input count of task"))
        if not isinstance(count, int) and count <= 0:
            raise Exception("Unexpected value")
        start = int(input("From = "))
        if not isinstance(start, int) and start <= 0:
            raise Exception("Unexpected value")
        stop = int(input("Stop = "))
        if not isinstance(stop, int) and stop <= 0:
            raise Exception("Unexpected value")
        step = int(input("Step = "))
        if not isinstance(step, int) and step <= 0:
            raise Exception("Unexpected value")
        return start, stop, step, count
    except:
        print("Input valid numbers!")


def create_devices(start, stop, step, count):
    devices = list(random.randrange(start=start, stop=stop, step=step) for _ in range(count))
    return devices


def choose_type_devices(devices):
    type = {1: 'Indentical', 2: 'Monotonuos', 3: 'Other'}
    print("Choose type of devices")
    print("1 - identical \n2 - Monotonuos\n3 - Other")
    type_num = int(input())
    if type_num not in [1, 2, 3]:
        raise Exception("Unexpected value")
    if type_num == 1:
        h_devices = len(devices) * [1]
        return h_devices
    if type_num == 2:
        # Todo write calculate h array
        pass
    if type_num == 3:
        # Todo write third method
        pass
