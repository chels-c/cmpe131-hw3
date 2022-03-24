from flask import flask, url_for
global name
global city_names

myobj = Flask(_name_)

@myobj.route("/home")
def home():
	'''
	<html>
	<head>
	</head>
	<body>
		<h1>Welcome '''  + name '''</h1>
		<a href="www.google.com">not google </a>
		<ul>
		{% for city.name in city_names %}
       			<li>city</li>
  		{% endfor %}
		</ul>
	</body>
	</html>
	'''
#myapp_obj.run()
