from PyQt5 import QtCore, QtWidgets

# Класс для передачи сигнала  из потока в GUI
class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str) # в скобках указываем тип данных который будем передавать из потока
    def __init__(self, parent=None):    # parent=None без родительского окна
        QtCore.QThread.__init__(self, parent)

    def run(self):
        for i in range(1,21):
            self.sleep(1)
            self.mysignal.emit(str(i)) # данные которые передаем из потока спомощью сигнала

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None): # parent=None без родительского окна
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel('Нажмите кнопку для запуска потока') # можно вместо текста использовать html и css
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button = QtWidgets.QPushButton('Запустить процесс')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.mythread = MyThread()  # Создаем экземпляр класса
        self.button.clicked.connect(self.on_clicked)    # connect служит для присоединения функции к событию
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    def on_clicked(self):
        self.button.setDisabled(True)  # Делаем кнопку неактивной
        self.mythread.start()  # Запускаем поток

    def on_started(self):  # Вызывается при запуске потока
        self.label.setText("Вызван метод on_started()")

    def on_finished(self):  # Вызывается при завершении потока
        self.label.setText("Вызван метод on_finished()")
        self.button.setDisabled(False)  # Делаем кнопку активной

    def on_change(self, s):
        self.label.setText(s)


if __name__ == "__main__":  # код будет запущен только при запуске программы (текущего файлика), а не импорте. __name__ will contain __main__
    import sys

    app = QtWidgets.QApplication(sys.argv) # объект приложения может быть только один sys.argv в каждой операционной системе указыается что то свое
    window = MyWindow()
    window.setWindowTitle("Использование класса QThread")
    # window.resize(300, 70) # указывает рекомендованные значения, если виджеты будут выходить за грацицы окна окно увеличется автоматически
    padding_left = 900 # второй способ установки геометрии
    padding_top = 300
    window_width = 500
    window_height = 300
    window.setGeometry(padding_left,padding_top,window_width,window_height)
    window.show()
    sys.exit(app.exec_()) # для того что бы программа завершалась корректно.
