from flask import render_template, request, redirect

from . import main
from .forms import *
from ..Classifier import *


@main.route('/interface', methods=['GET', 'POST'])
def interface():
    # Todo записать в таблицу данные с формы


    form = InterfaceForm()
    if request.method == 'POST':  # TODO check why form is not valid

        insert_in_set_table(form)
        create_tasks(form)
        return redirect('/')
    return render_template("interface.html", form=form)


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@main.route('/result_task', methods=['GET'])
def result_task():
    option_set, option_task = output_from_task_table()

    return render_template("result_task.html", option_set=option_set, option_task=option_task)


@main.route('/result_classifier', methods=['GET'])
def result_classifier():
    option = output_from_classifier_table()
    return render_template("result_options.html", option=option)


@main.route('/options', methods=['POST', 'GET'])
def options():
    form = OptionForm()
    if request.method == 'POST':
        json_form_data = json_from_option_form(form)
        insert_in_classifier_table(duration_p=json_form_data[0],
                                   scattering_q=json_form_data[1],
                                   dispersion_h=json_form_data[2])
        print("insert succsessfull", json_form_data)
        return redirect('/interface')
    return render_template("options.html", form=form)


@main.route('/deleteall', )
def delete():
    from ..models import Classifier, Set, Task
    from .. import db
    db.session.query(Task).delete()
    db.session.query(Set).delete()
    db.session.query(Classifier).delete()
    db.session.commit()
    return render_template('deleteall.html')
