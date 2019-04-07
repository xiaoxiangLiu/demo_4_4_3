from app.models import User
from app import db



user = User(user_id="123", user_password="123", user_name="123", user_phone="132", user_status=0,
            user_update_time="2019-01-01", user_create_tiem="2019-01-01")
db.session.add(user)

db.session.commit()