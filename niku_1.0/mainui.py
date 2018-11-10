from PyQt5 import QtWidgets,uic
  
  
app = QtWidgets.QApplication([])
niku = uic.loadUi('niku.ui')
niku.show()

app.exec()
