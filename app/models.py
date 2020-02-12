from flask_login import UserMixin
from . import login_manager
from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class Pickup:
      
    def __init__(self, pickup_id, author, pickupLine):
        
        self.pickup_id = pickup_id
        self.author = author
        self.pickupLine = pickupLine



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    # pitches = db.relationship('Pitch', backref = 'author', lazy=True

    def get_reset_token(self, expires_sec=1800):
        s= Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'{self.username}'
        
    @staticmethod
    def verify_reset_token(token):
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow )
    content = db.Column(db.Text(1600), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    category = db.Column(db.String(255), nullable= False)
    def __repr__(self):
        return f"Pitch('{self.title}','{self.date_posted}')"