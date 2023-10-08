# Standard library imports

# Remote library imports
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt

# Local imports

# Instantiate app, set attributes
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

app.secret_key = b'\xc5\xd0\xcbS\x82,\x07\xbf\xf4|\xad\xc4\x15\x84\xf0F'

# Define metadata, instantiate db
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)
app.app_context().push()

db.init_app(app)
# added .init_app
migrate = Migrate(app, db)


# Instantiate REST API
api = Api(app)

#Instantiate Bcrypt
bcrypt = Bcrypt(app)


# Instantiate CORS
CORS(app)
