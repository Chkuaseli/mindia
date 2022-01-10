from quiz.database_conf import db
from datetime import datetime
from datetime import datetime,timezone

class Pictures(db.Model):
    id = db.Column(db.Integer(), primary_key=True,nullable = False)
    pic=db.Column(db.String(180) ,unique = True,nullable =False)
    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'))


class Tests(db.Model):
  _searchable_=['name','code']
  id = db.Column(db.Integer(), primary_key=True,nullable = False)
  code =  db.Column(db.String(80),unique = True, nullable=False)
  name = db.Column(db.String(80),unique = False, nullable=False)
  desc = db.Column(db.String(180) ,unique = False,nullable =False)
  date_crated = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
  pic_id = db.relationship('Pictures', backref='tests',cascade="all,delete")

class Subjects(db.Model):
  id = db.Column(db.Integer(), primary_key=True,nullable = False)
  name = db.Column(db.String(80),unique = False, nullable=False)
