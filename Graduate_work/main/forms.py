from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField
from wtforms.validators import NumberRange, InputRequired


######FORM CLASSES
class MainForm(FlaskForm):
    P = SelectField(u'Programming Language', choices=[(1, 'XS'), (2, 'S'), (2, 'M'), (2, 'L'), (2, 'XL')])
    Q = SelectField(u'Programming Language', choices=[(1, 'XS'), (2, 'S'), (2, 'M'), (2, 'L'), (2, 'XL')])
    H = SelectField(u'Programming Language', choices=[(1, 'XS'), (2, 'S'), (2, 'M'), (2, 'L'), (2, 'XL')])


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
