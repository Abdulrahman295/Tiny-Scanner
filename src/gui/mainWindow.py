import os
from PyQt5 import QtCore, QtGui, QtWidgets
from src.fileManager.fileManager import FileManager
from src.scanner.scanner import Scanner

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 753)
        MainWindow.setMinimumSize(QtCore.QSize(750, 753))
        MainWindow.setMaximumSize(QtCore.QSize(750, 753))
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icon.png')
        MainWindow.setWindowIcon(QtGui.QIcon(icon_path))
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: #19232D;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(36, 160, 237);\n"
"    color: white;\n"
"    font-size: 15px; \n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    margin: 4px;\n"
"    outline: none;\n"
"    border: none;\n"
"    font-family: \"Arial Rounded MT Bold\", Arial, sans-serif;\n"
"}\n"
"\n"
"/* Disabled Button State */\n"
"QPushButton:disabled {\n"
"    background-color: rgb(36, 160, 237);\n"
"    color: rgba(255, 255, 255, 0.7);\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"/* Checked Button State */\n"
"QPushButton:checked {\n"
"    background-color: rgb(25, 140, 210);\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Checked and Disabled Button State */\n"
"QPushButton:checked:disabled {\n"
"    background-color: rgb(25, 140, 210);\n"
"    color: rgba(255, 255, 255, 0.7);\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* Checked and Selected Button State */\n"
"QPushButton:checked:selected {\n"
"    background: rgb(25, 140, 210);\n"
"    color: white;\n"
"}\n"
"\n"
"/* Hover State */\n"
"QPushButton:hover {\n"
"    background-color: rgb(25, 140, 210);\n"
"    color: white;\n"
"}\n"
"\n"
"/* Pressed Button State */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(20, 120, 180);\n"
"    color: white;\n"
"}\n"
"\n"
"/* Selected Button State */\n"
"QPushButton:selected {\n"
"    background: rgb(25, 140, 210);\n"
"    color: white;\n"
"}\n"
"\n"
"/* Menu Indicator Positioning */\n"
"QPushButton::menu-indicator {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: bottom right;\n"
"    bottom: 4px;\n"
"}\n"
"\n"
"/* Dialog Button Box Special Case */\n"
"QDialogButtonBox QPushButton {\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white; /* White text to match other elements */\n"
"    padding: 2px;\n"
"    font-style: italic;\n"
"     font-weight: bold;\n"
"    font-size: 18px;\n"
"    font-family: \"Arial Rounded MT Bold\", Arial, sans-serif;\n"
"}\n"
"\n"
"QTextEdit{\n"
"    font-size: 20px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(10, 10, 731, 731))
        self.verticalWidget.setStyleSheet("")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalWidget)
        self.label.setStyleSheet("QLabel {\n"
"    font-size: 20px;\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.file_path_holder = QtWidgets.QLineEdit(self.verticalWidget)
        self.file_path_holder.setReadOnly(True) 
        self.file_path_holder.setStyleSheet("QLineEdit {\n"
"    /*background-color: rgb(25, 35, 45); /* Dark background */\n"
"    background-color: #19232D;\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    padding-left: 4px;\n"
"    padding-right: 4px;\n"
"    border-style: solid;\n"
"    border: 1px solid rgb(69, 83, 100); /* Muted border */\n"
"    border-radius: 4px;\n"
"    color: white; /* White text to match button */\n"
"    font-family: \"Arial Rounded MT Bold\", Arial, sans-serif;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: rgb(25, 35, 45);\n"
"    color: rgba(255, 255, 255, 0.6); /* Lighter disabled text */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 1px solid rgb(52, 103, 146); /* Slightly brighter blue border on hover */\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid rgb(36, 160, 237); /* Match button\'s active color */\n"
"}\n"
"\n"
"QLineEdit:selected {\n"
"    background-color: rgb(52, 103, 146);\n"
"    color: white;\n"
"}")
        self.file_path_holder.setObjectName("file_path_holder")
        self.horizontalLayout_5.addWidget(self.file_path_holder)
        self.open_file_button = QtWidgets.QPushButton(self.verticalWidget)
        self.open_file_button.setStyleSheet("QPushButton {\n"
"    width: 100px;  /* Fixed width */\n"
"    min-width: 100px;\n"
"    max-width: 100px;\n"
"}")
        self.open_file_button.setObjectName("open_file_button")
        self.horizontalLayout_5.addWidget(self.open_file_button)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.verticalWidget)
        self.horizontalWidget_2.setStyleSheet("QWidget {\n"
"    border: 1px solid rgb(69, 83, 100);\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"    margin-top: 10px;\n"                                                                    
"}\n"
"\n"
"QWidget > QLabel, \n"
"QWidget > QPushButton {\n"
"    border: none;\n"
"}\n"
"\n"
"")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.horizontalWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.code_holder = QtWidgets.QTextEdit(self.horizontalWidget_2)
        self.code_holder.setStyleSheet("QTextEdit{\n"
"    background-color: #19232D;\n"
"    margin: 4px;\n"
"    color: white;\n"
"    font-family: \"Arial Rounded MT Bold\", Arial, sans-serif;\n"
"    font-size: 20px;\n"
"}\n"
"QTextEdit:disabled {\n"
"    background-color: rgb(25, 35, 45);\n"
"    color: rgba(255, 255, 255, 0.6); /* Lighter disabled text */\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    border: 1px solid rgb(52, 103, 146); /* Slightly brighter blue border on hover */\n"
"    color: white;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 1px solid rgb(36, 160, 237); /* Match button\'s active color */\n"
"}\n"
"\n"
"QTextEdit:selected {\n"
"    background-color: rgb(52, 103, 146);\n"
"    color: white;\n"
"}")

        self.code_holder.setObjectName("code_holder")
        self.verticalLayout_2.addWidget(self.code_holder)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scan_button = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.scan_button.setObjectName("scan_button")
        self.horizontalLayout_2.addWidget(self.scan_button)
        self.parse_button = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.parse_button.setObjectName("parse_button")
        self.horizontalLayout_2.addWidget(self.parse_button)
        self.close_button = QtWidgets.QPushButton(self.horizontalWidget_2)
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_2.addWidget(self.close_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.horizontalWidget_2)
        self.statusBar = QtWidgets.QStatusBar(self.verticalWidget)
        self.statusBar.setStyleSheet("""
            QStatusBar {
                color: white;
                background-color: #19232D;
                font-size: 15px;
                font-weight: bold;
                font-style: italic;
                margin: 2px;
            }
        """)
        self.statusBar.setSizeGripEnabled(False)  # Remove the resize grip
        self.verticalLayout.addWidget(self.statusBar)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tiny Parser"))
        self.open_file_button.setText(_translate("MainWindow", "Open"))
        self.label_2.setText(_translate("MainWindow", "Code"))
        self.scan_button.setText(_translate("MainWindow", "Scan"))
        self.parse_button.setText(_translate("MainWindow", "Parse"))
        self.close_button.setText(_translate("MainWindow", "Close"))

    def showMessage(self, message):
        self.statusBar.showMessage(message, 6000)

    def openFileFunction(self):
        file_path, code = FileManager.read_code(self)

        if not file_path or not code:
            return
        
        self.file_path_holder.setText(file_path)
        self.code_holder.setText(code)
    
    def closeWindowFunction(self):
        QtWidgets.QApplication.quit()

    def scanFunction(self):
        if not self.code_holder.toPlainText():
            self.showMessage("Please open a file or write code in order to scan")
            return
        try:
            code = self.code_holder.toPlainText()
            scanner = Scanner(code)
            tokens = scanner.tokenize()
            FileManager.write_tokens(self, tokens)
        except Exception as e:
            self.showMessage(f"Error during scanning: {e}")
        

    def initialize_buttons(self):
        self.open_file_button.clicked.connect(self.openFileFunction)
        self.close_button.clicked.connect(self.closeWindowFunction)
        self.scan_button.clicked.connect(self.scanFunction)
        self.parse_button.clicked.connect(lambda: print("Parse button clicked"))
