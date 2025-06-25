from PyQt5 import QtCore, QtWidgets
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel("Привет, мир!")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.btnQuit = QtWidgets.QPushButton("&Закрыть окно")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)

if __name__ == "__main__": # код будет запущен только при запуске программы, а не импорте. __name__ will contain __main__
 # if the code is executed as the main program
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow() # Создаем экземпляр класса
    window.setWindowTitle("ООП-стиль создания окна")
    window.resize(300, 70)
    window.show() # Отображаем окно
    sys.exit(app.exec_()) # Запускаем цикл обработки событий

# app = QtWidgets.QApplication(sys.argv)
# window = MyWindow()  # Создаем экземпляр класса
# window.setWindowTitle("ООП-стиль создания окна")
# window.resize(300, 70)
# window.show()  # Отображаем окно
# sys.exit(app.exec_())  # Запускаем цикл обработки событий