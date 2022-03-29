from app import myobj
from flask import render_template, flash

name = ''
city_names = ["city1", "city2"]

@myobj.route('/')
def home():
	return return_template(home.html, name = name)
