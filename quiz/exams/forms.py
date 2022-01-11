from wtforms import Form,StringField, TextAreaField, SubmitField,validators,ValidationError,RadioField,IntegerField,SelectField
from flask_wtf.file import FileField,FileAllowed,FileField,FileRequired
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length,InputRequired
from .models import Tests

class PictureForm(FlaskForm):
    name = StringField('First Name: ',validators=[DataRequired(),Length(min=3, max=50, message='Name length must be between %(min)d and %(max)d characters') ])
    pic = FileField('Card image: ', validators=[FileAllowed(['jpg','png','jpeg','gif'],'Image only please'),FileRequired()])

class SubjectForm(FlaskForm):
    name = StringField('First Name: ',validators=[DataRequired(),Length(min=3, max=50, message='Name length must be between %(min)d and %(max)d characters') ])
    submit = SubmitField('add subjects')

class TestForm(FlaskForm):
    code = StringField('Code: ',validators=[DataRequired(),Length(min=3, max=10, message='Code length must be between %(min)d and %(max)d characters') ])
    name = StringField('Name: ',validators=[DataRequired(),Length(min=3, max=50, message='Name length must be between %(min)d and %(max)d characters') ])
    desc = TextAreaField('Description')
    submit = SubmitField('add test')

    def validate_code(self,code):
        if Tests.query.filter_by(code=code.data).first():
            raise ValidationError('This code alredy exist!')