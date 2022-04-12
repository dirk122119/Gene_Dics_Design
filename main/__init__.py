from flask import Flask,redirect,url_for
from config import Config

app=Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def hello():
    return redirect(url_for('Dashboard.home'))

from main.dashboard.view import Dashboard
from main.camera.view import Camera

app.register_blueprint(Dashboard,url_prefix='/dashboard')
app.register_blueprint(Camera,url_prefix='/camera')