from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('YourNal')
db = SQLAlchemy(app)