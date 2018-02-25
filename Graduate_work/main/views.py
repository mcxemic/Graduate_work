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
    print(form)
    objects_json = json_from_form(form)
    insert_in_classifier_table(duration_p=objects_json[0],
                               scattering_q=objects_json[1],
                               dispersion_h=objects_json[2], tablename=Classifier.__tablename__)

    return render_template("options.html", form=form)
