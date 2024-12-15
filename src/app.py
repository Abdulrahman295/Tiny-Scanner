import os
import sys
from src.gui.mainWindow import Ui_MainWindow
from PyQt5 import QtWidgets

def set_graphviz_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    graphviz_bin = os.path.join(current_dir, "graphviz", "bin")
    os.environ["PATH"] += os.pathsep + graphviz_bin

def main():
    set_graphviz_path()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.initialize_buttons()
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()