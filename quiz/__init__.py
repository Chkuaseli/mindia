from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .exams.models import db 
from .config import Config
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
from flask_msearch import Search

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


from quiz.exams import route