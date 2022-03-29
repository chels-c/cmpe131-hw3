from app import myobj
from flask import render_template, flash

name = ''
city_names = ["city1", "city2"]

@myobj.route('/')
def home():
	return render_template("home.html", name = name, city_names = city_names)
