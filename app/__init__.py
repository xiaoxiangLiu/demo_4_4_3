from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from setting import BaseSetting

app = Flask(__name__)


app.config.from_object(BaseSetting)


db = SQLAlchemy(app=app)

