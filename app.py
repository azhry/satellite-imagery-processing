from flask import Flask, render_template
from MyRoute import MyRoute
from YourRoute import YourRoute

app = Flask(__name__)
app.register_blueprint(MyRoute.page)
app.register_blueprint(YourRoute.page)