from PyQt5 import QtCore, QtWidgets

# QtWidgets.qApp.processEvents() # Запускаем оборот цикла
# Класс для передачи сигнала  из потока в GUI
class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str) # в скобках указываем тип данных который будем передавать из потока

    def __init__(self, parent=None):    # parent=None без родительского окна
        QtCore.QThread.__init__(self, parent)
        self.running = False # Флаг выполнения потока
        self.counter = 0

    def run(self): # переопределяем метод
        self.running = True
        while self.running:
            self.counter += 1
            self.sleep(1)
            self.mysignal.emit('count = %s' %self.counter) # данные, которые передаем из потока с помощью сигнала

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None): # parent=None без родительского окна
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel('Нажмите кнопку для запуска потока') # можно вместо текста использовать html и css
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button_start = QtWidgets.QPushButton('Запустить процесс')
        self.button_stop = QtWidgets.QPushButton('Остановить процесс')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button_start)
        self.vbox.addWidget(self.button_stop)
        self.setLayout(self.vbox)
        self.mythread = MyThread()  # Создаем экземпляр класса потока
        self.button_start.clicked.connect(self.on_clicked)    # connect служит для присоединения функции к событию
        self.button_stop.clicked.connect(self.on_stop)      # connect служит для присоединения функции к событию
        self.mythread.started.connect(self.on_started) # встроенный срабатывает при старте потока
        self.mythread.finished.connect(self.on_finished) # встроенный срабатывает при завершении потока
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection) # QtCore.Qt.QueuedConnection
        # говорит, что сигнал помещается в очередь обработки событий, т.е. в поток GUI

    def on_clicked(self):
        self.button_start.setDisabled(True)  # Делаем кнопку неактивной
        self.mythread.start()  # Запускаем поток

    def on_stop(self):
        self.mythread.running = False

    def on_started(self):  # Вызывается при запуске потока
        self.label.setText("Вызван метод on_started()")

    def on_finished(self):  # Вызывается при завершении потока
        self.label.setText("Вызван метод on_finished()")
        self.button_start.setDisabled(False)  # Делаем кнопку активной,

    def on_change(self, s):    # второй параметр метода служит для приема значения переданного сигналу
        self.label.setText(s)

    def closeEvent(self, event): # перехватываем закрытие окна нужен для корректного завершения программы
        self.hide() # скрываем окно, но программа продолжает работать
        self.mythread.running = False # меняем флаг выполнения программы
        self.mythread.wait(5000) # ждем максимум 5 сек пока поток завершит свою работу, если поток завершится раньшеЮ то программа завершиться раньше
        event.accept() # закрываем окно
        # event.ignore()  # для игнорирования завершения программы, программы не завершится


if __name__ == "__main__":  # код будет запущен только при запуске программы (текущего файлика), а не импорте. __name__ will contain __main__
    import sys

    app = QtWidgets.QApplication(sys.argv) # объект приложения может быть только один sys.argv в каждой операционной системе указыается что то свое
    window = MyWindow()
    window.setWindowTitle("Запуск и остановка потока ")
    # window.resize(300, 70) # указывает рекомендованные значения, если виджеты будут выходить за грацицы окна окно увеличется автоматически
    padding_left = 900 # второй способ установки геометрии
    padding_top = 300
    window_width = 500
    window_height = 300
    window.setGeometry(padding_left,padding_top,window_width,window_height)
    window.show()
    sys.exit(app.exec_()) # для того что бы программа завершалась корректно.
