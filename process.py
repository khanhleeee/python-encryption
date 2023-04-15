from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFormLayout
from PyQt6.uic import loadUi

import sys
import file_funcs.DocFile as DocFile
from tkinter import filedialog as fd

class ProcessUI(QWidget):
      def __init__(self, type = '', method = ''):
        self.type = type
        self.method = method
        super(ProcessUI, self).__init__()
        loadUi("./screen_process.ui", self)

        #------------------------------------ Variables -----------------------------------------------
        self.arr = []
        self.plainText = ''
        self.cipherText = ''

        #------------------------------------ Functions -----------------------------------------------
        def setupAlgorithms():
            if(type == "Mã hoá"):
                match method:
                    case "Thay thế":
                        return ["Caesar", "Vignere", "Belasco", "Trithemius"]
                    case "Chuyển vị":
                        return ["Chuyển vị 1 dòng", "Chuyển vị nhiều dòng"]
                    case "XOR":
                        return ["XOR Caesar", "XOR Vignere", "XOR Belasco", "XOR Trithemius"]
                    case "DES":
                        return ["Des"]
            else:
                return ["1", "2", "3"]
            
        #------------------------------------ Update variables -----------------------------------------------
        self.arr = setupAlgorithms()
        self.picked_method = self.arr[0]

        #------------------------------------ Button các phương pháp ------------------------------------
        def onClickAlgorithm(text):
            self.picked_method = text
            self.label_main_title.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Mã hoá với {self.picked_method}</span></p></body></html>")
            
        for i in range (len(self.arr)):
            self.btn = QPushButton('{}'.format(self.arr[i]), self.frame_3)
            
            
            self.btn.setMinimumSize(QtCore.QSize(0, 50))
            self.btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            self.btn.setMouseTracking(False)
            self.btn.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
            self.btn.setAutoFillBackground(False)

            self.btn.setStyleSheet("QPushButton {\n"
            "    color: white;\n"
            "    background-color: #2a9d8f;\n"
            "    border-radius: 4px;\n"
            "    font-weight: 800;\n"
            "    font-size: 12px;\n"
            "}\n"
            "QPushButton::pressed {\n"
            "    background-color: #e76f51;\n"
            "}\n"
            "QPushButton:hover\n"
            "{\n"
            "   background-color: #e76f51;\n"
            "    opacity: 80%;\n"
            "}")
            
            # self.btn.setObjectName("btn")
            text = self.btn.text()
            self.btn.clicked.connect(lambda ch, text=text : onClickAlgorithm(text))
            self.algorithm_container.addWidget(self.btn)

            








        
