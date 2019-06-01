from flask import Blueprint, render_template, abort
import math
import rasterio
import matplotlib.pyplot as plt

class MyRoute:

	page = Blueprint('myroute_page', __name__, template_folder='templates')
	base = '/myroute'

	@page.route("/")
	def index():
		image_file = "./data/LC80320422017001LGN00_B10.tif"
		sat_data = rasterio.open(image_file)
		b, g, r, n = sat_data.read()
		fig = plt.imshow(b)
		plt.show()
		return "Index"

	@page.route(f'{base}/')
	def home():
		return 'my route home'

	@page.route(f'{base}/login')
	def login():
		return 'my route login'