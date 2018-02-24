from flask import render_template

from . import main
from .forms import *


@main.route('/', methods=['GET', 'POST'])
def index():
    form = MainForm()
    # TODO add classifier interaction
    return render_template("interface.html", form=form)


@main.route('/options', methods=['POST', 'GET'])
def options():
    form = OptionForm()
    return render_template("options.html", form=form)
