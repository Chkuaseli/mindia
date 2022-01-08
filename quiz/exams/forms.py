from wtforms import Form,StringField, TextAreaField, SubmitField,validators,ValidationError,RadioField,IntegerField,SelectField
from flask_wtf.file import FileField,FileAllowed,FileField,FileRequired
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length,InputRequired

class Pictures(FlaskForm):
    name = StringField('First Name: ',validators=[DataRequired(),Length(min=3, max=50, message='Name length must be between %(min)d and %(max)d characters') ])
    pic = FileField('Card image: ', validators=[FileAllowed(['jpg','png','jpeg','gif'],'Image only please'),FileRequired()])

class Subjects(FlaskForm):
    name = StringField('First Name: ',validators=[DataRequired(),Length(min=3, max=50, message='Name length must be between %(min)d and %(max)d characters') ])
    submit=SubmitField('add subjects')

class Tests(FlaskForm):
    code = StringField('Code: ',validators=[DataRequired(),Length(min=3, max=10, message='Code length must be between %(min)d and %(max)d characters') ])
    name = StringField('First Name: ',validators=[DataRequired(),Length(min=3, max=50, message='Name length must be between %(min)d and %(max)d characters') ])
    desc = TextAreaField('Description')
    submit=SubmitField('add test')

    