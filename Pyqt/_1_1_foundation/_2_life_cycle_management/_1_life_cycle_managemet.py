from PyQt5 import QtWidgets
import sys, time

def on_clicked():
   for i in range(1, 21):
      button.setDisabled(False)  # Делаем кнопку неактивной
      time.sleep(1) # "Засыпаем" на 1 секунду
      QtWidgets.qApp.processEvents() # Запускаем оборот цикла Без этого пункта программа зависнет пока цикл фор не закончится
      print("step -", i)
      button.setDisabled(True)

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Запустить процесс")
button.resize(200, 40)
button.clicked.connect(on_clicked)
button.show()
sys.exit(app.exec_())