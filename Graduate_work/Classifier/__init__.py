from flask import Blueprint

dbi = "postgresql://postgres:password@localhost/graduate"
Classifier = Blueprint('Classifier', __name__)

from . import *


def list_from_object(duration_p, scattering_q, dispersion_h):
    duration_p_dict = create_dict_from_list(duration_p)
    scattering_q_dict = create_dict_from_list(scattering_q)
    dispersion_h_dict = create_dict_from_list(dispersion_h)
    return duration_p_dict, scattering_q_dict, dispersion_h_dict


def json_from_form(form):
    duration_p, scattering_q, dispersion_h = create_list_from_form(form)
    duration_p_dict, scattering_q_dict, dispersion_h_dict = list_from_object(duration_p, scattering_q, dispersion_h)
    duration_p_json, scattering_q_json, dispersion_h_json = create_JSON_from_dict(duration_p_dict, scattering_q_dict,
                                                                                  dispersion_h_dict)
    return [duration_p_json, scattering_q_json, dispersion_h_json]

def create_dict_from_list(object):
    print(object[0])
    object_dict = {}
    object_dict['XS'] = object[0]
    object_dict['S'] = object[1]
    object_dict['M'] = object[2]
    object_dict['L'] = object[3]
    object_dict['XL'] = object[4]
    return object_dict


def create_JSON_from_dict(object1, object2, object3):
    import json
    print("object 1", type(object1), object1)
    object_json1 = json.dumps(object1)

    print('object json 1', object_json1)
    object_json2 = json.dumps(object2)
    object_json3 = json.dumps(object3)
    return object_json1, object_json2, object_json3


def insert_in_classifier_table(duration_p, scattering_q, dispersion_h, tablename):
    from sqlalchemy import create_engine
    ins = tablename.insert().values(duration_p=duration_p, scattering_q=scattering_q, dispersion_h=dispersion_h)
    engine = create_engine(dbi)
    conn = engine.connect()
    conn.execute(ins)


def create_list_from_form(form):
    duration_p = [form.P_XS, form.P_S, form.P_M, form.P_L, form.P_XL]
    scattering_q = [form.Q_XS, form.Q_S, form.Q_M, form.Q_L, form.Q_XL]
    dispersion_h = [form.H_XS, form.H_S, form.H_M, form.H_L, form.H_XL]
    return duration_p, scattering_q, dispersion_h
