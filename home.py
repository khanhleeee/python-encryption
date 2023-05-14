from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.uic import loadUi

import sys


from process import ProcessUI

class MainUI(QMainWindow):
      def openProcessWindow(self, type, method):
         self.type = type
         self.method = method
         self.w = ProcessUI(type, method)
         self.w.show()

      def __init__(self):
         super(MainUI, self).__init__()
         loadUi("./screen_home.ui", self)
         #------------------------------ Menu items ------------------------------
         # Ma hoa
         self.action_mh_thaythe.triggered.connect(self.chooseMahoaThayThe)
         self.action_mh_chuyenvi.triggered.connect(self.chooseMahoaChuyenVi)
         self.action_mh_xor.triggered.connect(self.chooseMahoaXOR)
         self.action_mh_des.triggered.connect(self.chooseMahoaDES)
         self.action_mh_rsa.triggered.connect(self.chooseMahoaRSA)


         # Giai hoa
         self.action_gm_thaythe.triggered.connect(self.chooseGiaiMaThayThe)
         self.action_gm_chuyenvi.triggered.connect(self.chooseGiaiMaChuyenVi)
         self.action_gm_xor.triggered.connect(self.chooseGiaiMaXOR)
         self.action_gm_des.triggered.connect(self.chooseGiaiMaDES)
         self.action_gm_rsa.triggered.connect(self.chooseGiaiMaRSA)


      #------------------------------ Functions choosing algorithm ------------------------------
      # Ma hoa
      def chooseMahoaThayThe(self):
         self.openProcessWindow("Mã hoá", "Thay thế")
      def chooseMahoaChuyenVi(self):
         self.openProcessWindow("Mã hoá", "Chuyển vị")
      def chooseMahoaXOR(self):
         self.openProcessWindow("Mã hoá", "XOR")
      def chooseMahoaDES(self):
         self.openProcessWindow("Mã hoá", "DES")
      def chooseMahoaRSA(self):
         self.openProcessWindow("Mã hoá", "RSA")

      # Giai hoa  
      def chooseGiaiMaThayThe(self):
         self.openProcessWindow("Giải mã", "Thay thế")
      def chooseGiaiMaChuyenVi(self):
         self.openProcessWindow("Giải mã", "Chuyển vị")
      def chooseGiaiMaXOR(self):
         self.openProcessWindow("Giải mã", "XOR")
      def chooseGiaiMaDES(self):
         self.openProcessWindow("Giải mã", "DES")
      def chooseGiaiMaRSA(self):
         self.openProcessWindow("Giải mã", "RSA")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainUI()
    w.show()
    app.exec()

