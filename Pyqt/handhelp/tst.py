from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setWindowTitle("Помогалка v 2.0")
        self.resize(300, 200)

        # Словарь для хранения открытых окон
        self.open_windows = {}

        # Центральный виджет и основной layout
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.vbox = QtWidgets.QVBoxLayout(central_widget)

        for btn_name in args:
            button = QtWidgets.QPushButton(btn_name)
            button.clicked.connect(lambda checked, name=btn_name: self.on_button_click(name))
            self.vbox.addWidget(button)

    def on_button_click(self, name):
        # Если окно с таким именем уже существует
        if name in self.open_windows:
            window = self.open_windows[name]
            window.activateWindow()  # Активируем окно
            window.raise_()  # Поднимаем на передний план
            return

        # Создаем новое окно
        new_window = QtWidgets.QMainWindow()
        new_window.setWindowTitle(name)
        new_window.resize(200, 150)

        # Добавляем метку с названием кнопки
        label = QtWidgets.QLabel(f"Это окно кнопки: {name}")
        label.setAlignment(QtCore.Qt.AlignCenter)

        # Устанавливаем центральный виджет
        central_widget = QtWidgets.QWidget()
        new_window.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)
        layout.addWidget(label)

        # Сохраняем ссылку на окно
        self.open_windows[name] = new_window

        # При закрытии окна удаляем его из словаря
        new_window.destroyed.connect(lambda: self.open_windows.pop(name, None))

        # Показываем новое окно
        new_window.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow('btn_1', 'btn_2', 'btn_3', 'btn_4')
    window.show()
    sys.exit(app.exec_())