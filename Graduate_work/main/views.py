import json
import os

from flask import render_template, request, redirect, json, url_for

from . import *
from .forms import *
from ..Classifier import *


@main.route('/interface', methods=['GET', 'POST'])
def interface():
    # Todo записать в таблицу данные с формы
    form = InterfaceForm()
    if request.method == 'POST': #and form.validate_on_submit():  # TODO check why form is not valid
        insert_in_set_table(form)
        create_tasks(form)
        return redirect('/')
    return render_template("interface.html", form=form)


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@main.route('/result_task', methods=['GET','POST'])
def result_task():
    from .convert_table import convert_set_to_dict
    from .convert_table import convert_task_to_dict
    if request.method == 'GET':
        option_set, option_task, option_algo = output_from_task_table()
        with open(os.path.join(os.path.dirname(__file__), "columns.json")) as f:
            config = json.load(f)
        f.close()
        # print('already GET')
        return render_template('result_task.html',
                           data=convert_task_to_dict(option_task),
                           columns=config['tasks'],
                           title='Індивідуальні задачі',
                           data1=convert_set_to_dict(option_set),
                           columns1=config['set'],
                           title1='Вхідні дані для генерації')
    else:
        id = request.form['id']
        from_val = request.form['from']
        to_val = request.form['to']
        #print(id, from_val, to_val)
        update_value(id, from_val, to_val)
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


@main.route('/statistic', methods=['GET', 'POST'])
def create_stat(chartID='chart_ID', chart_type='line', chart_height=500):

    form = StatisticForm()


    if request.method == 'POST':
        print('PSOT',request.form.get('Time_submit'))
        if request.form.get('Time_submit') == 'Time':
            query1, query2 = output_stat_ave_time(form.id1.data, form.id2.data)
            machine_count, first_time, second_time = create_graph(query1, query2)
            chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, }
            series = [{"name": 'Час виконання першому сеті', "data": first_time},
                  {"name": 'Час виконання на другому сеті', "data": second_time}]
            title = {"text": 'Порівняння часу виконання для різної кількості машин'}
            xAxis = {"categories": machine_count}
            yAxis = {"title": {"text": 'Час виконання'}}
            return redirect(url_for('main.graph', first_time=first_time, second_time=second_time, machine_count=machine_count))

        elif request.form.get('Relative_submit')=='Relative_Projection':
            query11, query22 = output_stat_ave_relative_projection(form.id1.data, form.id2.data)
            machine_count, first_time, second_time = create_graph(query11, query22)
            chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, }
            series = [{"name": 'Відносне відхидення в першому сеті', "data": first_time},
                      {"name": 'Відносне відхидення другому сеті', "data": second_time}]
            title = {"text": 'Порівняння відносної відхиленності для різної кількості машин'}
            xAxis = {"categories": machine_count}
            yAxis = {"title": {"text": 'Час виконання'}}
            return redirect(
                url_for('main.time_graph', first_time=first_time, second_time=second_time, machine_count=machine_count))

    return render_template('statistic.html', form=form)

@main.route('/result_classifier', methods=['GET'])
def result_classifier():
    list_classifier = output_from_classifier_table()
    with open(os.path.join(os.path.dirname(__file__), "columns.json")) as f:
        config = json.load(f)
    f.close()
    from .convert_table import convert_classifier_to_dict
    return render_template('result_classifier.html',
                           data=convert_classifier_to_dict(list_classifier),
                           columns=config['classifier'],
                           title='Значення меж класифікатору')


@main.route('/options', methods=['POST', 'GET'])
def options():
    form = OptionForm()
    if request.method == 'POST': #and form.validate_on_submit():
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
    from .convert_table import convert_data_to_dict
    return render_template('show_result.html',
                           data=convert_data_to_dict(option_algo),
                           columns=config['algo'],
                           title='Початкові розклади')


@main.route('/graph')
def graph(chartID='chart_ID', chart_type='line', chart_height=500):
    first_time = [float(i) for i in request.args.getlist('first_time')]
    second_time = [float(i) for i in request.args.getlist('second_time')]
    machine_count = [int(i) for i in request.args.getlist('machine_count')]


    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, }
    series = [{"name": 'Час виконання першому сеті', "data": first_time},
              {"name": 'Час виконання на другому сеті', "data": second_time}]
    title = {"text": 'Порівняння часу виконання для різної кількості машин'}
    xAxis = {"categories": machine_count}
    yAxis = {"title": {"text": 'Час виконання'}}



    return render_template('graph.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis,
                           yAxis=yAxis)


@main.route('/time_graph')
def time_graph(chartID='chart_ID', chart_type='line', chart_height=500):
    first_time = [float(i) for i in request.args.getlist('first_time')]
    second_time = [float(i) for i in request.args.getlist('second_time')]
    machine_count = [int(i) for i in request.args.getlist('machine_count')]

    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, }
    series = [{"name": 'Час виконання першому сеті', "data": first_time},
              {"name": 'Час виконання на другому сеті', "data": second_time}]
    title = {"text": 'Порівняння часу виконання для різної кількості машин'}
    xAxis = {"categories": machine_count}
    yAxis = {"title": {"text": 'Час виконання'}}

    return render_template('time_graph.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis,
                           yAxis=yAxis)


def update_value(id,from_val,to_val):
    # TODO end method
    from ..models import Task
    from .. import db
    import json
    tasks = Task.query.filter_by(id=int(id)).first()
    task_list = list(json.loads(tasks.tasks))
    print(type(task_list), task_list)
    task_list[task_list.index(int(from_val))] = int(to_val)
    tasks.tasks = json.dumps(task_list)
    db.session.commit()
    print('task list {0}'.format(task_list))
