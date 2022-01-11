from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .exams import db 
from .config import Config
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
from flask_msearch import Search
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config.from_object(Config)

# Setup Flask-SQLAlchemy
db.init_app(app)

#serch
search = Search()
search.init_app(app)

# migrate
Migrate(app, db)

#flask uploads
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

bcrypt = Bcrypt(app)


login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='customerLogin'
login_manager.needs_refresh_message_category='danger'
login_manager.login_message = u'Please login first'

from quiz.exams import route