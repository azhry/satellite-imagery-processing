from flask import Blueprint, render_template, abort

class MyRoute:

	page = Blueprint('myroute_page', __name__, template_folder='templates')
	base = '/myroute'

	@page.route(f'{base}/')
	def home():
		return 'my route home'

	@page.route(f'{base}/login')
	def login():
		return 'my route login'