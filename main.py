from design import Ui_Form as Design
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem
import sys


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.events = []
        self.pushButton.clicked.connect(self.add)

    def add(self):
        if self.lineEdit.text() == '':
            self.label_2.setText('Ошибка. Не введено название')
        else:
            self.events.append([self.calendarWidget.selectedDate().toPyDate(), self.timeEdit.time(), self.lineEdit.text()])
            self.update()

    def update(self):
        self.listWidget.clear()
        for i in list(sorted(self.events)):
            self.listWidget.addItem(QListWidgetItem(f'{i[-1]}, {i[0]}, {i[1].toString()}'))


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())