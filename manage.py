from app import create_app,db
from app.models import User, Pitch, Comment
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

# creating app instance
app = create_app('production')

# create manager instance
manager = Manager(app)

# create a migrate instance
migrate = Migrate(app,db)

manager.add_command('server', Server)
manager.add_command('db',MigrateCommand)