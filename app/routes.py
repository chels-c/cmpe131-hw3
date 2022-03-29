from app import myobj
from flask import render_template, flash

name = 'chels'
city_names = ["city1", "city2"]

@myobj.route('/')
def home():
	return render_template("home.html", name = name,city_names = city_names)

@myobj.route('', methods = ['GET', 'POST'])
def submit():
	form = SubmitForm()
	if form.validate_on_submit():
		flash('submitted'.format(form.CityName.data))
		return redirect('/')
	return render_template('home.html', title = 'submit', form = form)
