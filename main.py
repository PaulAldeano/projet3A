################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

# GUI FILE
from new_int import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_toggle.clicked.connect(lambda: UIfunctions.toggleMenu(self, 250, True))
        self.ui.Btn_import.clicked.connect(lambda: UIfunctions.importfile(self))

        ## PAGES
        ########################################################################

        # PAGE ML
        self.ui.Btn_ML.clicked.connect(lambda: self.ui.Pages_widget.setCurrentWidget(self.ui.Learning))

        # PAGE Linear Reg
        self.ui.Btn_linear.clicked.connect(lambda: self.ui.Pages_widget.setCurrentWidget(self.ui.Linear_reg))
        self.ui.plot_linearreg.clicked.connect(
            lambda: UIfunctions.linearreg(
                self,self.ui.label_file_path.text(),
                self.ui.x_axis_linear.value(),
                self.ui.y_ord_linear.value()))

        # PAGE Kmeans
        self.ui.Btn_kmeans.clicked.connect(lambda: self.ui.Pages_widget.setCurrentWidget(self.ui.kmeans_cluster))
        self.ui.Btn_cluster_kmeans.clicked.connect(lambda: UIfunctions.kmeans(
            self,
            self.ui.label_file_path.text(),
            self.ui.cluster_number.value()
        ))
        self.ui.Btn_elbow_plot.clicked.connect(lambda : UIfunctions.elbow_met(
            self,
            self.ui.label_file_path.text(),
            self.ui.cluster_max.value()
        ))

        # PAGE Polynomial
        self.ui.Btn_poly_reg.clicked.connect(lambda: self.ui.Pages_widget.setCurrentWidget(self.ui.polynomial_reg))
        self.ui.plot_polynomial.clicked.connect(
            lambda: UIfunctions.polynomialreg(
                self,
                self.ui.label_file_path.text(),
                self.ui.degree_polynomial.value(),
                self.ui.x_axis_linear_poly.value(),
                self.ui.y_ord_linear_poly.value()))
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())