import wtforms
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class TrackForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    image = wtforms.StringField('image')