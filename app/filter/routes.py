from flask import render_template, redirect, url_for, request, flash, jsonify
from app import db
from app.plogin.models import Project
from app.plogin.models import Employee
from app.plogin.models import Skill
from app.plogin.models import Emp_skill
from app.plogin import pdash
from app.filter import filtr
from app.filter.forms import Emp_filter_form
import json
from flask import jsonify

@filtr.route('/efilter', methods  = ['GET','POST'])
def efilter():
    emp_skill = None
    employee = None
    emp_filter_form = Emp_filter_form()
    emp_filter_form.skill.choices = [(skill.skill_id,skill.skill_name) for skill in Skill.query.all()]
    if request.method == 'POST':
        emp_skill = Emp_skill.query.filter_by(skill_id = emp_filter_form.skill.data).filter_by(experience = emp_filter_form.exp.data).filter_by(skill_range = emp_filter_form.range.data).order_by(Emp_skill.final_rating.desc()).all()
        employee = Employee.query.all()
    return render_template('newefilter.html', emp_filter_form = emp_filter_form, emp_skill = emp_skill, employee = employee)

@filtr.route('/efilter/<skill>')
def exp(skill):
    emp_details = Emp_skill.query.filter_by(skill_id = skill).all()

    ls = []

    for exp in emp_details:
        expobj = {}
        expobj['exp'] = exp.experience
        ls.append(expobj)

    return jsonify({'experience': ls})

@filtr.route('/efilter/<skill>/<exp>')
def range(skill,exp):
    emp_details = Emp_skill.query.filter_by(skill_id = skill).filter_by(experience = exp).all()
    ls = []

    for range in emp_details:
        rangeobj = {}
        rangeobj['range'] = range.skill_range
        ls.append(rangeobj)

    return jsonify({'range':ls})
