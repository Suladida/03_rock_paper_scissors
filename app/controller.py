from flask import render_template
from app import app
# from app.models.player import Player
# from app.models.game import Game

@app.route('/')
def index():
    return render_template("index.html", title="Home")