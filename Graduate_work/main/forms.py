from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, FloatField, TextField
from wtforms.validators import NumberRange, InputRequired, Email, Required


class OptionForm(FlaskForm):
    P_XS = IntegerField('XS',
                        validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                    NumberRange(1, 100, message='Невірне значення! ( від _до _)')])
    P_S = IntegerField('S ',
                       validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                   NumberRange(1, 100, message='Невірне значення! ( від _до _)')])
    P_M = IntegerField('M ',
                       validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                   NumberRange(1, 100, message='Невірне значення! ( від _до _)')])
    P_L = IntegerField('L ',
                       validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                   NumberRange(1, 100, message='Невірне значення! ( від _до _)')])
    P_XL = IntegerField('XL',
                        validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                    NumberRange(1, 100, message='Невірне значення! ( від _до _)')])
    Q_XS = FloatField('XS',
                      validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                  NumberRange(0.0, 1, message='Невірне значення! ( від _до _)')])
    Q_S = FloatField('S ',
                     validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                 NumberRange(0, 1, message='Невірне значення! ( від _до _)')])
    Q_M = FloatField('M ',
                     validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                 NumberRange(0, 1, message='Невірне значення! ( від _до _)')])
    Q_L = FloatField('L ',
                     validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                 NumberRange(0, 1, message='Невірне значення! ( від _до _)')])
    Q_XL = FloatField('XL',
                      validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                  NumberRange(0, 1, message='Невірне значення! ( від _до _)')])
    H_XS_to = FloatField('XS',
                         validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                     NumberRange(0, 100, message='Невірне значення! ( від _до _)')])
    H_S_to = FloatField('S ',
                        validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                    NumberRange(0, 100, message='Невірне значення! ( від _до _)')])
    H_M_to = FloatField('M ',
                        validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                    NumberRange(0, 100, message='Невірне значення! ( від _до _)')])
    H_L_to = FloatField('L ',
                        validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                    NumberRange(0, 100, message='Невірне значення! ( від _до _)')])
    H_XL_to = FloatField('XL',
                         validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                     NumberRange(0, 100, message='Невірне значення! ( від _до _)')])
    H_XS_from = FloatField('XS',
                           validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                       NumberRange(0, 100, message='Невірне значення! ( від _до _)')])
    H_S_from = FloatField('S ',
                          validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                      NumberRange(0, 100, message='Невірне значення! ( від _до _)')])
    H_M_from = FloatField('M ',
                          validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                      NumberRange(0, 100, message='Невірне значення! ( від _до _)')])
    H_L_from = FloatField('L ',
                          validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                      NumberRange(0, 100, message='Невірне значення! ( від _до _)')])
    H_XL_from = FloatField('XL',
                           validators=[InputRequired(message='Заповніть обов\'язкове поле!'),
                                       NumberRange(0, 100, message='Невірне значення! ( від _до _)')])


class InterfaceForm(FlaskForm):
    n_min = IntegerField('від')
    n_max = IntegerField('до')
    n_step = IntegerField('крок')
    I_type = SelectField(u'Тип', choices=[(1, 'Ідентичні'), (2, 'Пропорційні'), (3, 'Незв\'язні')])
    P = SelectField(u'P', choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL')])
    Q = SelectField(u'Q', choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL')])
    H = SelectField(u'H', choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL')])
    distribution = SelectField(u'Закон розподілу', choices=[(1, 'Нормальний'), (2, 'Рівномірний')])
    amount_of_tasks = IntegerField('Кількість індивідуальних задач')
    gen_algo = SelectField(u'Алгоритм генерації', choices=[(1, 'Рівномірний'), (2, 'Нерівномірний')])
    add_opt_task = SelectField(u'Допоміжні оптимізаційні задачі', choices=[(1, '1'), (2, '2')])
    C = IntegerField('C *')

class StatisticForm(FlaskForm):
    id1 = IntegerField()
    id2 = IntegerField()
    paramsY = SelectField(u'Q', choices=[(1, 'machine'), (2, 'something')])
    paramsX = SelectField(u'Q', choices=[(1, 'opt'), (2, 'time')])