
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QWidget, QPushButton, QFormLayout, QMessageBox
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
        self.privateKey = ''

        #------------------------------------ Functions -----------------------------------------------
        def setupAlgorithms():
            if(type == "Mã hoá"):
                match method:
                    case "Thay thế":
                        return ["Caesar", "Vignere", "Belasco", "Trithemius"]
                    case "Chuyển vị":
                        return ["Chuyển vị 2 dòng", "Chuyển vị nhiều dòng"]
                    case "XOR":
                        return ["XOR Caesar", "XOR Vignere", "XOR Belasco", "XOR Trithemius"]
                    case "DES":
                        return ["Des"]
                    case "Rsa":
                        return ["Rsa"]
            else:
                match method:
                    case "Thay thế":
                        return ["Caesar", "Vignere", "Belasco", "Trithemius"]
                    case "Chuyển vị":
                        return ["Chuyển vị 2 dòng", "Chuyển vị nhiều dòng"]
                    case "XOR":
                        return ["XOR Caesar", "XOR Vignere", "XOR Belasco", "XOR Trithemius"]
                    case "DES":
                        return ["Des"]
                    case "Rsa":
                        return ["Rsa"]
                    
            
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
                if(self.picked_algorithm == "Rsa" and type == "Giải mã"):
                    keyFilePath = self.file_path.split(".")
                    keyFilePath = '_PrivateKey.'.join(keyFilePath)
                    keyText = DocFile.DocFile(keyFilePath)

                    self.input_key.setText(''.join(keyText))

                self.text = DocFile.DocFile(self.file_path)

            # Thêm nội dung gốc vào input
            self.textEdit.setText(''.join(self.text));
        
        def saveFile():
            self.cipherText= str(self.textEdit_2.toPlainText())
            self.fileName= str(self.input_fileName.toPlainText())

            if(self.picked_algorithm == "Rsa"):
                n,d = self.privateKey
                LuuFile.GhiFile(self.cipherText, self.fileName, str(n) + '\n' + str(d))
            else:    
                LuuFile.GhiFile(self.cipherText, self.fileName)
            
        def showDialogSaveSuccess():
            msgBox = QMessageBox()
            msgBox.setText("Lưu file thành công.")
            msgBox.setWindowTitle("Thông báo")
            msgBox.setStyleSheet("QLabel {min-width: 300px; min-height: 70px;}")

            returnValue = msgBox.exec()
            if returnValue == QMessageBox.StandardButton.Ok:
                self.textEdit =  self.textEdit.setText('')
                self.input_key = self.input_key.setText('')
                self.textEdit_2 = self.textEdit_2.setText('')
                self.input_fileName = self.input_fileName.setText('')
            
    
        def runAlgorithm():
                self.key = str(self.input_key.toPlainText())
                self.text = str(self.textEdit.toPlainText())
                self.textEdit_2.setText('')

                result = run_algorithm.Run(self.type, self.picked_algorithm, ''.join(self.text), self.key)

                if(self.picked_algorithm == "Rsa" and type == "Mã hoá"):
                    C, n, d = result
                    self.privateKey = n,d
                    result = C

                self.textEdit_2.setText(result)
        #------------------------------------ Update variables -----------------------------------------------
        self.arr = setupAlgorithms()
        self.picked_algorithm = self.arr[0]

        if(self.picked_algorithm == "Trithemius" or self.picked_algorithm == "Chuyển vị 2 dòng"):
            self.input_key.setHidden(True)
            self.label_key.setHidden(True)
        elif (self.picked_algorithm == "Rsa"):
            if(type == "Mã hoá"):
                self.input_key.setHidden(True)
                self.label_key.setHidden(True)
            else:
                self.input_key.setHidden(False)
                self.label_key.setHidden(False)
                self.label_key.setText('Nhập private key: ')
        else:
            self.input_key.setHidden(False)   
            self.label_key.setHidden(False)   

        #------------------------------------ SET component ------------------------------------------------------------

        self.label_main_title.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">{self.type} với {self.picked_algorithm}</span></p></body></html>")

        self.btn_readFile.clicked.connect(readFile)

        self.process_btn.clicked.connect(runAlgorithm)

        self.btn_saveFile.clicked.connect(saveFile)

        self.btn_saveFile.clicked.connect(showDialogSaveSuccess)

        #------------------------------------ Button các phương pháp ------------------------------------
        def onClickAlgorithm(text):
            self.picked_algorithm = text
            self.label_main_title.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">{self.type} với {self.picked_algorithm}</span></p></body></html>")
            self.textEdit_2.setText('');

            if(self.picked_algorithm == "Trithemius" or self.picked_algorithm == "Chuyển vị 2 dòng"):
                self.input_key.setHidden(True)
                self.label_key.setHidden(True)
            else:
                self.input_key.setHidden(False)   
                self.label_key.setHidden(False)      

          
            
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
            
            text = self.btn.text()
            self.btn.clicked.connect(lambda ch, text=text : onClickAlgorithm(text))
            self.algorithm_container.addWidget(self.btn)

            








        

