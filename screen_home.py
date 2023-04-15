from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1157, 641)

        # Main frame
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
        "    color: white;    \n"
        "    background-color: #264653;\n"
        "}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Main container
        self.container = QtWidgets.QFrame(parent=self.centralwidget)
        self.container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.container.setObjectName("container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.container)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # App title
        self.app_title = QtWidgets.QLabel(parent=self.container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_title.sizePolicy().hasHeightForWidth())
        self.app_title.setSizePolicy(sizePolicy)
        self.app_title.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.app_title.setFont(font)
        self.app_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.app_title.setObjectName("app_title")
        self.verticalLayout_2.addWidget(self.app_title)

        # Content container
        self.container_content = QtWidgets.QFrame(parent=self.container)
        self.container_content.setMinimumSize(QtCore.QSize(0, 500))
        self.container_content.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.container_content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.container_content.setObjectName("container_content")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.container_content)
        self.verticalLayout_3.setContentsMargins(-1, 11, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Name container
        self.label_names = QtWidgets.QLabel(parent=self.container_content)
        self.label_names.setMinimumSize(QtCore.QSize(200, 40))
        self.label_names.setMaximumSize(QtCore.QSize(16777213, 39))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_names.setFont(font)
        self.label_names.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_names.setObjectName("label_names")
        self.verticalLayout_3.addWidget(self.label_names)

        # Name item
        self.label_mk = QtWidgets.QLabel(parent=self.container_content)
        self.label_mk.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_mk.setFont(font)
        self.label_mk.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_mk.setObjectName("label_mk")
        self.verticalLayout_3.addWidget(self.label_mk)
        self.label_nttn = QtWidgets.QLabel(parent=self.container_content)
        self.label_nttn.setMinimumSize(QtCore.QSize(200, 25))
        self.label_nttn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setItalic(False)
        self.label_nttn.setFont(font)
        self.label_nttn.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_nttn.setObjectName("label_nttn")
        self.verticalLayout_3.addWidget(self.label_nttn)
        self.label_nqt = QtWidgets.QLabel(parent=self.container_content)
        self.label_nqt.setMinimumSize(QtCore.QSize(200, 25))
        self.label_nqt.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(12)
        font.setItalic(False)
        self.label_nqt.setFont(font)
        self.label_nqt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_nqt.setObjectName("label_nqt")
        self.verticalLayout_3.addWidget(self.label_nqt)
        self.label_gvhd = QtWidgets.QLabel(parent=self.container_content)
        self.label_gvhd.setMinimumSize(QtCore.QSize(300, 60))
        self.label_gvhd.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_gvhd.setFont(font)
        self.label_gvhd.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_gvhd.setObjectName("label_gvhd")
        self.verticalLayout_3.addWidget(self.label_gvhd)
        self.verticalLayout_2.addWidget(self.container_content)
        self.verticalLayout.addWidget(self.container)
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu bar
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1157, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(parent=self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menu_mahoa = QtWidgets.QMenu(parent=self.menuMenu)
        self.menu_mahoa.setObjectName("menu_mahoa")
        self.menu_giaima = QtWidgets.QMenu(parent=self.menuMenu)
        self.menu_giaima.setObjectName("menu_giaima")
        
        MainWindow.setMenuBar(self.menubar)
        
        def onClick(action):
            print(action)
        
        
        self.action_mh_thaythe = QtGui.QAction(parent=MainWindow)
        self.action_mh_thaythe.setObjectName("action_mh_thaythe")
        self.action_mh_thaythe.triggered.connect()

        self.action_mh_chuyenvi = QtGui.QAction(parent=MainWindow)
        self.action_mh_chuyenvi.setObjectName("action_mh_chuyenvi")
        self.action_mh_thaythe.triggered.connect()

        self.action_mh_xor = QtGui.QAction(parent=MainWindow)
        self.action_mh_xor.setObjectName("action_mh_xor")
        self.action_mh_thaythe.triggered.connect()

        self.action_mh_des = QtGui.QAction(parent=MainWindow)
        self.action_mh_des.setObjectName("action_mh_des")
        self.action_mh_thaythe.triggered.connect()


        self.action_gm_thaythe = QtGui.QAction(parent=MainWindow)
        self.action_gm_thaythe.setObjectName("action_gm_thaythe")
        self.action_mh_thaythe.triggered.connect()


        self.action_gm_chuyenvi = QtGui.QAction(parent=MainWindow)
        self.action_gm_chuyenvi.setObjectName("action_gm_chuyenvi")
        self.action_mh_thaythe.triggered.connect()


        self.action_gm_xor = QtGui.QAction(parent=MainWindow)
        self.action_gm_xor.setObjectName("action_gm_xor")
        self.action_mh_thaythe.triggered.connect()


        self.action_gm_des = QtGui.QAction(parent=MainWindow)
        self.action_gm_des.setObjectName("action_gm_des")
        self.action_mh_thaythe.triggered.connect()


        self.menu_mahoa.addAction(self.action_mh_thaythe)
        self.menu_mahoa.addAction(self.action_mh_chuyenvi)
        self.menu_mahoa.addAction(self.action_mh_xor)
        self.menu_mahoa.addAction(self.action_mh_des)
        self.menu_giaima.addAction(self.action_gm_thaythe)
        self.menu_giaima.addAction(self.action_gm_chuyenvi)
        self.menu_giaima.addAction(self.action_gm_xor)
        self.menu_giaima.addAction(self.action_gm_des)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.menu_mahoa.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.menu_giaima.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.app_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#e76f51;\">ĐỀ TÀI: CÁC THUẬT TOÁN MÃ HÓA CỔ ĐIỂN</span></p></body></html>"))
        self.label_names.setText(_translate("MainWindow", "Tên thành viên nhóm:"))
        self.label_mk.setText(_translate("MainWindow", "Lê Mai Khánh"))
        self.label_nttn.setText(_translate("MainWindow", "Nguyễn Thị Tuyết Ngân"))
        self.label_nqt.setText(_translate("MainWindow", "Ngô Quốc Tứ"))
        self.label_gvhd.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic;\">GV hướng dẫn: TS. Phạm Đức Thành</span></p></body></html>"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menu_mahoa.setTitle(_translate("MainWindow", "Mã hóa"))
        self.menu_giaima.setTitle(_translate("MainWindow", "Giải mã"))
        self.action_mh_thaythe.setText(_translate("MainWindow", "Thay thế"))
        self.action_mh_chuyenvi.setText(_translate("MainWindow", "Chuyển vị"))
        self.action_mh_xor.setText(_translate("MainWindow", "Xor"))
        self.action_mh_des.setText(_translate("MainWindow", "Des"))
        self.action_gm_thaythe.setText(_translate("MainWindow", "Thay thế"))
        self.action_gm_chuyenvi.setText(_translate("MainWindow", "Chuyển vị"))
        self.action_gm_xor.setText(_translate("MainWindow", "Xor"))
        self.action_gm_des.setText(_translate("MainWindow", "Des"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
