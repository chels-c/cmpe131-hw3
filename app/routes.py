from app import myobj
from flask import render_template, flash

global name
global city_names

@myobj.route('/')
def home():
	return return_template(home.html, name = name)
