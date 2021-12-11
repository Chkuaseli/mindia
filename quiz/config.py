import os

basedir = os.path.abspath(os.path.dirname(__file__))
# image = os.path.join(basedir,'static/images')
class Config:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:user13@localhost/mindia'
    SQLALCHEMY_TRACK_MODIFICATIONS =False
    SECRET_KEY = 'mindiaaa' 
#     # photos 
    UPLOADED_PHOTOS_DEST = os.path.join(basedir,'static/images')
#     DROPZONE_ALLOWED_FILE_TYPE = 'image/*'