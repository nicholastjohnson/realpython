# config.py

import os

# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
SECRET_KEY = 'my_precious'

# defines the full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database url
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH