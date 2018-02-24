from flask import render_template

from . import main
from .forms import *



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("main.html")


@app.route('/interface', methods=['GET', 'POST'])
def interface():
    form = InterfaceForm()
    return render_template("interface.html", form=form)

@app.route('/options', methods=['GET', 'POST'])
def options():
    form = OptionForm()
    return render_template("options.html", form=form)
