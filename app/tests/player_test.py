import unittest

from app.models.game import Game
from app.models.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Lobster1", "Choice1")
        self.player2 = Player("Lobster2", "Choice2")
        
    # @unittest.skip("Delete this line to run the test")
    def test_player_has_name(self):
        self.assertEqual("Lobster1", self.player1.check_player_name())

