import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Lobster Queen", "Rock")
        self.player2 = Player("Lobster King", "Scissors")
        self.game = Game(self.player1, self.player2)
        
    # @unittest.skip("Delete this line to run the test")
    def test_add_players(self):
        self.game.add_players(self.player1)
        self.game.add_players(self.player2)
        self.assertEqual(2, self.game.check_players())

    # @unittest.skip("Delete this line to run the test")
    def test_play_game(self):
        self.assertEqual(self.player1.name, self.game.play_game(self.player1, self.player2))

