from quiz import app,db,photos,search
from flask import redirect, render_template, url_for, flash, request,current_app,jsonify,session,make_response,request
import secrets,os
import pdfkit
from datetime import datetime
from .forms import Pictures,Subjects,Tests
from .models import Tests,Pictures,Subjects

@app.route('/',methods=['GET'])
def department():
    t = "make mindia websaite"
    return t

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
  
@app.route('/add_test',methods=['POST','GET'])
def add_test():
    form = Tests()
    if request.method =='POST':
        code = form.code.data
        name = form.name.data
        desc = form.desc.data
        if code != None and name != None: 
            add_test = Tests(code = code,name=name,desc=desc)
            db.session.add(add_test)
            flash(f'the {code} with name {name} has bin adedd to your database','success')
            db.session.commit()
        return form

    return render_template('cards/add_tests.html',form = form , title = 'add test')

@app.route('/update_test',methods=['POST','GET'])
def update_test():
    form = Tests()
    t = "make mindia websaite"
    return t