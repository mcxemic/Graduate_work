from flask import render_template

from . import main
from .forms import *
from ..Classifier import *


@main.route('/', methods=['GET', 'POST'])
def index():
    form = MainForm()
    return render_template("interface.html", form=form)


@main.route('/options', methods=['POST', 'GET'])
def options():
    from ..models import Classifier
    form = OptionForm()
    duration_p, scattering_q, dispersion_h = create_list_from_form(form)
    duration_p_dict = create_dict_from_list(duration_p)
    scattering_q_dict = create_dict_from_list(scattering_q)
    dispersion_h_dict = create_dict_from_list(dispersion_h)
    duration_p_json = create_JSON_from_dict(duration_p_dict)
    scattering_q_json = create_JSON_from_dict(scattering_q_dict)
    dispersion_h_json = create_JSON_from_dict(dispersion_h_dict)
    insert_in_classifier_table(duration_p=duration_p_json,
                               scattering_q=scattering_q_json,
                               dispersion_h=dispersion_h_json, tablename=Classifier.__tablename__)


    return render_template("options.html", form=form)
