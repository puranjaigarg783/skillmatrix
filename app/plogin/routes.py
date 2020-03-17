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
from app.plogin.forms import Lr_edit_form
from app.plogin.forms import Sr_edit_form
from app.plogin.forms import Skill_search_form
from app.plogin.forms import Loc_search_form
from sqlalchemy import func
from sqlalchemy.sql import label


import pprint

from flask import render_template, redirect, url_for

@pdash.route('/pm/project/<pid>', methods = ['GET','POST'])
def pm_pdetails(pid):
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
    return render_template('pm_proj_skill.html', proj_skill=proj_skill, project = project, pskill = pskill, empl = empl)

@pdash.route('/pm/projects/employee/<eid>', methods = ['GET','POST'])
def pm_edetails(eid):
    lr_edit_form = Lr_edit_form()
    location = Location.query.all()
    employee = Employee.query.filter_by(emp_id = eid).first()
    emp_skill = Emp_skill.query.filter_by(emp_id = eid).all()
    lr_edit_form.skill_select.choices = [(emp_skill[i].geteSkillId(),emp_skill[i].geteSkillId()) for i in range(0,len(emp_skill))]

    # print(lr_edit_form.skill_select.choices)
    if request.method == 'POST':
        print('aaaa')
        new_emp_skill = Emp_skill.query.filter_by(emp_id=eid).filter_by(skill_id=lr_edit_form.skill_select.data).first()
        new_lr_edit_form = Lr_edit_form(obj=new_emp_skill)
        new_emp_skill.proj_lead_rating = new_lr_edit_form.lead_rating.data
        print(new_emp_skill.proj_lead_rating)
        db.session.add(new_emp_skill)
        db.session.commit()
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
    return render_template('pm_emp_skills.html', employee = employee, emp_skill = emp_skill,eskill = eskill, projt = projt,ecert = ecert, avgskill = avgskill, Project = Project, location = location, lr_edit_form = lr_edit_form)

@pdash.route('/pm/projects/search/employee/<eid>', methods = ['GET','POST'])
def pm_srch_edetails(eid):
    lr_edit_form = Lr_edit_form()
    location = Location.query.all()
    employee = Employee.query.filter_by(emp_id = eid).first()
    emp_skill = Emp_skill.query.filter_by(emp_id = eid).all()
    lr_edit_form.skill_select.choices = [(emp_skill[i].geteSkillId(),emp_skill[i].geteSkillId()) for i in range(0,len(emp_skill))]

    # print(lr_edit_form.skill_select.choices)
    if request.method == 'POST':
        print('aaaa')
        new_emp_skill = Emp_skill.query.filter_by(emp_id=eid).filter_by(skill_id=lr_edit_form.skill_select.data).first()
        new_lr_edit_form = Lr_edit_form(obj=new_emp_skill)
        new_emp_skill.proj_lead_rating = new_lr_edit_form.lead_rating.data
        print(new_emp_skill.proj_lead_rating)
        db.session.add(new_emp_skill)
        db.session.commit()
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
    return render_template('pm_srch_emp_skills.html', employee = employee, emp_skill = emp_skill,eskill = eskill, projt = projt,ecert = ecert, avgskill = avgskill, Project = Project, location = location, lr_edit_form = lr_edit_form)


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


@pdash.route('/emp/employee/<eid>', methods = ['GET','POST'])
def emp_edetails(eid):
    sr_edit_form = Sr_edit_form()
    location = Location.query.all()
    employee = Employee.query.filter_by(emp_id = eid).first()
    emp_skill = Emp_skill.query.filter_by(emp_id = eid).all()
    sr_edit_form.skill_select.choices = [(emp_skill[i].geteSkillId(),emp_skill[i].geteSkillId()) for i in range(0,len(emp_skill))]

    # print(lr_edit_form.skill_select.choices)
    if request.method == 'POST':
        new_emp_skill = Emp_skill.query.filter_by(emp_id=eid).filter_by(skill_id=sr_edit_form.skill_select.data).first()
        new_sr_edit_form = Sr_edit_form(obj=new_emp_skill)
        new_emp_skill.self_eval_rating = new_sr_edit_form.self_rating.data
        db.session.add(new_emp_skill)
        db.session.commit()
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
    return render_template('emp_emp_skills.html', employee = employee, emp_skill = emp_skill,eskill = eskill, projt = projt,ecert = ecert, avgskill = avgskill, Project = Project, location = location, sr_edit_form = sr_edit_form)

