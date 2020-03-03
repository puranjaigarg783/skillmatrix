from flask import render_template, redirect, url_for, request, flash
from app import db
from app.auth.forms import Login_form
from app.auth.models import Emp_details
from app.plogin.models import Project
from app.auth import authn
from app.plogin import pdash
from flask_login import login_user, logout_user


@authn.route('/', methods = ['GET','POST'])
def log_in():
    login_form = Login_form()
    emp_details = Emp_details.query.filter_by(emp_id = login_form.log_id.data).first()
    if request.method == 'POST':
        if not emp_details:
            print('no')
            return redirect(url_for('authn.log_in'))
        return redirect(url_for('pdash.edetails', eid=login_form.log_id.data))
    return render_template('logging.html', login_form = login_form)







