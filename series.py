from dataclasses import dataclass, field
from game import Game

@dataclass
class Series:
    title: str
    games: list[Game] = field(default_factory=list)

    def get_rating(self) -> int:
        """Returns average rating of all games in series"""
        _total = 0
        _num_of_games = 0
        for game in self.games:
            if game.rating:
                _total += game.rating
            _num_of_games += 1
        avg_rating = _total // _num_of_games
        return avg_rating

    def get_num_completed(self) -> tuple[int, int]:
        """Returns num_complete and num_of_games"""
        _num_complete = 0
        _num_of_games = 0
        for game in self.games:
            if game.completed:
                _num_complete += 1
            _num_of_games += 1
        return (_num_complete, _num_of_games)

    def add_game(self, game: Game) -> None:
        """Add game to series"""
        self.games.append(game)

    def remove_game(self, game: Game) -> None:
        """Remove game from series"""
        self.games.remove(game)

    def get_num_games(self) -> int:
        """Returns number of games in series"""
        _num_games = len(self.games)
        return _num_games
