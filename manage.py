import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from quiz.exams import app
from quiz.database_conf import db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()