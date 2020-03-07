from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired


class Emp_filter_form(FlaskForm):
    skill = SelectField('Skills', choices = [])
    exp = SelectField('Experience', choices = [])
    range = SelectField('Range', choices = [])