@pdash.route('/emp/project/<pid>', methods = ['GET','POST'])
def emp_pdetails(pid):
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
    return render_template('emp_proj_skill.html', proj_skill=proj_skill, project = project, pskill = pskill, empl = empl)


@pdash.route('/employee/<eid>', methods = ['GET','POST'])
def edetails(eid):
    lr_edit_form = Lr_edit_form()
    location = Location.query.all()
    employee = Employee.query.filter_by(emp_id = eid).first()
    emp_skill = Emp_skill.query.filter_by(emp_id = eid).all()
    lr_edit_form.skill_select.choices = [(emp_skill[i].geteSkillId(),emp_skill[i].geteSkillId()) for i in range(0,len(emp_skill))]

    # print(lr_edit_form.skill_select.choices)
    if request.method == 'POST':
        print('aaaa')
        new_emp_skill = Emp_skill.query.filter_by(emp_id=eid).filter_by(skill_id=lr_edit_form.skill_select.data).first()
        new_lr_edit_form = Lr_edit_form(obj=new_emp_skill)
        new_emp_skill.proj_lead_rating = new_lr_edit_form.lead_rating.data
        print(new_emp_skill.proj_lead_rating)
        db.session.add(new_emp_skill)
        db.session.commit()
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
    return render_template('emp_skills.html', employee = employee, emp_skill = emp_skill,eskill = eskill, projt = projt,ecert = ecert, avgskill = avgskill, Project = Project, location = location, lr_edit_form = lr_edit_form)



@pdash.route('/emp/allprojects')
def emp_allproj():


    project = Project.query.all()
    proj_skill = Proj_skill.query.all()
    skill = Skill.query.all()
    return render_template('emp_all_proj.html', project = project, proj_skill = proj_skill, skill = skill)


@pdash.route('/allprojects')
def allproj():


    project = Project.query.all()
    proj_skill = Proj_skill.query.all()
    skill = Skill.query.all()
    return render_template('all_proj.html', project = project, proj_skill = proj_skill, skill = skill)

@pdash.route('/auth/skill', methods = ['GET','POST'])
def auth_sdetails():

    skill_search_form = Skill_search_form()
    skill_search_form.skill_select.choices = [(skill.skill_id, skill.skill_name) for skill in Skill.query.all()]
    skill = None
    proj_skill = None
    emp_skill = None
    emp_avgskill = None
    proj_prsent_avgskill = None
    proj_rated_avgskill = None
    project = None
    new_proj_skill = None
    graph_emp_skill = None
    graph_employee = None
    if request.method == 'POST':
        skill = Skill.query.filter_by(skill_id = skill_search_form.skill_select.data).all()
        new_proj_skill = Proj_skill.query.filter_by(skill_id = skill_search_form.skill_select.data).all()
        ls = [new_proj_skill[i].getProjectId() for i in range(0,len(new_proj_skill))]
        project = Project.query.filter(Project.proj_id.in_(ls)).all()
        proj_skill = db.session.query(Proj_skill.skill_id,label('ptotal',func.count(Proj_skill.proj_id))).group_by(Proj_skill.skill_id).all()
        emp_skill = db.session.query(Emp_skill.skill_id, label('etotal',func.count(Emp_skill.emp_id))).group_by(Emp_skill.skill_id).all()
        emp_avgskill = db.session.query(Emp_skill.skill_id,label('askill',func.avg(Emp_skill.final_rating))).group_by(Emp_skill.skill_id).all()
        proj_prsent_avgskill = db.session.query(Proj_skill.skill_id,label('proj_prsent_avgskill',func.avg(Proj_skill.proj_prsent_skill_rating))).group_by(Proj_skill.skill_id).all()
        proj_rated_avgskill = db.session.query(Proj_skill.skill_id,label('proj_rated_avgskill',func.avg(Proj_skill.proj_rated_rating))).group_by(Proj_skill.skill_id).all()
        graph_emp_skill = Emp_skill.query.filter_by(skill_id = skill_search_form.skill_select.data).all()
        lr = [graph_emp_skill[i].getEmpId() for i in range(0,len(graph_emp_skill))]
        graph_employee = Employee.query.filter(Employee.emp_id.in_(lr)).all()
    return render_template('auth_skill_dash.html', skill= skill,proj_skill=proj_skill,emp_skill=emp_skill,emp_avgskill=emp_avgskill, proj_prsent_avgskill=proj_prsent_avgskill,proj_rated_avgskill=proj_rated_avgskill, project = project, new_proj_skill = new_proj_skill, graph_emp_skill = graph_emp_skill, graph_employee = graph_employee, skill_search_form = skill_search_form)



