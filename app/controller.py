from flask import Flask, render_template, request, redirect
from app import app
from app.models.game import *
from app.models.player import *
from app.models.blah import players

@app.route('/')
def index():
    return render_template("index.html", title="Home", players=players)

@app.route('/result', methods=["POST"])
def game_result():
    name = request.form["name"]
    choice = request.form["choice"]
    player1 = Player("Lobsteretta", "Rock")
    player2 = Player(name, choice)
    current_game = Game(player1, player2)
    winner = current_game.play_game(player1, player2)

    # new_player = Player(name=name, choice=choice)
    # result = add_players(new_player)
    return render_template("result.html", title="Home", players=players, player1=player1, player2=player2, winner=winner)
    # else:
        # return "ERRORRRRRRRRRRRR"








# @app.route('/result', methods=["POST"])
# def game_result():
#     # if request.method == "POST":
#     name = request.form["name"]
#     choice = request.form["choice"]
#     player1 = Player("Lobsteretta", "Rock")
#     player2 = Player(name, choice)
#     # if request.form["choice"] == player1.choice:
#     if player2.choice == player1.choice:

#     # new_player = Player(name=name, choice=choice)
#     # result = add_players(new_player)
#         return render_template("result.html", title="Home", players=players, player1=player1, player2=player2)
#     else:
#         return "ERRORRRRRRRRRRRR"