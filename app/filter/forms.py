from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired


class Filter_form(FlaskForm):
    skill = SelectField('Skills', choices = [])
    exp = SelectField('Experience', choices = [])