@pdash.route('/skill/<sid>')
def sdetails(sid):
    skill = Skill.query.filter_by(skill_id = sid).all()
    new_proj_skill = Proj_skill.query.filter_by(skill_id = sid).all()
    ls = [new_proj_skill[i].getProjectId() for i in range(0,len(new_proj_skill))]
    # eskill = Skill.query.filter(Skill.skill_id.in_(ls)).all()
    project = Project.query.filter(Project.proj_id.in_(ls)).all()
    proj_skill = db.session.query(Proj_skill.skill_id,label('ptotal',func.count(Proj_skill.proj_id))).group_by(Proj_skill.skill_id).all()
    emp_skill = db.session.query(Emp_skill.skill_id, label('etotal',func.count(Emp_skill.emp_id))).group_by(Emp_skill.skill_id).all()
    emp_avgskill = db.session.query(Emp_skill.skill_id,label('askill',func.avg(Emp_skill.final_rating))).group_by(Emp_skill.skill_id).all()
    proj_prsent_avgskill = db.session.query(Proj_skill.skill_id,label('proj_prsent_avgskill',func.avg(Proj_skill.proj_prsent_skill_rating))).group_by(Proj_skill.skill_id).all()
    proj_rated_avgskill = db.session.query(Proj_skill.skill_id,label('proj_rated_avgskill',func.avg(Proj_skill.proj_rated_rating))).group_by(Proj_skill.skill_id).all()
    graph_emp_skill = Emp_skill.query.filter_by(skill_id = sid).all()
    lr = [graph_emp_skill[i].getEmpId() for i in range(0,len(graph_emp_skill))]
    graph_employee = Employee.query.filter(Employee.emp_id.in_(lr)).all()
    return render_template('skill_dash.html', skill= skill,proj_skill=proj_skill,emp_skill=emp_skill,emp_avgskill=emp_avgskill,proj_prsent_avgskill=proj_prsent_avgskill,proj_rated_avgskill=proj_rated_avgskill, project = project, new_proj_skill = new_proj_skill, graph_emp_skill = graph_emp_skill, graph_employee = graph_employee)


@pdash.route('/auth/location', methods=['GET', 'POST'])
def auth_ldetails():
    emp_skill = None
    skill = Skill.query.all()
    loc_search_form = Loc_search_form()
    loc_search_form.loc_select.choices = [(location.loc_id,location.loc_name) for location in Location.query.all()]
    if request.method == 'POST':
        location = Location.query.filter_by(loc_id=loc_search_form.loc_select.data).first()
        employee = Employee.query.filter_by(loc_id=loc_search_form.loc_select.data).all()
        ls = [employee[i].geteID() for i in range(0, len(employee))]
        emp_skill = db.session.query(Emp_skill.skill_id, label('no_emp', func.count(Emp_skill.emp_id))).filter(Emp_skill.emp_id.in_(ls)).group_by(Emp_skill.skill_id).all()
    return render_template('auth_loc_dash.html', emp_skill=emp_skill, skill=skill, loc_search_form = loc_search_form)


@pdash.route('/location/<lid>', methods = ['GET','POST'])
def ldetails(lid):

    skill = Skill.query.all()
    location = Location.query.filter_by(loc_id = lid).first()
    employee = Employee.query.filter_by(loc_id = lid).all()
    ls = [employee[i].geteID() for i in range(0,len(employee))]
    emp_skill = db.session.query(Emp_skill.skill_id,label('no_emp',func.count(Emp_skill.emp_id))).filter(Emp_skill.emp_id.in_(ls)).group_by(Emp_skill.skill_id).all()
    # for i in emp_skill:
    #     print(i.skill_id)
    #     print(i.no_emp)
    return render_template('loc_dash.html', emp_skill = emp_skill , skill = skill)

@pdash.route('/auth')
def auth():
    return render_template('auth_db.html')