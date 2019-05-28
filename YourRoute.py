from flask import Blueprint, render_template, abort

class YourRoute:

	page = Blueprint('yourroute_page', __name__, template_folder='templates')
	base = '/yourroute'

	@page.route(f'{base}/')
	def home():
		return 'your route home'

	@page.route(f'{base}/login')
	def login():
		return 'your route login'