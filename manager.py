from app import *
from app.models import *
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


manager = Manager(app=app)

migrate = Migrate(app=app, db=db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
