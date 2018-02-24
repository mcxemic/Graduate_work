from flask import Blueprint

dbi = "postgresql://postgres:password@localhost/graduate"
Classifier = Blueprint('Classifier', __name__)

from . import *


def create_dict_from_list(object):
    object_dict = {}
    object_dict['XS'] = object[0]
    object_dict['S'] = object[1]
    object_dict['M'] = object[2]
    object_dict['L'] = object[3]
    object_dict['XL'] = object[4]
    return object_dict


def create_JSON_from_dict(object):
    import json
    object_json = json.dumps(object)
    return object_json


def insert_in_classifier_table(duration_p, scattering_q, dispersion_h, tablename):
    from sqlalchemy import create_engine
    ins = tablename.insert().values(duration_p=duration_p, scattering_q=scattering_q, dispersion_h=dispersion_h)
    engine = create_engine(dbi)
    conn = engine.connect()
    conn.execute(ins)


def create_list_from_form(form):
    duration_p = list(form.P_XS, form.P_S, form.P_M, form.P_L, form.P_XL)
    scattering_q = list(form.Q_XS, form.Q_S, form.Q_M, form.Q_L, form.Q_XL)
    dispersion_h = list(form.H_XS, form.H_S, form.H_M, form.H_L, form.H_XL)
    return duration_p, scattering_q, dispersion_h
