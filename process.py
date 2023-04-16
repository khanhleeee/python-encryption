
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QWidget, QPushButton, QFormLayout
from PyQt6.uic import loadUi

import sys

from tkinter import filedialog as fd

import file_funcs.DocFile as DocFile
import file_funcs.LuuFile as LuuFile
import run_algorithm

class ProcessUI(QWidget):
      def __init__(self, type = '', method = ''):
        self.type = type
        self.method = method
        super(ProcessUI, self).__init__()
        loadUi("./screen_process.ui", self)
        

        #------------------------------------ Variables -----------------------------------------------
        self.arr = []
        self.text = ''
        self.cipherText = ''
        self.key = ''
        self.fileName = ''

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
                match method:
                    case "Thay thế":
                        return ["Caesar", "Vignere", "Belasco", "Trithemius"]
                    case "Chuyển vị":
                        return ["Chuyển vị 1 dòng", "Chuyển vị nhiều dòng"]
                    case "XOR":
                        return ["XOR Caesar", "XOR Vignere", "XOR Belasco", "XOR Trithemius"]
                    case "DES":
                        return ["Des"]
            
        def readFile():
            filetypes = (('text files', '*.txt'),)
            
            filename = fd.askopenfilename(
                title='Open a file',
                initialdir='./texts',
                filetypes=filetypes
            )

            # Lưu đường dẫn và gọi phương thức đọc file
            self.file_path = filename
            if(self.file_path != ''):
                self.text = DocFile.DocFile(self.file_path)

            # Thêm nội dung gốc vào input
            self.textEdit.setText(''.join(self.text));
        
        def saveFile():
            self.cipherText= str(self.textEdit_2.toPlainText())
            self.fileName= str(self.input_fileName.toPlainText())

            result = LuuFile.GhiFile(self.cipherText, self.fileName)

       
        def runAlgorithm():
            self.key = str(self.input_key.toPlainText())
            self.text = str(self.textEdit.toPlainText())
            result = run_algorithm.Run(self.type, self.picked_algorithm, ''.join(self.text), self.key)

            self.textEdit_2.setText(result)
            # print(result)
        #------------------------------------ Update variables -----------------------------------------------
        self.arr = setupAlgorithms()
        self.picked_algorithm = self.arr[0]


        #------------------------------------ SET component ------------------------------------------------------------

        self.label_main_title.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">{self.type} với {self.picked_algorithm}</span></p></body></html>")

        self.btn_readFile.clicked.connect(readFile)

        self.process_btn.clicked.connect(runAlgorithm)

        self.btn_saveFile.clicked.connect(saveFile)

        #------------------------------------ Button các phương pháp ------------------------------------
        def onClickAlgorithm(text):
            self.picked_algorithm = text
            self.label_main_title.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">{self.type} với {self.picked_algorithm}</span></p></body></html>")
            
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

            








        

