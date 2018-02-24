from flask import render_template

from . import main
from .forms import *


@main.route('/', methods=['GET', 'POST'])
def index():
    form = ClassifierForm()
    # TODO add classifier interaction
    return render_template("interface.html")
