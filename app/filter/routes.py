from flask import render_template, redirect, url_for, request, flash, jsonify
from app import db
from app.plogin.models import Project
from app.plogin.models import Employee
from app.plogin.models import Skill
from app.plogin.models import Emp_skill
from app.plogin import pdash
from app.filter import filtr
from app.filter.forms import Filter_form
import json
from flask import jsonify

@filtr.route('/efilter', methods  = ['GET','POST'])
def efilter():
    emp_skill = None
    filter_form = Filter_form()
    filter_form.skill.choices = [(skill.skill_id,skill.skill_name) for skill in Skill.query.all()]
    #filter_form.exp.choices = [(emp_skill.experience, emp_skill.experience) for emp_skill in Emp_skill.query.filter_by(skill_id = filter_form.skill.data)]
    if request.method == 'POST':
        emp_skill = Emp_skill.query.filter_by(skill_id = filter_form.skill.data).all()
    return render_template('efilter.html', filter_form = filter_form)

@filtr.route('/efilter/<skill>')
def exp(skill):
    emp_details = Emp_skill.query.filter_by(skill_id = skill).all()

    ls = []

    for exp in emp_details:
        expobj = {}
        expobj['exp'] = exp.experience
        ls.append(expobj)

    return jsonify({'experience': ls})