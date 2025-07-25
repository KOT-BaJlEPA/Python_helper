# from PyQt5 import QtCore, QtGui, QtWidgets
# import sys
#
# class Thread_1(QtCore.QThread):
#     signal_1 = QtCore.pyqtSignal(str) # created a signal for data exchange between threads (str is data type for the exchange)
#
#     def __init__(self, parent=None):
#         QtCore.QThread.__init__(self, parent)
#         self.count = 0
#
#     def run(self): # переопределяем метод
#         self.exec_() # запускаем цикл обработки сигналов
#
#     def on_start(self):
#         self.count += 1
#         self.signal_1.emit('from Thread_1 - ' + str(self.count)) #transmits a signal with data in this case str-'from Thread_1 - ' + str(self.count)  to the all slots connected to this signal
#
#
# class Thread_2(QtCore.QThread):
#     signal_2 = QtCore.pyqtSignal(
#         str)  # created a signal for data exchange between threads (str is data type for the exchange)
#
#     def __init__(self, parent=None):
#         QtCore.QThread.__init__(self, parent)
#
#     def run(self):  # переопределяем метод
#         self.exec_()  # запускаем цикл обработки сигналов(отправка строкового значения всем подключенным слотам)
#
#     def on_change(self, i):
#         i += 10
#         self.signal_2.emit('%d' %i)
#
# class MyWindow(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         QtWidgets.QMainWindow.__init__(self, parent)
#         self.label = QtWidgets.QLabel(self)
#         self.label.setAlignment(QtCore.Qt.AlignCenter)
#         self.button = QtWidgets.QPushButton('Generate signal')
#         self.vbox = QtWidgets.QVBoxLayout()
#         self.vbox.addWidget(self.label)
#         self.vbox.addWidget(self.button)
#         self.setLayout(self.vbox)
#         self.thread1 = Thread_1()
#         self.thread2 = Thread_2()
#         self.thread1.start()
#         self.thread2.start()
#         self.button.clicked.connect(self.thread1.on_start)
#         self.thread1.signal_1.connect(self.thread2.on_change)
#         self.thread2.signal_2.connect(self.on_thread2_s2)
#
#     def on_thread2_s2(self, s):
#         self.label.setText(s)
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     window = MyWindow()
#     window.setWindowTitle('exchange a signal between threads')
#     window.resize(800, 600)
#     window.show()
#     sys.exit(app.exec_())
#


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Thread_1(QtCore.QThread):
    signal_1 = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.count = 0
        self.running = True

    def run(self):
        while self.running:
            self.msleep(100)  # Небольшая пауза для снижения нагрузки на CPU

    def on_start(self):
        self.count += 1
        self.signal_1.emit(f'from Thread_1 - {self.count}')

    def stop(self):
        self.running = False
        self.wait()


class Thread_2(QtCore.QThread):
    signal_2 = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = True

    def run(self):
        while self.running:
            self.msleep(100)

    def on_change(self, i):
        try:
            num = int(i.split('-')[-1])  # Извлекаем число из строки
            num += 10
            self.signal_2.emit(str(num))
        except (ValueError, IndexError):
            self.signal_2.emit('0')

    def stop(self):
        self.running = False
        self.wait()


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exchange signals between threads')
        self.resize(800, 600)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        self.label = QtWidgets.QLabel('Waiting for data...', alignment=QtCore.Qt.AlignCenter)
        self.button = QtWidgets.QPushButton('Generate signal')

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        central_widget.setLayout(layout)

        # Создаем и запускаем потоки
        self.thread1 = Thread_1()
        self.thread2 = Thread_2()

        # Подключаем сигналы
        self.button.clicked.connect(self.thread1.on_start)
        self.thread1.signal_1.connect(self.thread2.on_change)
        self.thread2.signal_2.connect(self.update_label)

        self.thread1.start()
        self.thread2.start()

    def update_label(self, text):
        self.label.setText(f'Received: {text}')

    def closeEvent(self, event):
        # Корректно останавливаем потоки при закрытии окна
        self.thread1.stop()
        self.thread2.stop()
        event.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())