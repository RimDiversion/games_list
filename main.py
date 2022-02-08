import pickle
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from views import TableView, MainWindow
from list import GameList

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        games_list = load()
        length = games_list.get_num_games()
        table = TableView(games_list, length, 6)
        main_window = MainWindow()
        main_window.setupUI(self, table)

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
    app = QApplication(sys.argv)
    win = Main()
    sys.exit(app.exec_())