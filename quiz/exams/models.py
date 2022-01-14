from quiz.exams import db
from datetime import datetime
from datetime import datetime,timezone
from flask_login import UserMixin
from quiz import login_manager

@login_manager.user_loader
def user_loader(user_id):
    return Tests.query.get(user_id) or MainLogin.query.get(user_id)

class Pictures(db.Model):
    id = db.Column(db.Integer(), primary_key=True,nullable = False)
    pic=db.Column(db.String(180) ,unique = True,nullable =False)
    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'))

class Tests(db.Model,UserMixin):
  _searchable_=['name','code']
  id = db.Column(db.Integer(), primary_key=True,nullable = False)
  code =  db.Column(db.String(80),unique = True, nullable=False)
  name = db.Column(db.String(80),unique = False, nullable=False)
  desc = db.Column(db.String(180) ,unique = False,nullable =False)
  state = db.Column(db.String(100) ,nullable =False,default = 'student')
  date_crated = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
  #relation onetomany
  pic_id = db.relationship('Pictures', backref='tests',cascade="all,delete")
  

class Subjects(db.Model):
  id = db.Column(db.Integer(), primary_key=True,nullable = False)
  name = db.Column(db.String(80),unique = False, nullable=False)

class MainLogin(db.Model,UserMixin):
  id = db.Column(db.Integer(), primary_key=True,nullable = False)
  name = db.Column(db.String(180) ,unique = True,nullable =False)  
  pwd = db.Column(db.String(180) ,unique = False,nullable =False)
  state = db.Column(db.String(100) ,nullable =False,default = 'admin')