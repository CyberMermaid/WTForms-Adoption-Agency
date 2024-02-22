from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class AddPetForm(FlaskForm):
    """Form for adding pets."""
    name = StringField("Pet Name")
    species = StringField("Species")
    photo_URL = StringField("Enter Photo URL")
    age = IntegerField("Enter age")
    notes = StringField("Enter notes")