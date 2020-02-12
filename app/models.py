from flask_login import UserMixin

class Pickup:
      
    def __init__(self, pickup_id, author, pickupLine):
        
        self.pickup_id = pickup_id
        self.author = author
        self.pickupLine = pickupLine


    __tablename__ = 'users'

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
