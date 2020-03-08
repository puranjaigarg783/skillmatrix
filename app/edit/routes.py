from app import db
from app.edit import edit
from app.edit.forms import Lredit_form
from app.edit.forms import Sredit_form

from app.plogin.models import Emp_skill
from app.plogin import pdash
from flask import render_template, redirect, url_for, request, flash

@edit.route('/lredit/<eid>/<sid>', methods = ['GET','POST'])
def lrating(eid,sid):
    emp_skill = Emp_skill.query.filter_by(emp_id = eid).filter_by(skill_id = sid).first()
    lredit_form = Lredit_form(obj = emp_skill)
    if request.method == 'POST':
        emp_skill.proj_lead_rating = lredit_form.lead_rating.data
        db.session.add(emp_skill)
        db.session.commit()
        return redirect(url_for('pdash.edetails', eid = eid))
    return render_template('lr_edit.html',emp_skill = emp_skill, lredit_form = lredit_form)

@edit.route('/sedit/<eeid>/<ssid>', methods = ['GET','POST'])
def srating(eeid,ssid):
    emp_skill = Emp_skill.query.filter_by(emp_id = eeid).filter_by(skill_id = ssid).first()
    sredit_form = Sredit_form(obj = emp_skill)
    if request.method == 'POST':
        emp_skill.self_eval_rating = sredit_form.self_rating.data
        db.session.add(emp_skill)
        db.session.commit()
        return redirect(url_for('pdash.edetails', eid = eeid))
    return render_template('sredit.html',emp_skill = emp_skill, sredit_form = sredit_form)