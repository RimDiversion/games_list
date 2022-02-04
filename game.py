from datetime import date
from dataclasses import dataclass

@dataclass
class Game:    
    title: str
    completed: bool = False
    completion_date: date = None
    one_hundereded: bool = False
    one_hundereded_date: date = None
    rating: int = None
    

    def complete(self, date=date.today()) -> None:
        """Marks game as complete with the default date of today"""
        self.completion_date = date
        self.completed = True

    def uncomplete(self) -> None:
        """Sets game completion status to False"""
        self.completion_date = None
        self.completed = False

    def one_hundered(self, date=date.today()) -> None:
        """Marks game as completed 100% achievements"""
        self.one_hundereded_date = date
        self.one_hundereded = True

    def unone_hundered(self) -> None:
        """Sets game 100% achievement status to False"""
        self.one_hundereded_date = None
        self.one_hundereded = False

    def rate(self, rating: int) -> None:
        """Rates game from 0 to 100"""
        if 0 <= rating <= 100:
            self.rating = rating
        else:
            raise TypeError("Enter int from 0-100")

    def get_details(self) -> dict:
        details = {
        'title' : self.title,
        'completed' : self.completed,
        'completion_date' : self.completion_date,
        'one_hundereded' : self.one_hundereded,
        'one_hundereded_date' : self.one_hundereded_date,
        'rating' : self.rating
        }
        return details

    def __str__(self):
        return self.title