from dataclasses import dataclass, field
import pickle
from game import Game
from series import Series


@dataclass
class GameList:
    games: dict[str: Game] = field(default_factory=dict)
    series: list[Series] = field(default_factory=list)

    def add_game(self, game: Game) -> None:
        self.games[game.title] = game

    def remove_game(self, game: Game) -> None:
        self.games.pop(game.title)

    def add_series(self, series: Series) -> None:
        self.series.append(series)
    
    def remove_series(self, series: Series) -> None:
        self.series.remove(series)

    def get_num_completed(self) -> tuple[int, int]:
        """Returns num_complete and num_of_games"""
        _num_complete = 0
        _num_of_games = 0
        for game in self.games.values():
            if game.completed:
                _num_complete += 1
            _num_of_games += 1
        return (_num_complete, _num_of_games)

    def to_complete(self) -> dict:
        _to_complete = {}
        for game in self.games.values():
            if not game.completed:
                _to_complete[game.title] = game
        return _to_complete

    def completed(self) -> dict:
        _completed = {}
        for game in self.games.values():
            if game.completed:
                _completed[game.title] = game
        return _completed

    def get_num_games(self) -> int:
        """Returns number of games in series"""
        _num_games = len(self.games)
        return _num_games

    def __str__(self) -> str:
        string = ''
        for game in sorted(self.games):
            string += game + '\n'
        return string[:-1]

    def __repr__(self) -> str:
        string = ''
        for game in sorted(self.games):
            string += game + '\n'
        return string[:-1]


def save(games_list, name: str = 'games_list') -> None:
    """Saves current game list to file using pickle"""
    with open(name + '.pkl', 'wb') as file:
        pickle.dump(games_list, file, pickle.HIGHEST_PROTOCOL)

def load(name: str = 'games_list') -> GameList:
    """Loads game list from file using pickle"""
    with open(name + '.pkl', 'rb') as file:
        games_list = pickle.load(file)
        return games_list