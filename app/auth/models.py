from app import db, bcrypt
from flask_login import UserMixin
from app import login_manager


class Emp_details(UserMixin, db.Model):
    __tablename__ = 'emp_details'

    emp_id = db.Column(db.Integer, primary_key=True)
    emp_password = db.Column(db.String(80), nullable=False)
    auth = db.Column(db.Integer)

    def __init__(self, emp_id, emp_password, auth):
        self.emp_id = emp_id
        self.emp_password = emp_password
        self.auth = auth

    def getemppw(self):
        return self.emp_password

    def getauth(self):
        return self.auth


@login_manager.user_loader
def load_user(emp_id):
    return Emp_details.query.get(int(emp_id))
