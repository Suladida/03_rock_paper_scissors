from flask import Flask, render_template, request, redirect
from app import app
from app.models.game import *
from app.models.player import *
import random

@app.route('/')
def index():
    return render_template("index.html", title="Home")

@app.route('/result', methods=["POST", "GET"])
def game_result():
    name = request.form["name"]
    choice = request.form["choice"]
    player1 = Player(name, choice)
    choices = ["Rock", "Paper", "Scissors"]
    choice_2 = random.choice(choices)
    player2 = Player("Player 2", choice_2)
    current_game = Game(player1, player2)
    winner = current_game.play_game(player1, player2)
    return render_template("result.html", title="Result", player1=player1, player2=player2, winner=winner)
    

# @app.route('/result', methods=["POST"])
# def game_result():
#     name = request.form["name"]
#     choice = request.form["choice"]
#     player1 = Player("Lobsteretta", "Rock")
#     player2 = Player(name, choice)
#     current_game = Game(player1, player2)
#     winner = current_game.play_game(player1, player2)
#     return render_template("result.html", title="Result", player1=player1, player2=player2, winner=winner)
