import os
from flask_login import LoginManager
from flask import Flask


basedir = os.path.abspath(os.path.dirname(__file__))
# image = os.path.join(basedir,'static/images')
app = Flask(__name__)
class Config:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/mindia'
    SQLALCHEMY_TRACK_MODIFICATIONS =False
    SECRET_KEY = 'mindiaaa' 
#     # photos 
    UPLOADED_PHOTOS_DEST = os.path.join(basedir,'static/images')
    DROPZONE_ALLOWED_FILE_TYPE = 'image/*'

    login_manager=LoginManager()
    login_manager.init_app(app)
    login_manager.login_view='customerLogin'
    login_manager.needs_refresh_message_category='danger'
    login_manager.login_message = u'Please login first'