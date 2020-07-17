from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# app.config.from_object(os.environ['APP_SETTINGS'])
from rest.app import app, db
from apps.users.models import User
from apps.candidate.models import Candidate
from apps.tags.models import Tag

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
