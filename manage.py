from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

from app import create_app,db
from app.auth.v1.model.models import User,Genre 

app = create_app('development')
manager = Manager(app)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Genre = Genre)

if __name__ == '__main__':
    manager.run()