from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

 
class TableView(QTableWidget):
    def __init__(self, games_list, *args):
        self.games_list = games_list
        QTableWidget.__init__(self, *args)
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
 
    def setData(self):
        self.data = {}
        headers = [
            'Title',
            'Completed',
            'Date Completed',
            'Completed 100%',
            'Date Completed 100%',
            'Rating']       
        self.setHorizontalHeaderLabels(headers)
        
        for i, game in enumerate(self.games_list.games):
            game_details = game.get_details()
            for n, detail in enumerate(game_details):
                new_item = QTableWidgetItem(str(game_details[detail]))
                self.setItem(i, n, new_item)
