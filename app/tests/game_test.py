import unittest

from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Lobster1", "Choice1")
        self.player2 = Player("Lobster2", "Choice2")
        self.game = Game("Player1", "Player2")
        

    # @unittest.skip("Delete this line to run the test")
    def test_add_players(self):
        self.game.add_players(self.player1)
        self.game.add_players(self.player2)
        self.assertEqual(2, self.game.check_players())