from datetime import datetime
from .app import db 
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __table_name__= "user"
    id = db.Column(db.Integer ,primary_key=True,unique=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))
    photo_picture = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True),default=datetime.now)
    last_update = db.Column(db.DateTime(timezone=True), default=datetime.now,onupdate=datetime.now)
    is_admin = db.Column(db.Boolean,default=False)

    def __repr__(self):
        return str(self.id)
    def serialize(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
