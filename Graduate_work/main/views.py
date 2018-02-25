from flask import render_template

from . import main
from .forms import *
from ..Classifier import *


@main.route('/interface', methods=['GET', 'POST'])
def interface():
    form = InterfaceForm()
    return render_template("interface.html", form=form)


@main.route('/options', methods=['POST', 'GET'])
def options():
    form = OptionForm()

    json_form_data = json_from_form(form)
    insert_in_classifier_table(duration_p=json_form_data[0],
                               scattering_q=json_form_data[1],
                               dispersion_h=json_form_data[2])
    return render_template("options.html", form=form)


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@main.route('/result_1', methods=['GET'])
def result():
    option = output_from_classifier_table()
    print(option)
    return render_template("result_options.html", option=option)
