from app.plogin import pdash
from app import db
from app.plogin.models import Skill
from app.plogin.models import Project
from app.plogin.models import Proj_skill
from app.plogin.models import Emp_skill
from app.plogin.models import Employee
from app.plogin.models import Certification
from app.plogin.models import Emp_cert

import pprint

from flask import render_template, redirect, url_for

@pdash.route('/project/<pid>', methods = ['GET','POST'])
def pdetails(pid):
    project = Project.query.filter_by(proj_id =  pid ).first()
    proj_skill = Proj_skill.query.filter_by(proj_id =  pid).all()
    ls = [proj_skill[i].getpSkillId() for i in range(0,len(proj_skill))]
    empl = Employee.query.filter_by(proj_id = pid ).all()
    pskill = Skill.query.filter(Skill.skill_id.in_(ls)).all()
    return render_template('proj_skill.html', proj_skill=proj_skill, project = project, pskill = pskill, empl = empl)

@pdash.route('/employee/<eid>', methods = ['GET','POST'])
def edetails(eid):
    employee = Employee.query.filter_by(emp_id = eid).first()
    emp_skill = Emp_skill.query.filter_by(emp_id = eid).all()
    ls = [emp_skill[i].geteSkillId() for i in range(0,len(emp_skill))]
    eskill = Skill.query.filter(Skill.skill_id.in_(ls)).all()
    pr = employee.geteProjID()
    projt = Project.query.filter_by(proj_id = pr).first()
    emp_cert = Emp_cert.query.filter_by(emp_id=eid).all()
    lt = [emp_cert[i].geteCertId() for i in range(0, len(emp_cert))]
    ecert = Certification.query.filter(Certification.cert_id.in_(lt)).all()
    return render_template('emp_skill.html', employee = employee, emp_skill = emp_skill,eskill = eskill, projt = projt,ecert = ecert)
