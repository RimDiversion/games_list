import unittest
from datetime import date
import os
from game import Game
from series import Series
from list import GameList
from main import save, load

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game('Test')
        self.assertEqual(self.game.title, 'Test')

    def test_complete(self):
        self.assertEqual(self.game.completed, False)
        self.assertEqual(self.game.completion_date, None)
        self.game.complete()
        self.assertEqual(self.game.completed, True)
        self.assertEqual(self.game.completion_date, date.today())
        self.game.uncomplete()
        self.assertEqual(self.game.completed, False)
        self.assertEqual(self.game.completion_date, None)
    
    def test_one_hundered(self):
        self.assertEqual(self.game.one_hundereded, False)
        self.assertEqual(self.game.one_hundereded_date, None)
        self.game.one_hundered()
        self.assertEqual(self.game.one_hundereded, True)
        self.assertEqual(self.game.one_hundereded_date, date.today())
        self.game.unone_hundered()
        self.assertEqual(self.game.one_hundereded, False)
        self.assertEqual(self.game.one_hundereded_date, None)

    def test_rate(self):
        self.assertEqual(self.game.rating, None)
        self.game.rate(75)
        self.assertEqual(self.game.rating, 75)
        self.game.rate(100)
        self.assertEqual(self.game.rating, 100)
        self.game.rate(0)
        self.assertEqual(self.game.rating, 0)
        self.assertRaises(TypeError, self.game.rate, 150)
        self.assertRaises(TypeError, self.game.rate, -10)

class TestSeries(unittest.TestCase):
    def setUp(self):
        self.game1 = Game('Game 1', rating=50, completed=True)
        self.game2 = Game('Game 2', rating=75, completed=False)
        self.game3 = Game('Game 3', rating=95, completed=True)
        self.game4 = Game('Game 4')
        games = [self.game1, self.game2, self.game3]
        self.series = Series('Series 1', games)

    def test_get_rating(self):
        self.assertEqual(self.series.get_rating(), 73)
        self.game1.rate(55)
        self.assertEqual(self.series.get_rating(), 75)

    def test_get_num_completed(self):
        self.assertEqual(self.series.get_num_completed(), (2,3))

    def test_get_num_games(self):
        self.assertEqual(self.series.get_num_games(), 3)

    def test_add_game(self):
        self.series.add_game(self.game4)
        self.assertEqual(self.series.get_num_games(), 4)
        self.series.remove_game(self.game4)
        self.assertEqual(self.series.get_num_games(), 3)

class TestGameList(unittest.TestCase):
    def setUp(self):
        self.game1 = Game('Game 1', completed=True)
        self.game2 = Game('Game 2', completed=False)
        self.game3 = Game('Game 3', completed=True)
        self.game4 = Game('Game 4')
        games = [self.game1, self.game2, self.game3]
        series = Series('Series 1', games)
        self.game_list = GameList(games=games,series=series)
        self.test_list = GameList()

    def test_get_num_completed(self):
        self.assertEqual(self.game_list.get_num_completed(), (2, 3))

class TestMain(unittest.TestCase):
    def setUp(self):
        self.game1 = Game('Game 1')
        self.game2 = Game('Game 2')
        self.game3 = Game('Game 3')
        games = [self.game1, self.game2, self.game3]
        series = Series('Series 1', games)
        self.game_list = GameList(games=games,series=series)
        self.test_list = GameList()

    def test_save(self):
        self.assertNotEqual(self.game_list, self.test_list)
        save(self.game_list, name='test_list')
        self.test_list = load(name='test_list')
        self.assertEqual(self.game_list, self.test_list)
        os.remove('test_list.pkl')
