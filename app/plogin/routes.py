from app.plogin import pdash
from flask import render_template, redirect, url_for, request
from app import db
from app.plogin.models import Skill
from app.plogin.models import Project
from app.plogin.models import Proj_skill
from app.plogin.models import Emp_skill
from app.plogin.models import Employee
from app.plogin.models import Certification
from app.plogin.models import Emp_cert
from sqlalchemy import func
from sqlalchemy.sql import label


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
    avgskill = db.session.query(Emp_skill.skill_id,label('askill',func.avg(Emp_skill.final_rating))).group_by(Emp_skill.skill_id).all()
    return render_template('emp_skill.html', employee = employee, emp_skill = emp_skill,eskill = eskill, projt = projt,ecert = ecert, avgskill = avgskill, Project = Project)


@pdash.route('/allprojects')
def allproj():
    project = Project.query.all()
    proj_skill = Proj_skill.query.all()
    skill = Skill.query.all()
    return render_template('all_proj.html', project = project, proj_skill = proj_skill, skill = skill)

@pdash.route('/skill/<sid>')
def sdetails(sid):
    new_proj_skill = Proj_skill.query.filter_by(skill_id = sid).all()
    ls = [new_proj_skill[i].getProjectId() for i in range(0,len(new_proj_skill))]
    # eskill = Skill.query.filter(Skill.skill_id.in_(ls)).all()
    project = Project.query.filter(Project.proj_id.in_(ls)).all()
    skill = Skill.query.filter_by(skill_id = sid).all()
    proj_skill = db.session.query(Proj_skill.skill_id,label('ptotal',func.count(Proj_skill.proj_id))).group_by(Proj_skill.skill_id).all()
    emp_skill = db.session.query(Emp_skill.skill_id, label('etotal',func.count(Emp_skill.emp_id))).group_by(Emp_skill.skill_id).all()
    emp_avgskill = db.session.query(Emp_skill.skill_id,label('askill',func.avg(Emp_skill.final_rating))).group_by(Emp_skill.skill_id).all()
    proj_prsent_avgskill = db.session.query(Proj_skill.skill_id,label('proj_prsent_avgskill',func.avg(Proj_skill.proj_prsent_skill_rating))).group_by(Proj_skill.skill_id).all()
    proj_rated_avgskill = db.session.query(Proj_skill.skill_id,label('proj_rated_avgskill',func.avg(Proj_skill.proj_rated_rating))).group_by(Proj_skill.skill_id).all()
    return render_template('skill_dash.html', skill= skill,proj_skill=proj_skill,emp_skill=emp_skill,emp_avgskill=emp_avgskill,proj_prsent_avgskill=proj_prsent_avgskill,proj_rated_avgskill=proj_rated_avgskill, project = project, new_proj_skill = new_proj_skill)

