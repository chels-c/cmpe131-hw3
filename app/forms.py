from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SubmitForm(FlaskForm):
	CityName = StringField('City Name', validators = [DataRequired()]
	submit = SubmitField('Submit')
