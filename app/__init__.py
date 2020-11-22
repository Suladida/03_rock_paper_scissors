from flask import Flask

app = Flask(__name__)
app.static_folder = "models/static"

from app import controller