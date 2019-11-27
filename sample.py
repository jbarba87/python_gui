from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class MyWindow(QMainWindow):
  
  contador = 0
  
  def __init__(self):
    super(MyWindow, self).__init__()
    self.setGeometry(200, 200, 500, 200)
    self.setWindowTitle("Example Window")
    
    # Not resizable
    self.setMinimumSize(400, 200)
    self.setMaximumSize(400, 200)
    self.initUI()
    
  def initUI(self):
    self.label = QtWidgets.QLabel(self)
    self.label.setText("Press next button")
    self.label.setGeometry(50, 50, 120, 30)
#    self.label.move(50, 50)
    
    self.button = QtWidgets.QPushButton(self)
    self.button.setText("Press me!")
    self.button.setGeometry(200, 50, 120, 30)
#    self.button.move(200, 50)
    self.button.clicked.connect(self.clic)
    
  def clic(self):
    self.contador = self.contador + 1
    texto = "Times clicked: " + str(self.contador)
    self.button.setText(texto)
    print(texto)
    
    
    if (self.contador >= 10):
      self.button.setEnabled(False)

    
    
def window():
  app = QApplication(sys.argv)
  win = MyWindow()
  win.show()
  sys.exit(app.exec_())
  
window()
