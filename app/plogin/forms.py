from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired


class Lr_edit_form(FlaskForm):
    skill_select = SelectField('Select the skill for which lead rating needs to be edited', choices = [])
    lead_rating = IntegerField('New Project Lead Rating', validators = [DataRequired()])

class Sr_edit_form(FlaskForm):
    skill_select = SelectField('Select the skill for which Self rating needs to be edited', choices = [])
    self_rating = IntegerField('New Self Rating', validators = [DataRequired()])



class Skill_search_form(FlaskForm):
    skill_select = SelectField('Select skill', choices = [])

class Loc_search_form(FlaskForm):
    loc_select = SelectField('Location Select', choices = [])