from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PickupForm(FlaskForm):
    
    author = StringField('Pickup', validators = [Required()])
    pickup = TextAreaField('Pickup line', validators = [Required()])
    
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')