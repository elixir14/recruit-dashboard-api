from rest.app import db


class Candidate(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(1000), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(100), unique=False)
    last_name = db.Column(db.String(100), unique=False)
    contact_no = db.Column(db.String(100), unique=False)
    gid = db.Column(db.Integer)
    quids = db.Column(db.Text)
    su = db.Column(db.Integer, default=0)
    subscription_expired = db.Column(db.Integer,default=0)
    verify_code = db.Column(db.Integer,default=0)
    dob = db.Column(db.DateTime)
    city = db.Column(db.String(128),default='')
    country = db.Column(db.String(128),default='')
    state = db.Column(db.String(128),default='')
    job_location = db.Column(db.String(128),default='')
    post = db.Column(db.String(128),default='')
    attachment = db.Column(db.String(128),default='')
    education = db.Column(db.String(128),default='')
    experienced =db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime)
    udate = db.Column(db.DateTime)
    mail_sent =db.Column(db.Integer, default=0)
    favorite =db.Column(db.Integer, default=0)
    note = db.Column(db.Text)
    

     


