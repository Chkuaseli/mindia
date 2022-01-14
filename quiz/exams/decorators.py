from functools import wraps
from .models import Tests,Pictures,Subjects,MainLogin
from flask import redirect,render_template,url_for
from flask_login import login_user,logout_user,login_required,current_user
from quiz import bcrypt
import functools

# დეკორატორი წვდომებისათვის ორი როლისთვის ადმინი და სტუდენტ["admin","student"]
def decorator_factory(user):
    # We're going to return this decorator
    def simple_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("dekoratorshia shemosuli")
            if user == 'admin':
                if current_user.is_authenticated and current_user.name:
                    print(current_user)
                    usr = MainLogin.query.filter_by(name=current_user.name).first()
                    if usr and usr.state == 'admin':
                        print("adminiaaaaaaaaaaa",current_user.name,usr)
                        return func(*args,**kwargs)
                    else:
                        return redirect(url_for('StudentLogin'))
                else:
                    return redirect(url_for('StudentLogin'))
            if user == 'student':
                print("Shemovida studentia")
                if current_user.is_authenticated:
                    print("val1")
                    stud = Tests.query.filter_by(code=current_user.code).first()
                    print(stud.state,current_user.code)
                    if stud and stud.state =='student':
                        print("val2")
                        print("studentiaaaaaaaaaaaaaaa",current_user.code)
                        return func(*args,**kwargs)
                    else:
                        return redirect(url_for("StudentLogin"))
            else:
                return redirect(url_for('StudentLogin'))

        return wrapper

    return simple_decorator