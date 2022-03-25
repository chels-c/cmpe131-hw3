from flask import Flask, url_for
global name
global city_names

myobj = Flask(__name__)

@myobj.route("/home")
def home():
	return """
	<html>
	<head>
	</head>
	<body>
		<h1>Welcome """  + name """ </h1>
		<a href="www.google.com">not google </a>
		<ul>
		{% for city in city_names %}
       			<li>city.name</li>
  		{% endfor %}
		</ul>
	</body>
	</html>"""
#myapp_obj.run()
