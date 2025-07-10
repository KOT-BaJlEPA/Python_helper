from PyQt5 import QtCore, QtWidgets
from _1_OOP_style_create_window import MyWindow
import sys
import time


class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent) # parent=None без родительского окна
        self.myWidget = MyWindow()
        self.myWidget.vbox.setContentsMargins(50, 100, 200, 400) #отступ виджета от остальных элементов(л,в,п,н)
        self.button = QtWidgets.QPushButton("&Изменить надпись")
        mainBox = QtWidgets.QVBoxLayout()
        mainBox.addWidget(self.myWidget)
        mainBox.addWidget(self.button)
        self.setLayout(mainBox)
        self.button.clicked.connect(self.on_clicked)
    def on_clicked(self):
        # self.on_change()
        # self.on_change2()
        # self.myWidget.label.setText("Новая надпись")
        # self.button.setDisabled(True)
        self.on_change2()
        QtWidgets.qApp.processEvents()# необходимо для перезапуска цикла
        self.on_change()
        # если раскомментировать то текст "Новая надпись" мы не увидим т.к. значение окна поменяется когда функция on_clicked() закончит свою работу
        # time.sleep(10)
        # self.button.setDisabled(False)
        # self.myWidget.label.setText("Old text")

    def on_change(self):
        time.sleep(1)
        self.button.setDisabled(False)
        self.myWidget.label.setText("Old text")

    def on_change2(self):
        time.sleep(1)
        self.myWidget.label.setText("Новая надпись")
        self.button.setDisabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowTitle("Преимущество ООП-стиля")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())
