from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class Lredit_form(FlaskForm):
    lead_rating = IntegerField('New Project Lead Rating', validators = [DataRequired()])


class Sredit_form(FlaskForm):
    self_rating =  IntegerField('New Self Rating', validators = [DataRequired()])