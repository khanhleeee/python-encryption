from PyQt6 import QtCore, QtGui, QtWidgets

import file_funcs.DocFile as DocFile
from tkinter import filedialog as fd


class Process_UI(object):
    
    def setupUi(self, Form, type = "Mã hoá", method = "Thay thế"):
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
                self.plainText = DocFile.DocFile(self.file_path)

            # Thêm nội dung gốc vào input
            self.textEdit.setText(''.join(self.plainText));

        #------------------------------------ Update variables -----------------------------------------------
        self.arr = setupAlgorithms()
        self.picked_method = self.arr[0]
        
        #------------------------------------ Main page form ------------------------------------------
        Form.setObjectName("Form")
        Form.resize(1004, 740)
        Form.setStyleSheet("QWidget {\n"
        "    color: white;\n"
        "    background-color: #264653;\n"
        "    font: 75 14px \"\";\n"
        "    font: 63 8pt \"Montserrat\";\n"
        "}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.QFrame = QtWidgets.QFrame(parent=Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QFrame.sizePolicy().hasHeightForWidth())

        #------------------------------------ Nav frame ------------------------------------------------
        self.QFrame.setSizePolicy(sizePolicy)
        self.QFrame.setMinimumSize(QtCore.QSize(300, 0))
        self.QFrame.setMaximumSize(QtCore.QSize(330, 16777215))
        self.QFrame.setStyleSheet("")
        self.QFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.QFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.QFrame.setObjectName("QFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.QFrame)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(14, 0, 14, -1)
        self.verticalLayout.setObjectName("verticalLayout")

        #------------------------------------ Frame of nav items ---------------------------------------
        self.frame_3 = QtWidgets.QFrame(parent=self.QFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(167, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 800))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayout = QtWidgets.QFormLayout(self.frame_3)
        self.formLayout.setContentsMargins(0, 10, 0, -1)
        self.formLayout.setObjectName("formLayout")

        #------------------------------------ Label "Các phương pháp" ------------------------------------
        self.label_nav= QtWidgets.QLabel(parent=self.frame_3)
        self.label_nav.setMinimumSize(QtCore.QSize(300, 70))
        self.label_nav.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_nav.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_nav.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_nav)

        #------------------------------------ Button các phương pháp ------------------------------------
        def onClickAlgorithm(text):
            self.picked_method = text
            self.label_main_title.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Mã hoá với {self.picked_method}</span></p></body></html>")
            
        for i in range (len(self.arr)):
            self.btn = QtWidgets.QPushButton('{}'.format(self.arr[i]), self.frame_3)
            
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
            
            self.btn.setObjectName("btn")
            text = self.btn.text()
            self.btn.clicked.connect(lambda ch, text=text : onClickAlgorithm(text))
            self.formLayout.setWidget(i + 1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.btn)

        self.verticalLayout.addWidget(self.frame_3)

        #------------------------------------ Back home button ----------------------------------------------------------
        self.backhome_btn = QtWidgets.QPushButton(parent=self.QFrame)
        self.backhome_btn.setStyleSheet("QPushButton {\n"
        "    background-color: transparent;\n"
        "    font: 75 8pt \"Rubik\";\n"
        "}\n"
        "\n"
        "QPushButton::hover {\n"
        "    font-weight: 600;\n"
        "}")
        
        self.backhome_btn.setObjectName("backhome_btn")
        self.verticalLayout.addWidget(self.backhome_btn, 0, QtCore.Qt.AlignmentFlag.AlignLeft)

        #------------------------------------ Main frame for encryption / decryption ------------------------------------
        self.gridLayout.addWidget(self.QFrame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(parent=Form)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        #------------------------------------ Label "Giải mã/ Mã hoá bằng phương pháp"------------------------------------
        self.label_main_title = QtWidgets.QLabel(parent=self.frame_2)
        self.label_main_title.setMaximumSize(QtCore.QSize(16777215, 60))
        self.label_main_title.setMinimumSize(QtCore.QSize(16777215, 60))
        self.label_main_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_main_title.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_main_title)

        
        self.widget = QtWidgets.QWidget(parent=self.frame_2)
        self.widget.setMinimumSize(QtCore.QSize(0, 30))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #------------------------------------ Label "Nội dung gốc" ----------------------------------------------------------
        self.label_origin = QtWidgets.QLabel(parent=self.widget)
        self.label_origin.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_origin)

        #------------------------------------ Button đọc file ---------------------------------------------------------------
        self.btn_readFile = QtWidgets.QPushButton(parent=self.widget)
        self.btn_readFile.setMinimumSize(QtCore.QSize(120, 30))
        self.btn_readFile.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btn_readFile.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_readFile.setStyleSheet("QPushButton {\n"
        "    color: white;\n"
        "    background-color: #2a9d8f;\n"
        "    border-radius: 4px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    opacity: 0.8;\n"
        "}")

        self.btn_readFile.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.btn_readFile)
        self.verticalLayout_2.addWidget(self.widget)
        self.btn_readFile.clicked.connect(readFile)

        #------------------------------------ Text edit noi dung goc ----------------------------------------------------------
        self.textEdit = QtWidgets.QTextEdit(parent=self.frame_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.widget_3 = QtWidgets.QWidget(parent=self.frame_2)
        self.widget_3.setMinimumSize(QtCore.QSize(120, 40))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget_3.setStyleSheet("\n" "Qt::AlignHCenter")
        self.widget_3.setObjectName("widget_3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget_3)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.formLayout_2.setObjectName("formLayout_2")

        #------------------------------------ Key label ------------------------------------------------------------------------
        self.label_key = QtWidgets.QLabel(parent=self.widget_3)
        self.label_key.setStyleSheet("QLabel {\n"
        "    margin-right: 8px;\n"
        "}")
        self.label_key.setObjectName("label_key")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_key)

        #------------------------------------ Key input ------------------------------------------------------------------------
        self.input_key = QtWidgets.QTextEdit(parent=self.widget_3)
        self.input_key.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignCenter)
        self.input_key.setMaximumSize(QtCore.QSize(140, 29))
        self.input_key.setObjectName("input_key")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.input_key)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(parent=self.frame_2)
        self.widget_2.setMinimumSize(QtCore.QSize(120, 30))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        

        #------------------------------------ Label "Nội dung sau khi xử lý" -----------------------------------------------------
        self.label_processed = QtWidgets.QLabel(parent=self.widget_2)
        self.label_processed.setObjectName("label_processed")
        self.horizontalLayout_3.addWidget(self.label_processed)

        #------------------------------------ Text edit nội dung sau khi xử lý ----------------------------------------------------
        self.verticalLayout_2.addWidget(self.widget_2)
        self.input_processed = QtWidgets.QTextEdit(parent=self.frame_2)
        self.input_processed.setObjectName("input_processed")

        self.verticalLayout_2.addWidget(self.input_processed)
        self.widget_4 = QtWidgets.QWidget(parent=self.frame_2)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_4.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.widget_4.setObjectName("widget_4")
        self.formLayout_3 = QtWidgets.QFormLayout(self.widget_4)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.formLayout_3.setContentsMargins(0, -1, 0, -1)
        self.formLayout_3.setObjectName("formLayout_3")
        
        self.btn_saveFile = QtWidgets.QPushButton(parent=self.widget_4)
        self.btn_saveFile.setMinimumSize(QtCore.QSize(120, 30))
        self.btn_saveFile.setMaximumSize(QtCore.QSize(120, 16777215))
        self.btn_saveFile.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_saveFile.setStyleSheet("QPushButton {\n"
        "    color: white;\n"
        "    background-color: #2a9d8f;\n"
        "    border-radius: 4px;\n"
        "    margin-bottom: 2px;\n"
        "}\n"
        "QPushButton:hover {\n"
        "    opacity: 0.8;\n"
        "}")
        self.btn_saveFile.setObjectName("pushButton_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.btn_saveFile)
        
        self.input_fileName = QtWidgets.QTextEdit(parent=self.widget_4)
        self.input_fileName.setMaximumSize(QtCore.QSize(200, 16777215))
        self.input_fileName.setObjectName("textEdit_4")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.input_fileName)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_nav.setText(_translate("Form", f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Các thuật toán</span></p></body></html>"))

        self.backhome_btn.setText(_translate("Form", "<  Trở về trang chủ"))
        
        self.label_main_title.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Mã hoá với {self.picked_method}</span></p></body></html>")
        self.label_origin.setText(_translate("Form", "Nội dung gốc"))
        self.btn_readFile.setText(_translate("Form", "Đọc file"))
        self.label_key.setText(_translate("Form", "Key"))
        self.label_processed.setText(_translate("Form", "Nội dung sau khi xử lý"))
        self.btn_saveFile.setText(_translate("Form", "Lưu file"))
        self.input_fileName.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Montserrat\'; font-size:8pt; font-weight:56; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#dddddd;\">result.txt</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Process_UI()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
