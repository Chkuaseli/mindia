from typing import Sized
from quiz import app,db,photos,search,photos
from flask import redirect, render_template, url_for, flash, request,current_app,jsonify,session,make_response,request
import secrets,os
import pdfkit
from datetime import datetime
from .forms import PictureForm,SubjectForm,TestForm
from .models import Tests,Pictures,Subjects
from PIL import Image

@app.route('/',methods=['GET'])
def department():
    t = "make mindia websaite"
    return t

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn
  
@app.route('/add_test',methods=['POST','GET'])
def add_test():
    form = TestForm()
    print("testing ")
    print(form.validate_on_submit())
    print(form.errors)
    if form.validate_on_submit() and request.method =='POST':
        code = form.code.data
        name = form.name.data
        desc = form.desc.data
        if code != None and name != None:
            add_test = Tests(code = code,name=name,desc=desc)
            pic = request.files.getlist('file')
            if any(f for f in pic):
                for up in pic:
                    # images = photos.save(up,name = secrets.token_hex(10)+".") ამ შემთხვევაში ქართული დასახელების ფოტოები არ იტვირთება 
                    images = save_picture(up)
                    pics =  Pictures (pic = images) 
                    add_test.pic_id.append(pics) 
            db.session.add(add_test)
            db.session.commit()            
            flash(f'მონაცემები წარმატებით დაემატა','success')
        return redirect(url_for('add_test'))
    return render_template('card/add_tests.html',form = form )

@app.route('/update_test',methods=['POST','GET'])
def update_test():
    form = Tests()
    t = "make mindia websaite"
    return t