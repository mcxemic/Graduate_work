from . import db


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

    child = db.relationship("Task")


    # TODO __repr__


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    set_id = db.Column(db.Integer, db.ForeignKey('sets.id'))
    productivity_factor = db.Column(db.JSON)
    devises_amount = db.Column(db.Integer)
    tasks = db.Column(db.JSON)
    first_Optimization = db.Column(db.JSON)
    first_projection = db.Column(db.Float)
    first_lead_time = db.Column(db.Float)
    first_relatively_projection= db.Column(db.Float)
    first_iteration_count = db.Column(db.Float)

    # TODO __repr__


class Algorithm(db.Model):
    __tablename__ = 'algorithms'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
    initial_timetable_first_alg = db.Column(db.JSON)
    initial_timetable_second_alg = db.Column(db.JSON)


class Optimization(db.Model):
    __tablename__ = 'optimization'

    id = db.Column(db.Integer,primary_key=True)
    alg_id = db.Column(db.Integer,db.ForeignKey('algorithms.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))

