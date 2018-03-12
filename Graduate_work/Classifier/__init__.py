from sqlalchemy.sql.expression import func

from . import *
from . import views


# classifiers = Blueprint('classifier', __name__)



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
    sets = {'P': form.P.data, 'Q': form.Q.data, 'H': form.H.data,
            'n_min': form.n_min.data, 'n_max': form.n_max.data, 'n_step': form.n_step.data,
            'I_type': form.I_type.data, 'distribution': form.distribution.data,
            'amount_of_tasks': form.amount_of_tasks.data, 'gen_algo': form.gen_algo.data}
    print("sets", sets)
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
    from ..models import Task, Set
    out_set = Set.query.all()
    out_task = Task.query.all()
    return out_set, out_task


def create_list_from_form(form):
    duration_p = [form.P_XS.data, form.P_S.data, form.P_M.data, form.P_L.data, form.P_XL.data]
    scattering_q = [form.Q_XS.data, form.Q_S.data, form.Q_M.data, form.Q_L.data, form.Q_XL.data]
    dispersion_h = [form.H_XS.data, form.H_S.data, form.H_M.data, form.H_L.data, form.H_XL.data]
    return duration_p, scattering_q, dispersion_h


def create_tasks(form):
    from ..models import Set, Classifier, Task
    from .. import db
    from ..main import big_fucking_function
    import json
    C = 1000
    devises = list(range(form.n_min.data, form.n_max.data, form.n_step.data))
    print(devises)
    # TODO get data from set form
    classifiers = db.session.query(Classifier).order_by(Classifier.id)[-1]
    scat_Q = return_classifier_value(form.Q.data, json.loads(classifiers.scattering_q))
    dur_P = return_classifier_value(form.P.data, json.loads(classifiers.duration_p))
    dis_h = return_classifier_value(form.H.data, json.loads(classifiers.dispersion_h))
    # TODO get last classifier
    # TODO generate task from set form
    productivity_factors = set_of_productivity(devises, form.I_type.data)
    devises_amount = len(productivity_factors)
    set_id = db.session.query(Set).order_by(Set.id)[-1].id
    s = big_fucking_function(form.amount_of_tasks.data, devises, dur_P, scat_Q, C)


    # TODO write tasks to task database
    for i in range(form.amount_of_tasks.data):
        tsk = Task(set_id=set_id, productivity_factor=json.dumps(productivity_factors),
                   devises_amount=devises_amount, tasks=json.dumps(s[i]))
        db.session.add(tsk)
        db.session.commit()


def create_productivity_factor(length, type, k_list=None):
    if type == '1':
        return length * [1]
    else:
        return k_list


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


def set_of_productivity(count_devices, type):
    sets_of_machine = []
    for i in count_devices:
        sets_of_machine.append(create_productivity_factor(i, type))
    return sets_of_machine
