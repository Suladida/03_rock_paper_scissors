import unittest

from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Lobster1", "Choice1")
        self.player2 = Player("Lobster2", "Choice2")
        self.players = [self.player1, self.player2]

    @unittest.skip("Delete this line to run the test")
    def test_check_players(self):
        self.assertEqual(2, self.players.check_players())