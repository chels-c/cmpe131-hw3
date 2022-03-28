from app import myobj
from flask import render_templates, flash

global name
global city_names

@myobj.route('/')
def home():
	return return_templates(home.html, name = name)
