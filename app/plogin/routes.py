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
from app.plogin.models import Location
from sqlalchemy import func
from sqlalchemy.sql import label


import pprint

from flask import render_template, redirect, url_for

@pdash.route('/project/<pid>', methods = ['GET','POST'])
def pdetails(pid):
    empl = Employee.query.filter_by(proj_id = pid ).all()
    proj_skill = Proj_skill.query.filter_by(proj_id =  pid).all()
    lr = [empl[i].geteID() for i in range(0,len(empl))]
    avg_emp_skill = db.session.query(Emp_skill.skill_id,label('avg_emp_skill',func.avg(Emp_skill.final_rating))).filter(Emp_skill.emp_id.in_(lr)).group_by(Emp_skill.skill_id).all()
    for i in proj_skill:
        for j in avg_emp_skill:
            if i.skill_id == j.skill_id:
                i.proj_prsent_skill_rating = j.avg_emp_skill
                db.session.add(i)
                db.session.commit()
    project = Project.query.filter_by(proj_id =  pid ).first()
    ls = [proj_skill[i].getpSkillId() for i in range(0,len(proj_skill))]
    pskill = Skill.query.filter(Skill.skill_id.in_(ls)).all()
    return render_template('proj_skill.html', proj_skill=proj_skill, project = project, pskill = pskill, empl = empl)

@pdash.route('/employee/<eid>', methods = ['GET','POST'])
def edetails(eid):
    location = Location.query.all()
    employee = Employee.query.filter_by(emp_id = eid).first()
    emp_skill = Emp_skill.query.filter_by(emp_id = eid).all()

    for i in emp_skill:
        i.final_rating = i.proj_lead_rating + i.self_eval_rating + i.experience
        db.session.add(i)
        db.session.commit()
    ls = [emp_skill[i].geteSkillId() for i in range(0,len(emp_skill))]
    eskill = Skill.query.filter(Skill.skill_id.in_(ls)).all()
    pr = employee.geteProjID()
    projt = Project.query.filter_by(proj_id = pr).first()
    emp_cert = Emp_cert.query.filter_by(emp_id=eid).all()
    lt = [emp_cert[i].geteCertId() for i in range(0, len(emp_cert))]
    ecert = Certification.query.filter(Certification.cert_id.in_(lt)).all()
    avgskill = db.session.query(Emp_skill.skill_id,label('askill',func.avg(Emp_skill.final_rating))).group_by(Emp_skill.skill_id).all()
    return render_template('new3_emp.html', employee = employee, emp_skill = emp_skill,eskill = eskill, projt = projt,ecert = ecert, avgskill = avgskill, Project = Project, location = location)


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
    graph_emp_skill = Emp_skill.query.filter_by(skill_id = sid).all()
    lr = [graph_emp_skill[i].getEmpId() for i in range(0,len(graph_emp_skill))]
    graph_employee = Employee.query.filter(Employee.emp_id.in_(lr)).all()
    return render_template('skill_dash.html', skill= skill,proj_skill=proj_skill,emp_skill=emp_skill,emp_avgskill=emp_avgskill,proj_prsent_avgskill=proj_prsent_avgskill,proj_rated_avgskill=proj_rated_avgskill, project = project, new_proj_skill = new_proj_skill, graph_emp_skill = graph_emp_skill, graph_employee = graph_employee)

