from flask import render_template, request
from app import app
from app.models.game import *
from app.models.player import *
from app.models.blah import players

@app.route('/')
def index():
    return render_template("index.html", title="Home", players=players)

@app.route('/result', methods=["POST"])
def play_game():
    print(request.form)
    return "Done"