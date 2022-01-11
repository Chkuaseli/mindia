from typing import Sized
from quiz import app,db,photos,search,photos,bcrypt
from flask import redirect, render_template, url_for, flash, request,current_app,jsonify,session,make_response,request
import secrets,os
# import pdfkit
from datetime import datetime
from .forms import PictureForm,SubjectForm,TestForm,LoginForm,AdminLoginForm
from .models import Tests,Pictures,Subjects,MainLogin
from PIL import Image
from flask_login import login_user,logout_user,login_required,current_user

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# აქ ვინახავ სურათს სტატიკ ფოლდერში
def save_picture(form_picture):
    random_hex = form_picture.filename + secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_fn)
    # თუ გვინდა სურათების დაპატარავება 
    # output_size = (125, 125)
    # i = Image.open(form_picture) 
    # i.thumbnail(output_size)
    form_picture.save(picture_path)
    return picture_fn


@app.route('/student/login',methods=['GET','POST'])
def StudentLogin():
    form = LoginForm()
    if form.validate_on_submit():
        user=Tests.query.filter_by(code=form.login.data).first()
        if user:
            login_user(user)
            flash(f'თქვენ წარმატებით შეხვედით თქვენს ოთახში','success')
            next = request.args.get('next')
            return redirect(next or url_for('StudentHome'))
        flash(f'დაფიქსირდა შესვლის არასწორი მცდელობა','danger')
        return redirect(url_for("customerLogin"))
    return render_template('card/student_login.html',form=form)

@login_required
@app.route('/student/home',methods=['GET','POST'])
def StudentHome():
    z= current_user.id
    print("username",current_user.code,Pictures.query.filter_by(test_id = z).first().pic)
    return render_template('card/student_home.html')

@login_required
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

@app.route('/admin/tests',methods=['POST','GET'])
def tests():
    tests = Tests.query.all()

    # for pic in tests:
    #     pic.

    return render_template('card/tests.html',tests=tests)

@app.route('/update_test',methods=['POST','GET'])
def update_test():
    form = Tests()
    t = "make mindia websaite"
    return t

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('/'))


@app.route("/admin/login", methods=['GET', 'POST'])
def login():
    # add_admin = MainLogin(name = 'admin',pwd = bcrypt.generate_password_hash('12345').decode('utf-8'))
    # db.session.add(add_admin)
    # db.session.commit()
    # return "daemata warmatebit admini"
    if current_user.is_authenticated and current_user.state =='admin':
        return redirect(url_for('AdminHome'))
    form = AdminLoginForm()
    if form.validate_on_submit():
        user = MainLogin.query.filter_by(name=form.name.data).first()
        if user and bcrypt.check_password_hash(user.pwd, form.pwd.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('AdminHome'))
        else:
            flash('Login Unsuccessful. Please check name and password', 'danger')
    return render_template('card/admin_login.html', title='Login', form=form)


@app.route("/admin/home", methods=['GET', 'POST'])
def AdminHome():
    data = 'admin user'+ '  ' + current_user.name
    return data

@app.route("/")
def main():
    return render_template('cards/main_page.html')