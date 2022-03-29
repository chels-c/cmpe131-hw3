from app import myobj
from flask import render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

name = 'chels'
city_names = ["city1", "city2"]

@myobj.route('/', methods = ['GET', 'POST'])
def home():
	form = SubmitForm()
	if form.validate_on_submit():
		flash(form.CityName.data)
	return render_template("home.html", name = name,city_names = city_names, form=form)
"""
@myobj.route('/submit', methods = ['GET', 'POST'])

def submit():
	form = SubmitForm()
	if form.validate_on_submit():
		flash('submitted'.format(form.CityName.data))
		return redirect('/')
	return render_template('home.html', title = 'submit', form = form)
"""
class SubmitForm(FlaskForm):
	CityName = StringField('City Name', validators = [DataRequired()]
	submit = SubmitField('Submit')
