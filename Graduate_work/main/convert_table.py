# TODO: оптимизировать функции конвертации в таблицы и перенести в другой файл
def convert_data_to_dict(option_algo):
    out = []
    for i in option_algo:
        dic = {'id_task': i.task_id, 'initial_timetable_second_alg': i.initial_timetable_second_alg,
               'initial_timetable_first_alg': i.initial_timetable_first_alg}
        out.append(dic)
    return out


def convert_classifier_to_dict(option):
    out = []
    for i in option:
        dic = {'id': i.id, 'duration_p': i.duration_p, 'scattering_q': i.scattering_q, 'dispersion_h': i.dispersion_h}
        out.append(dic)
    return out


def convert_task_to_dict(option):
    out = []
    for i in option:
        dic = {'id': i.id, 'set_id': i.set_id, 'productivity_factor': i.productivity_factor,
               'devises_amount': i.devises_amount, 'tasks': i.tasks}
        out.append(dic)
    return out


def convert_set_to_dict(option):
    out = []
    for i in option:
        dic = {'id': i.id, 'size_p': i.size_p, 'size_q': i.size_q, 'size_h': i.size_h, 'type_device': i.type_device,
               'tasks_count': i.tasks_count, 'distribution': i.distribution}
        out.append(dic)
    return out