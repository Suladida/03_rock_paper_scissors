class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.players = []

    def add_players(self, player):
        self.players.append(player)

    def check_players(self):
        return len(self.players)

    def play_game(self, player1, player2):
        if player1.choice == "Rock" and player2.choice == "Scissors":
            return player1.name
        if player1.choice == "Rock" and player2.choice == "Paper":
            return player2.name
        if player1.choice == "Paper" and player2.choice == "Rock":
            return player1.name
        if player1.choice == "Paper" and player2.choice == "Scissors":
            return player2.name
        if player1.choice == "Scissors" and player2.choice == "Paper":
            return player1.name
        if player1.choice == "Scissors" and player2.choice == "Rock":
            return player2.name
        if player1.choice == player2.choice:
            return "It's a Draw!"