class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.players = []

    def add_players(self, player):
        self.players.append(player)

    def check_players(self):
        return len(self.players)