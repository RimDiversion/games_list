import pickle
from list import GameList



def main():
    games_list = GameList()

def save(games_list, name: str = 'games_list') -> None:
    """Saves current game list to file using pickle"""
    with open(name + '.pkl', 'wb') as file:
        pickle.dump(games_list, file, pickle.HIGHEST_PROTOCOL)

def load(name: str = 'games_list') -> GameList:
    """Loads game list from file using pickle"""
    with open(name + '.pkl', 'rb') as file:
        games_list = pickle.load(file)
        return games_list