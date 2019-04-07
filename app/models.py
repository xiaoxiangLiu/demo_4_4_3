from app import app
from app import db



class User(db.Model):
    """
    user 表
    """
    __tablename__ = "user"
    user_id = db.Column(db.String(64), primary_key=True, unique=True, index=True)
    user_password = db.Column(db.String(64), nullable=True)
    user_name = db.Column(db.String(64), nullable=True)
    user_phone = db.Column(db.Integer(), nullable=True)
    user_status = db.Column(db.Integer, nullable=True)
    user_create_tiem = db.Column(db.DateTime, index=True)
    user_update_time = db.Column(db.DateTime, index=True)
