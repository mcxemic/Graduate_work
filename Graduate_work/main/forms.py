from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, FloatField
from wtforms.validators import NumberRange, InputRequired


class OptionForm(FlaskForm):
    P_XS = IntegerField('XS', validators=[InputRequired(), NumberRange(1, 100)])
    P_S = IntegerField('S ')
    P_M = IntegerField('M ')
    P_L = IntegerField('L ')
    P_XL = IntegerField('XL')
    Q_XS = FloatField('XS')
    Q_S = FloatField('S ')
    Q_M = FloatField('M ')
    Q_L = FloatField('L ')
    Q_XL = FloatField('XL')
    H_XS = FloatField('XS')
    H_S = FloatField('S ')
    H_M = FloatField('M ')
    H_L = FloatField('L ')
    H_XL = FloatField('XL')
    C = IntegerField('C ')

class InterfaceForm(FlaskForm):
    n_min = IntegerField('від')
    n_max = IntegerField('до')
    n_step = IntegerField('крок')
    I_type = SelectField(u'Тип пристрою', choices=[(1, 'Ідентичні'), (2, 'Пропорційні'), (3, 'Незв\'язні')])
    P = SelectField(u'P', choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL')])
    Q = SelectField(u'H', choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL')])
    H = SelectField(u'Q', choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL')])
    distribution = SelectField(u'Закон розподілу', choices=[(1, 'Нормальний'), (2, 'Рівномірний')])
    amount_of_tasks = IntegerField('Кількість індивідуальних задач')
    initial_schedule = SelectField(u'Алгоритм генерації початкового розкладу', choices=[(1, 'Алгоритм 1'), (2, 'Алгоритм 2')])
    gen_algo = SelectField(u'Алгоритм генерації', choices=[(1, 'Нормальний'), (2, 'Рівномірний')])


    # Todo add criterion
