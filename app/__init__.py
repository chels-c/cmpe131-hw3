from flask import Flask

myobj = Flask(__name__)
myobj.config.from_mapping(
	SECRET_KEY = 'HW3-HP-PAIN'
)
from app import routes
