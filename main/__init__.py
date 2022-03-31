from flask import Flask
from config import Config

app=Flask(__name__)
app.config.from_object(Config)

from main.dashboard.view import Dashboard
from main.camera.view import Camera

app.register_blueprint(Dashboard,url_prefix='/dashboard')
app.register_blueprint(Camera,url_prefix='/camera')