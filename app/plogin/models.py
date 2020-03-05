from app import db


class Project(db.Model):
    __tablename__ = 'project'

    proj_id = db.Column(db.Integer, primary_key=True)
    proj_name = db.Column(db.String(80), nullable=False)
    emp_id =  db.Column(db.Integer)

    def __init__(self, proj_id, proj_name, emp_id):
        self.proj_name = proj_name
        self.proj_id = proj_id
        self.emp_id = emp_id

    def getprojid(self):
        return self.proj_id
    # def __repr__(self):
    #     return 'The project id and name is {} and {} respectively'.format(self.proj_id,self.proj_name)

class Skill(db.Model):
    __tablename__ = 'skill'

    skill_id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(80), nullable=False)


    def __init__(self, skill_id, skill_name):
        self.skill_name = skill_name
        self.skill_id = skill_id
    #
    # def __repr__(self):
    #     return 'The project id and name is {} and {}'.format(self.skill_id,self.skill_name)
    #

class Proj_skill(db.Model):
    __tablename__ = 'proj_skill'

    proj_skill_id = db.Column(db.Integer, primary_key=True)
    proj_id = db.Column(db.Integer)
    proj_rated_rating = db.Column(db.Integer)
    proj_prsent_skill_rating = db.Column(db.Integer)
    skill_range = db.Column(db.String(80), nullable=False)

    skill_id = db.Column(db.Integer, db.ForeignKey('skill.skill_id'))


    def __init__(self, proj_id,skill_id,proj_rated_rating,proj_prsent_skill_rating,skill_range):
        self.proj_id = proj_id
        self.skill_id = skill_id
        self.proj_rated_rating = proj_rated_rating
        self.proj_prsent_skill_rating = proj_prsent_skill_rating
        self.skill_range = skill_range

    def getProjectId(self):
        return self.proj_id

    def getpSkillId(self):
        return self.skill_id

    def getProjectRating(self):
        return self.proj_prsent_skill_rating
    #
    # def __repr__(self):
    #     return 'The project id and name is {} and {}'.format(self.proj_id,self.skill_id)
    #

class Employee(db.Model):
    __tablename__ = 'employee'

    emp_id = db.Column(db.Integer, primary_key=True)
    emp_name = db.Column(db.String(80), nullable=False)
    emp_desg_id = db.Column(db.Integer)
    emp_role = db.Column(db.String(80), nullable=False)
    experience = db.Column(db.String(80), nullable=False)
    proj_id = db.Column(db.Integer, primary_key=True)


    def __init__(self, emp_id, emp_name, emp_desg_id, emp_role, experience,proj_id):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_desg_id = emp_desg_id
        self.emp_role = emp_role
        self.experience = experience
        self.proj_id = proj_id

    def geteProjID(self):
        return self.proj_id

    def geteID(self):
        return self.emp_id


class Emp_skill(db.Model):
    __tablename__ = 'emp_skill'

    emp_skill_id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer)
    skill_id = db.Column(db.Integer)
    skill_range = db.Column(db.Integer)
    proj_lead_rating = db.Column(db.Integer)
    self_eval_rating = db.Column(db.Integer)
    experience = db.Column(db.Float)
    final_rating = db.Column(db.Integer)


    def __init__(self, emp_skill_id, emp_id, skill_id, skill_range,proj_lead_rating,
                 self_eval_rating,experience, final_rating):
        self.emp_skill_id = emp_skill_id
        self.emp_id = emp_id
        self.skill_id = skill_id
        self.skill_range = skill_range
        self.proj_lead_rating = proj_lead_rating
        self.self_eval_rating = self_eval_rating
        self.experience = experience
        self.final_rating = final_rating


    def geteSkillId(self):
        return self.skill_id

class Certification(db.Model):
    __tablename__ = 'certification'

    cert_id = db.Column(db.Integer, primary_key=True)
    cert_name = db.Column(db.String(80), nullable=False)
    cert_link = db.Column(db.String(200), nullable=False)


    def __init__(self, cert_id, cert_name, cert_link):
        self.cert_name = cert_name
        self.cert_id = cert_id
        self.cert_link = cert_link

class Emp_cert(db.Model):
    __tablename__ = 'emp_cert'

    emp_cert_id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.String(80), nullable=False)
    cert_id = db.Column(db.String(200), nullable=False)


    def __init__(self, emp_cert_id, emp_id, cert_id):
        self.emp_cert_id = emp_cert_id
        self.cert_id = cert_id
        self.emp_id = emp_id


    def geteCertId(self):
        return self.cert_id

