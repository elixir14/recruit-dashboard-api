from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


from apps.users import models
from apps.tags import models
from apps.candidate import models

#app.config.from_object(os.environ['APP_SETTINGS'])
from rest.app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
