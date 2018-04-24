from . import views
from ..main import algorithms


def list_from_object(duration_p, scattering_q, dispersion_h):
    duration_p_dict = create_dict_from_list(duration_p)
    scattering_q_dict = create_dict_from_list(scattering_q)
    dispersion_h_dict = create_dict_from_list(dispersion_h)
    return duration_p_dict, scattering_q_dict, dispersion_h_dict


def json_from_option_form(form):
    duration_p, scattering_q, dispersion_h = create_list_from_form(form)
    duration_p_dict, scattering_q_dict, dispersion_h_dict = list_from_object(duration_p, scattering_q, dispersion_h)
    duration_p_json, scattering_q_json, dispersion_h_json = create_JSON_from_dict(duration_p_dict, scattering_q_dict,
                                                                                  dispersion_h_dict)
    return [duration_p_json, scattering_q_json, dispersion_h_json]


def create_dict_from_list(object):
    object_dict = {}

    object_dict['XS'] = object[0]
    object_dict['S'] = object[1]
    object_dict['M'] = object[2]
    object_dict['L'] = object[3]
    object_dict['XL'] = object[4]
    return object_dict


def create_JSON_from_dict(object1, object2, object3):
    import json
    object_json1 = json.dumps(object1)
    object_json2 = json.dumps(object2)
    object_json3 = json.dumps(object3)
    return object_json1, object_json2, object_json3


def insert_in_classifier_table(duration_p, scattering_q, dispersion_h):
    from ..models import Classifier
    from .. import db
    cl = Classifier(duration_p=duration_p, scattering_q=scattering_q, dispersion_h=dispersion_h)
    db.session.add(cl)
    db.session.commit()


def insert_in_set_table(form):
    from ..models import Set, Classifier
    from .. import db
    from sqlalchemy import func
    sets = {'P': form.P.data, 'Q': form.Q.data, 'H': form.H.data,
            'n_min': form.n_min.data, 'n_max': form.n_max.data, 'n_step': form.n_step.data,
            'I_type': form.I_type.data, 'distribution': form.distribution.data,
            'amount_of_tasks': form.amount_of_tasks.data, 'gen_algo': form.initial_schedule.data}

    st = Set(size_q=sets['Q'], size_h=sets['H'], size_p=sets['P'],
             classifier_id=db.session.query(func.max(Classifier.id)),
             type_device=sets['I_type'], tasks_count=sets['amount_of_tasks'],
             distribution=sets['distribution'], algorithm_generation=sets['gen_algo'])
    db.session.add(st)
    db.session.commit()


def output_from_classifier_table():
    from ..models import Classifier
    out = Classifier.query.all()
    return out


def output_from_task_table():
    from ..models import Task, Set, Algorithm
    # Return the results represented by this Query as a list.
    out_set = Set.query.all()
    out_task = Task.query.all()
    out_algo = Algorithm.query.all()
    return out_set, out_task, out_algo


def create_list_from_form(form):
    duration_p = [form.P_XS.data, form.P_S.data, form.P_M.data, form.P_L.data, form.P_XL.data]
    scattering_q = [form.Q_XS.data, form.Q_S.data, form.Q_M.data, form.Q_L.data, form.Q_XL.data]
    dispersion_h = generate_H_from_form(form)
    return duration_p, scattering_q, dispersion_h


def generate_H_from_form(form):
    import random as rd
    h = [round(rd.uniform(form.H_XS_from.data, form.H_XS_to.data), 3),
         round(rd.uniform(form.H_S_from.data, form.H_S_to.data), 3),
         round(rd.uniform(form.H_M_from.data, form.H_M_to.data), 3),
         round(rd.uniform(form.H_L_from.data, form.H_L_to.data), 3),
         round(rd.uniform(form.H_XL_from.data, form.H_XL_to.data), 3)]
    return h


def create_tasks(form):
    # TODO rewrite
    from ..models import Set
    from .. import db
    from ..main import generate_sets

    # Todo Проверить закон распределение и передать

    if form.C.data != None:
        C = form.C.data
    else:
        C = 100000

    devises = get_devices(form)
    scat_Q, dur_P, dis_H = get_factors_from_forms(form)
    real_p = C / dur_P
    print(scat_Q, dur_P, real_p)
    real_q = scat_Q * real_p
    productivity_factors = set_of_productivity(devices=devises, type_task=form.I_type.data, coef=dis_H)

    set_id = db.session.query(Set).order_by(Set.id)[-1].id
    # Todo Проверить тип, вызвать и сохранить идентичность или нет
    type_of_algorithm_initial_schedule = get_type_of_algorithm(form)
    sets = generate_sets(form.distribution.data, form.amount_of_tasks.data, devises, real_p, real_q, C,
                         form.gen_algo.data)
    write_to_task_table(form=form, set_id=set_id, productivity_factors=productivity_factors, sets=sets,
                        type_of_algorithm=type_of_algorithm_initial_schedule, C=C)
    # algorithms.run_algorithms(productivity_factors,sets,set_id,form.initial_schedule.data)


def get_type_of_algorithm(form):
    if form.initial_schedule.data == '1':
        return 1
    else:
        return 2


def return_classifier_value(sets, classifier):
    if sets == '1':
        return classifier.get('XS')
    elif sets == '2':
        return classifier.get('S')
    elif sets == '3':
        return classifier.get('M')
    elif sets == '4':
        return classifier.get('L')
    elif sets == '5':
        return classifier.get('XL')


def get_devices(form): return list(range(form.n_min.data, form.n_max.data, form.n_step.data))


def set_of_productivity(devices, type_task, coef):
    sets_of_machine = []
    for i in devices:
        sets_of_machine.append(check_type_of_task(type_task, i, coef))
    return sets_of_machine


def get_factors_from_forms(form):
    from ..models import Classifier
    from .. import db
    import json

    classifiers = db.session.query(Classifier).order_by(Classifier.id)[-1]
    print('Classifiers ', classifiers)
    scat_Q = return_classifier_value(form.Q.data, json.loads(classifiers.scattering_q))
    dur_P = return_classifier_value(form.P.data, json.loads(classifiers.duration_p))
    dis_h = return_classifier_value(form.H.data, json.loads(classifiers.dispersion_h))
    print(scat_Q, dur_P, dis_h, ' clas')
    return scat_Q, dur_P, dis_h


def write_to_task_table(form, set_id, productivity_factors, sets, type_of_algorithm, C):
    from ..models import Task
    from .. import db
    import json

    for i in range(form.amount_of_tasks.data):
        tsk = Task(set_id=set_id, productivity_factor=json.dumps(productivity_factors[i]),
                   devises_amount=len(productivity_factors[i]), tasks=json.dumps(sets[i]))
        db.session.add(tsk)
        db.session.commit()
        task_id = db.session.query(Task).order_by(Task.id)[-1].id
        algorithms.run_algorithms(type_of_algorithm, productivity_factors, sets, task_id, C)


def check_type_of_task(type_task, device_amount, coeff=None):
    if type_task == '1':
        productivity_factors = device_amount * [1]
        return productivity_factors
    elif type_task == '2':
        productivity_factors = get_productivity_factors(device_amount, coeff)
        return productivity_factors
    else:
        pass


def get_productivity_factors(length, coef):
    productive_factors = [1]
    for i in range(length - 1):
        productive_factors.append(productive_factors[-1] * coef)
    return productive_factors
