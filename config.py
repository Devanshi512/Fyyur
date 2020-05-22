import os
SECRET_KEY = os.urandom(32)

# Grab the folder/directory where the script is running
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable the debug mode
DEBUG = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/fyyur'
