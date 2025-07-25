from PyQt5 import QtCore, QtWidgets
import sys
import time

app = QtWidgets.QApplication(sys.argv)  #   created application can only one
window = QtWidgets.QWidget()      #   create window
# <object> = QWidget([parent = <PARENT>], [flags = <type window>]
#PARENT - link to parent component,
#flags - если тип окна указан, то компонент, имея родителя, также будет обладать своим собственным окном, но окажется привязанным к родителю.
# Это позволяет создать модальное окно которое будет блокировать только окно родителя, а не все окна приложения
window.setWindowTitle("Hello World")    #   set title
window.resize(800, 600)                 #    set min size

# флаги которые позволяют установить стиль окна и кнопок
# window.setWindowFlags(QtCore.Qt.Window |
#                       QtCore.Qt.Sheet |
#                       QtCore.Qt.WindowContextHelpButtonHint |
#                       QtCore.Qt.WindowStaysOnTopHint)
window.show()
window.show()      #   show window
# time.sleep(3)
# window.hide()       #   hide window
# time.sleep(3)
# window.show()       #   show window
# time.sleep(3)
# window.setVisible(False)    #   hide window
# time.sleep(3)
# window.setVisible(True)     #   show window
sys.exit(app.exec_())               #   for right completion