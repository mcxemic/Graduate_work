import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

POSTGRES = {
    'user': 'IS_42',
    'pw': 'FICT_ASU',
    'db': 'graduate',
    'host': 'localhost',
    'port': '5432',
}

# TODO add secure solution
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s'.format(POSTGRES)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost/graduate"

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Classifier(db.Model):
    __tablename__ = 'classifiers'

    id = db.Column(db.Integer, primary_key=True)
    duration_p = db.Column(db.JSON)
    scattering_q = db.Column(db.JSON)
    dispersion_h = db.Column(db.JSON)
    child = db.relationship("Set")

    def __repr__(self):
        return ('id: {}   P: {}   Q: {}  H: {}'.
                format(self.id, self.duration_p,
                       self.scattering_q, self.dispersion_h))


class Set(db.Model):
    __tablename__ = 'sets'

    id = db.Column(db.Integer, primary_key=True)
    size_p = db.Column(db.String)
    size_q = db.Column(db.String)
    size_h = db.Column(db.String)
    classifier_id = db.Column(db.Integer, db.ForeignKey('classifiers.id'))
    type_device = db.Column(db.String)
    tasks_count = db.Column(db.Integer)
    criterion_device = db.Column(db.String)
    distribution = db.Column(db.String)
    algorithm_generation = db.Column(db.String)

    child = db.relationship("Task")


    # TODO __repr__


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    set_id = db.Column(db.Integer, db.ForeignKey('sets.id'))
    productivity_factors = db.Column(db.ARRAY(db.Float))
    devises_amount = db.Column(db.Integer)
    tasks_amount = db.Column(db.Integer)

    # TODO __repr__


# TODO form for classifier (interface for classifier db table
class ClassifierForm(FlaskForm):
    pass


# TODO form for input (interface for set and task
class BaseInputForm(FlaskForm):
    pass


# create shell for use via terminal
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Classifier=Classifier, Set=Set, Task=Task)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    # TODO add classifier interaction
    return render_template("interface.html")
