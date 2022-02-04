from dataclasses import dataclass, field
import pickle
from game import Game
from series import Series

@dataclass
class GameList:
    games: list[Game] = field(default_factory=list)
    series: list[Series] = field(default_factory=list)

    def add_game(self, game: Game) -> None:
        self.games.append(game)

    def remove_game(self, game: Game) -> None:
        self.games.remove(game)

    def add_series(self, series: Series) -> None:
        self.series.append(series)
    
    def remove_series(self, series: Series) -> None:
        self.series.remove(series)

    def get_num_completed(self) -> tuple[int, int]:
        """Returns num_complete and num_of_games"""
        _num_complete = 0
        _num_of_games = 0
        for game in self.games:
            if game.completed:
                _num_complete += 1
            _num_of_games += 1
        return (_num_complete, _num_of_games)

    def __str__(self):
        return str([game.title for game in self.games])