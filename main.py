import pickle
import sys
from PyQt5.QtWidgets import QApplication
from views import TableView
from list import GameList

def main():
    games_list = load()
    length = games_list.get_num_games()
    app = QApplication(sys.argv)
    table = TableView(games_list, length, 6)
    table.show()
    sys.exit(app.exec_())

def save(games_list, name: str = 'games_list') -> None:
    """Saves current game list to file using pickle"""
    with open(name + '.pkl', 'wb') as file:
        pickle.dump(games_list, file, pickle.HIGHEST_PROTOCOL)

def load(name: str = 'games_list') -> GameList:
    """Loads game list from file using pickle"""
    with open(name + '.pkl', 'rb') as file:
        games_list = pickle.load(file)
        return games_list

if __name__ == '__main__':
    main()