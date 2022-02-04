from PyQt5.QtWidgets import (QTableWidget, QDialog, QTableWidgetItem, QLabel, QLineEdit,
    QVBoxLayout, QDialogButtonBox, QFormLayout, QGroupBox, QCheckBox, QDateEdit, QSpinBox,
    )

 
class TableView(QTableWidget):
    def __init__(self, games_list, *args):
        self.games_list = games_list
        QTableWidget.__init__(self, *args)
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        add_button = QTableWidgetItem("Add")
        self.setItem(1, 10, add_button)
        self.item

    def add(self):
        game_entry = GameEntry(self)
        game_entry.exec_()

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

class GameEntry(QDialog):
    def __init__(self, table):
        super(GameEntry, self).__init__()
        self.createFormGroupBox()
        self.table = table
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        
        self.setWindowTitle("Game Entry")
        
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox()
        layout = QFormLayout()
        layout.addRow(QLabel("Title:"), QLineEdit())
        layout.addRow(QLabel("Completed:"), QCheckBox())
        layout.addRow(QLabel("Date Completed:"), QDateEdit())
        layout.addRow(QLabel("Completed 100%:"), QCheckBox())
        layout.addRow(QLabel("Date Completed 100%:"), QDateEdit())
        layout.addRow(QLabel("Rating:"), QSpinBox(minimum=0, maximum=100))
        
        self.formGroupBox.setLayout(layout)
