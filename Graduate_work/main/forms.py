from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField
from wtforms.validators import NumberRange, InputRequired

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
    gen_algo = SelectField(u'Алгоритм генерації', choices=[(1, 'Нормальний'), (2, 'Рівномірний')])


class OptionForm(FlaskForm):
    P_XS = IntegerField('XS', validators=[InputRequired(), NumberRange(1, 100)])
    P_S = IntegerField('S ')
    P_M = IntegerField('M ')
    P_L = IntegerField('L ')
    P_XL = IntegerField('XL')
    Q_XS = IntegerField('XS')
    Q_S = IntegerField('S ')
    Q_M = IntegerField('M ')
    Q_L = IntegerField('L ')
    Q_XL = IntegerField('XL')
    H_XS = IntegerField('XS')
    H_S = IntegerField('S ')
    H_M = IntegerField('M ')
    H_L = IntegerField('L ')
    H_XL = IntegerField('XL')
    C = IntegerField('C ')