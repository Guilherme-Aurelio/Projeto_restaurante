# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow1.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QListView, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 550)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 0, 680, 500))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setMaximumSize(QSize(700, 550))
        self.tab.setAutoFillBackground(False)
        self.tab.setStyleSheet(u"background-color: rgb(196, 220, 255);")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 30, 315, 205))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 40, 261, 141))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.lineEdit_2.setFont(font2)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_nome_cad = QLabel(self.gridLayoutWidget)
        self.label_nome_cad.setObjectName(u"label_nome_cad")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        self.label_nome_cad.setFont(font3)

        self.gridLayout.addWidget(self.label_nome_cad, 0, 0, 1, 1)

        self.label_valor_cad = QLabel(self.gridLayoutWidget)
        self.label_valor_cad.setObjectName(u"label_valor_cad")
        self.label_valor_cad.setFont(font3)

        self.gridLayout.addWidget(self.label_valor_cad, 2, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font3)

        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)

        self.label_desc_cad = QLabel(self.gridLayoutWidget)
        self.label_desc_cad.setObjectName(u"label_desc_cad")
        self.label_desc_cad.setFont(font3)

        self.gridLayout.addWidget(self.label_desc_cad, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font2)

        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font2)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font3)

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.cad_title = QLabel(self.frame)
        self.cad_title.setObjectName(u"cad_title")
        self.cad_title.setGeometry(QRect(20, 10, 281, 21))
        self.cad_title.setFont(font1)
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(340, 30, 315, 205))
        self.frame_2.setFont(font3)
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.edicao_tit = QLabel(self.frame_2)
        self.edicao_tit.setObjectName(u"edicao_tit")
        self.edicao_tit.setGeometry(QRect(30, 10, 251, 21))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.edicao_tit.setFont(font4)
        self.gridLayoutWidget_2 = QWidget(self.frame_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(30, 40, 251, 151))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font3)

        self.gridLayout_2.addWidget(self.pushButton_3, 4, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        self.comboBox.setFont(font2)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.comboBox, 0, 0, 1, 2)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font3)

        self.gridLayout_2.addWidget(self.pushButton_4, 4, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font2)

        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setFont(font2)

        self.gridLayout_2.addWidget(self.lineEdit_6, 3, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font2)

        self.gridLayout_2.addWidget(self.lineEdit_5, 2, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(180, 250, 301, 181))
        self.frame_3.setFont(font1)
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.exclusao_tit = QLabel(self.frame_3)
        self.exclusao_tit.setObjectName(u"exclusao_tit")
        self.exclusao_tit.setGeometry(QRect(10, 20, 281, 16))
        self.exclusao_tit.setFont(font1)
        self.gridLayoutWidget_3 = QWidget(self.frame_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(30, 50, 241, 101))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(11)
        self.pushButton_5.setFont(font5)

        self.gridLayout_3.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font5)

        self.gridLayout_3.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font3)

        self.gridLayout_3.addWidget(self.comboBox_2, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_5 = QFrame(self.tab_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(160, 10, 321, 241))
        self.frame_5.setFont(font1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.cardapio_label = QLabel(self.frame_5)
        self.cardapio_label.setObjectName(u"cardapio_label")
        self.cardapio_label.setGeometry(QRect(120, 10, 101, 31))
        self.cardapio_label.setFont(font1)
        self.gridLayoutWidget_4 = QWidget(self.frame_5)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(-10, 50, 321, 182))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.spinBox = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setFont(font2)

        self.gridLayout_4.addWidget(self.spinBox, 0, 4, 1, 1)

        self.comboBox_3 = QComboBox(self.gridLayoutWidget_4)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setFont(font2)

        self.gridLayout_4.addWidget(self.comboBox_3, 0, 2, 1, 2)

        self.listView = QListView(self.gridLayoutWidget_4)
        self.listView.setObjectName(u"listView")
        self.listView.setFont(font1)

        self.gridLayout_4.addWidget(self.listView, 1, 2, 1, 3)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font5)

        self.gridLayout_4.addWidget(self.pushButton_7, 2, 3, 1, 1)

        self.frame_6 = QFrame(self.tab_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(145, 250, 341, 211))
        self.frame_6.setFont(font1)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_5 = QWidget(self.frame_6)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(20, 40, 301, 141))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.gridLayoutWidget_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font5)

        self.gridLayout_5.addWidget(self.pushButton_8, 1, 0, 1, 2)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font5)

        self.gridLayout_5.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.listView_2 = QListView(self.gridLayoutWidget_5)
        self.listView_2.setObjectName(u"listView_2")

        self.gridLayout_5.addWidget(self.listView_2, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_nome_cad.setText(QCoreApplication.translate("MainWindow", u"NOME:", None))
        self.label_valor_cad.setText(QCoreApplication.translate("MainWindow", u"VALOR:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_desc_cad.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.cad_title.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE PRODUTOS/PRATOS", None))
        self.edicao_tit.setText(QCoreApplication.translate("MainWindow", u"EDI\u00c7\u00c3O DE PRODUTOS/PRATOS", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"NOME:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VALOR:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O:", None))
        self.exclusao_tit.setText(QCoreApplication.translate("MainWindow", u"EXCLUS\u00c3O DE PRODUTOS/PRATOS", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"PRODUTO", None))
        self.cardapio_label.setText(QCoreApplication.translate("MainWindow", u"CARD\u00c1PIO", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"FINALIZAR PEDIDO", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"PEDIDO", None))
    # retranslateUi

