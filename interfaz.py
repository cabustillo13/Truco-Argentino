from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Envido - Truco Argentino")
        MainWindow.resize(840, 573)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.fondo = QtWidgets.QLabel(self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(0, 0, 840, 511))
        self.fondo.setText("")
        self.fondo.setPixmap(QtGui.QPixmap("./Resultados/portada.png"))
        self.fondo.setScaledContents(True)
        self.fondo.setObjectName("Fondo")
        
        self.botonComenzar = QtWidgets.QPushButton(self.centralwidget)
        self.botonComenzar.setGeometry(QtCore.QRect(20, 510, 411, 41))
        self.botonComenzar.setObjectName("Comenzar")
        
        self.botonEnvido = QtWidgets.QPushButton(self.centralwidget)
        self.botonEnvido.setGeometry(QtCore.QRect(430, 510, 391, 41))
        self.botonEnvido.setObjectName("Envido")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("Barra Menu")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("Estatus de la barra")
        
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.botonEnvido.clicked.connect(self.mostrarBotonEnvido)
        self.botonComenzar.clicked.connect(self.mostrarBotonComenzar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calcular Envido - TRUCO ARGENTINO"))
        self.botonComenzar.setText(_translate("MainWindow", "COMENZAR"))
        self.botonEnvido.setText(_translate("MainWindow", "ENVIDO"))

    def mostrarBotonEnvido(self):
        self.fondo.setPixmap(QtGui.QPixmap("Resultados/photo1.png"))

    def mostrarBotonComenzar(self):
        self.fondo.setPixmap(QtGui.QPixmap("Resultados/photo0.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_()) 
    
    
#Bibliografia: https://techwithtim.net/tutorials/pyqt5-tutorial/images/
