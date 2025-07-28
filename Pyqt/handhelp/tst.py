from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class SendLoginWindow(QtWidgets.QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.setWindowTitle('Отправить логин')
        self.resize(300, 100) # минимальные ширина и длинна

        # Центральный виджет и основной layout
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.vbox = QtWidgets.QVBoxLayout(central_widget)
        # Поля для ввода логина и почты
        self.input_login = QtWidgets.QLineEdit()
        self.input_login.setPlaceholderText('Введите логин')
        self.input_email = QtWidgets.QLineEdit()
        self.input_email.setPlaceholderText('Введите почту')
        # Кнопки отправить и стереть
        self.btn_send = QtWidgets.QPushButton('Отправить')
        self.btn_send.clicked.connect(self.send_login)
        self.btn_clear = QtWidgets.QPushButton('Очистить')
        self.btn_clear.clicked.connect(self.clear_input)
        # Поле отображения ошибок и хода выполнения программы (2 строчки + 10px отступы)
        self.description_and_error = QtWidgets.QLabel('<center>Пока ошибок нет</center>')
        # self.description_and_error = QtWidgets.QTextEdit()
        # self.description_and_error.setReadOnly(True)
        # self.description_and_error.setText('Пока ошибок нет')
        # font_metrics = self.description_and_error.fontMetrics()
        # line_height = font_metrics.lineSpacing()
        # self.description_and_error.setFixedHeight(2 * line_height + 10)
        # Добавляем виджеты в layout
        self.vbox.addWidget(self.input_login)
        self.vbox.addWidget(self.input_email)
        self.vbox.addWidget(self.btn_send)
        self.vbox.addWidget(self.btn_clear)
        self.vbox.addWidget(self.description_and_error)

    def send_login(self):
        login = self.input_login.text()
        email = self.input_email.text()
        self.description_and_error.setText('Логин: ' + login + 'отправлен\nпочта : ' + email)

    def clear_input(self):
        self.description_and_error.clear()
        self.description_and_error.setText('Пока ошибок нет')
        self.input_login.clear()
        self.input_email.clear()







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SendLoginWindow()
    window.show()
    sys.exit(app.exec_())
