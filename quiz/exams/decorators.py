from functools import wraps
from .models import Tests,Pictures,Subjects,MainLogin
from flask import redirect,render_template,url_for
from flask_login import login_user,logout_user,login_required,current_user
from quiz import bcrypt
import functools

