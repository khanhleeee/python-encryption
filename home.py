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

         # Giai hoa
         self.action_gm_thaythe.triggered.connect(self.chooseGiaiMaThayThe)
         self.action_gm_chuyenvi.triggered.connect(self.chooseGiaiMaChuyenVi)
         self.action_gm_xor.triggered.connect(self.chooseGiaiMaXOR)
         self.action_gm_des.triggered.connect(self.chooseGiaiMaDES)

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

      # Giai hoa  
      def chooseGiaiMaThayThe(self):
         self.openProcessWindow("Giải hoá", "Thay thế")
      def chooseGiaiMaChuyenVi(self):
         self.openProcessWindow("Giải hoá", "Chuyển vị")
      def chooseGiaiMaXOR(self):
         self.openProcessWindow("Giải hoá", "XOR")
      def chooseGiaiMaDES(self):
         self.openProcessWindow("Giải hoá", "DES")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainUI()
    w.show()
    app.exec()
