from PyQt5 import QtCore, QtGui, QtWidgets

class Thread1(QtCore.QThread):
    signal1 = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.count = 0

    def run(self): # переопределяем метод
        self.exec_() # запускаем цикл обработки сигналов

    def on_started(self):
        c
        self.signal1.emit('started')