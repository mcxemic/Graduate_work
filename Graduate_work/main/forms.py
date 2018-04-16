from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, FloatField, TextField
from wtforms.validators import NumberRange, InputRequired, Email, Required


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
    H_XS_to = FloatField('XS')
    H_S_to = FloatField('S ')
    H_M_to = FloatField('M ')
    H_L_to = FloatField('L ')
    H_XL_to = FloatField('XL')
    H_XS_from = FloatField('XS')
    H_S_from = FloatField('S ')
    H_M_from = FloatField('M ')
    H_L_from = FloatField('L ')
    H_XL_from = FloatField('XL')


class InterfaceForm(FlaskForm):
    n_min = IntegerField('від', validators=[
            InputRequired(), Email(message ='ololo'),])
    n_max = IntegerField('до')
    n_step = IntegerField('крок')
    I_type = SelectField(u'Тип', choices=[(1, 'Ідентичні'), (2, 'Пропорційні'), (3, 'Незв\'язні')])
    P = SelectField(u'P', choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL')])
    Q = SelectField(u'H', choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL')])
    H = SelectField(u'Q', choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL')])
    distribution = SelectField(u'Закон розподілу', choices=[(1, 'Нормальний'), (2, 'Рівномірний')])
    amount_of_tasks = IntegerField('Кількість індивідуальних задач', validators=[InputRequired()])
    initial_schedule = SelectField(u'Алгоритм генерації початкового розкладу', choices=[(1, 'Алгоритм 1'), (2, 'Алгоритм 2')])
    gen_algo = SelectField(u'Алгоритм генерації', choices=[(1, 'Нормальний'), (2, 'Рівномірний')])
    add_opt_task = SelectField(u'Допоміжні оптимізаційні задачі', choices=[(1, '1'), (2, '2')])
    C = IntegerField('C ')
