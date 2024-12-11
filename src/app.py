import sys
from src.gui.mainWindow import Ui_MainWindow
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.initialize_buttons()
MainWindow.show()
sys.exit(app.exec_())