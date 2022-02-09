## ==> GUI FILE

from main import *
from ml_engine import *
from kmeans import *


class UIfunctions(MainWindow):
    def toggleMenu(self,maxWidth,enable):
        if enable:

            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 100

            # SET MAX WIDTH
            if width == 100:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def importfile(self):
        file = QFileDialog.getOpenFileName(
            parent=self,
            caption="Select a file"
        )
        self.ui.label_file_path.setText(file[0])

    def linearreg(self,path,X,Y):
        if path[-3:] == "csv":
            linearreg_csv(path,X,Y)
        if path[-3:] == "txt":
            linear_regression(path,X,Y)

    def polynomialreg(self,path,n,X,Y):
        if path[-3:] == "csv":
            polynomial_reg_csv(path,n,X,Y)
        if path[-3:] == "txt":
            polynomial_regression(path,n,X,Y)
    
    def kmeans(self,path,clust_num):
        kmeans_func(path,clust_num)
    
    def elbow_met(self,path,range):
        elbow_method(path,range)