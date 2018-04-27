import os
from flask import render_template, request, redirect, json

from . import *
from .forms import *
from ..Classifier import *


@main.route('/interface', methods=['GET', 'POST'])
def interface():
    # Todo записать в таблицу данные с формы
    form = InterfaceForm()
    if request.method == 'POST':  # & form.validate_on_submit():  # TODO check why form is not valid
        insert_in_set_table(form)
        create_tasks(form)
        return redirect('/')
    return render_template("interface.html", form=form)


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@main.route('/result_task', methods=['GET'])
def result_task():
    option_set, option_task, option_algo = output_from_task_table()
    with open(os.path.join(os.path.dirname(__file__), "columns.json")) as f:
        config = json.load(f)
    f.close()
    return render_template('result_task.html',
                           data=convert_task_to_dict(option_task),
                           columns=config['tasks'],
                           title='Індивідуальні задачі',
                           data1=convert_set_to_dict(option_set),
                           columns1=config['set'],
                           title1='Вхідні дані для генерації')




@main.route('/result_classifier', methods=['GET'])
def result_classifier():
    list_classifier = output_from_classifier_table()
    with open(os.path.join(os.path.dirname(__file__), "columns.json")) as f:
        config = json.load(f)
    f.close()
    return render_template('result_classifier.html',
                           data=convert_classifier_to_dict(list_classifier),
                           columns=config['classifier'],
                           title='Значення таблиці класифікатор')


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


@main.route('/show_result', )
def show_output():
    option_set, option_task, option_algo = output_from_task_table()
    with open(os.path.join(os.path.dirname(__file__), "columns.json")) as f:
        config = json.load(f)
    f.close()
    return render_template('show_result.html',
                           data=convert_data_to_dict(option_algo),
                           columns=config['algo'],
                           title='Побудовані початкові розклади')


# TODO: оптимизировать функции конвертации в таблицы и перенести в другой файл
def convert_data_to_dict(option_algo):
    out = []
    for i in option_algo:
        dic = {'id_task': i.task_id, 'initial_timetable_second_alg': i.initial_timetable_second_alg,
               'initial_timetable_first_alg': i.initial_timetable_first_alg}
        out.append(dic)
    return out


def convert_classifier_to_dict(option):
    out = []
    for i in option:
        dic = {'id': i.id, 'duration_p': i.duration_p, 'scattering_q': i.scattering_q, 'dispersion_h': i.dispersion_h}
        out.append(dic)
    return out


def convert_task_to_dict(option):
    out = []
    for i in option:
        dic = {'id': i.id, 'set_id': i.set_id, 'productivity_factor': i.productivity_factor,
               'devises_amount': i.devises_amount, 'tasks': i.tasks}
        out.append(dic)
    return out


def convert_set_to_dict(option):
    out = []
    for i in option:
        dic = {'id': i.id, 'size_p': i.size_p, 'size_q': i.size_q, 'size_h': i.size_h, 'type_device': i.type_device,
               'tasks_count': i.tasks_count, 'distribution': i.distribution,
               'algorithm_generation': i.algorithm_generation}
        out.append(dic)
    return out
