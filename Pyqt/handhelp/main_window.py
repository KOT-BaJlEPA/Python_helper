from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setWindowTitle("Помогалка v 2.0")
        self.resize(300, 200) # width height

        # Центральный виджет и основной layout
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.vbox = QtWidgets.QVBoxLayout(central_widget)
        self.open_sub_windows = {}
        for btn_name in args:
            button = QtWidgets.QPushButton(btn_name)
            button.clicked.connect(lambda checked, name=btn_name: self.on_button_click(name))
            self.vbox.addWidget(button)

    def on_button_click(self, name):
        # дочернее окно с таким именем уже открыто
        if name in self.open_sub_windows:
            sub_window = self.open_sub_windows[name]
            sub_window.activateWindow()  # Активируем окно
            sub_window.raise_()  # фокус на открытое окно
        else:
            sub_window = SubWindow(name, parent=self) # при закрытии основного окна закроются и дочерние окна
            self.open_sub_windows[name] = sub_window
            sub_window.show()



class SubWindow(QtWidgets.QMainWindow):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.resize(200, 200) # width height
        # Центральный виджет и основной layout
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.vbox = QtWidgets.QVBoxLayout(central_widget)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow('btn_1', 'btn_2', 'btn_3', 'btn_4')
    window.show()
    sys.exit(app.exec_())
