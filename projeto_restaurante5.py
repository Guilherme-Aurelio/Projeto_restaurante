# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'restaurante_oficial.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QStringListModel)
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
        self.tab.setStyleSheet(u"")
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
        self.desc_cad = QLineEdit(self.gridLayoutWidget)
        self.desc_cad.setObjectName(u"desc_cad")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.desc_cad.setFont(font2)

        self.gridLayout.addWidget(self.desc_cad, 1, 1, 1, 1)

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

        self.ok_cad = QPushButton(self.gridLayoutWidget)
        self.ok_cad.setObjectName(u"ok_cad")
        self.ok_cad.setFont(font3)

        self.gridLayout.addWidget(self.ok_cad, 3, 0, 1, 1)

        self.label_desc_cad = QLabel(self.gridLayoutWidget)
        self.label_desc_cad.setObjectName(u"label_desc_cad")
        self.label_desc_cad.setFont(font3)

        self.gridLayout.addWidget(self.label_desc_cad, 1, 0, 1, 1)

        self.valor_cad = QLineEdit(self.gridLayoutWidget)
        self.valor_cad.setObjectName(u"valor_cad")
        self.valor_cad.setFont(font2)

        self.gridLayout.addWidget(self.valor_cad, 2, 1, 1, 1)

        self.nome_cad = QLineEdit(self.gridLayoutWidget)
        self.nome_cad.setObjectName(u"nome_cad")
        self.nome_cad.setFont(font2)

        self.gridLayout.addWidget(self.nome_cad, 0, 1, 1, 1)

        self.cancelar_cad = QPushButton(self.gridLayoutWidget)
        self.cancelar_cad.setObjectName(u"cancelar_cad")
        self.cancelar_cad.setFont(font3)

        self.gridLayout.addWidget(self.cancelar_cad, 3, 1, 1, 1)

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
        self.ok_edi = QPushButton(self.gridLayoutWidget_2)
        self.ok_edi.setObjectName(u"ok_edi")
        self.ok_edi.setFont(font3)

        self.gridLayout_2.addWidget(self.ok_edi, 4, 0, 1, 1)

        self.comboBox_edi = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_edi.setObjectName(u"comboBox_edi")
        self.comboBox_edi.setEnabled(True)
        self.comboBox_edi.setFont(font2)
        self.comboBox_edi.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.comboBox_edi, 0, 0, 1, 2)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.cancelar_edi = QPushButton(self.gridLayoutWidget_2)
        self.cancelar_edi.setObjectName(u"cancelar_edi")
        self.cancelar_edi.setFont(font3)

        self.gridLayout_2.addWidget(self.cancelar_edi, 4, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.nome_edi = QLineEdit(self.gridLayoutWidget_2)
        self.nome_edi.setObjectName(u"nome_edi")
        self.nome_edi.setFont(font2)

        self.gridLayout_2.addWidget(self.nome_edi, 1, 1, 1, 1)

        self.valor_edi = QLineEdit(self.gridLayoutWidget_2)
        self.valor_edi.setObjectName(u"valor_edi")
        self.valor_edi.setFont(font2)

        self.gridLayout_2.addWidget(self.valor_edi, 3, 1, 1, 1)

        self.desc_edi = QLineEdit(self.gridLayoutWidget_2)
        self.desc_edi.setObjectName(u"desc_edi")
        self.desc_edi.setFont(font2)

        self.gridLayout_2.addWidget(self.desc_edi, 2, 1, 1, 1)

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
        self.ok_exc = QPushButton(self.gridLayoutWidget_3)
        self.ok_exc.setObjectName(u"ok_exc")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(11)
        self.ok_exc.setFont(font5)

        self.gridLayout_3.addWidget(self.ok_exc, 1, 0, 1, 1)

        self.cancelar_exc = QPushButton(self.gridLayoutWidget_3)
        self.cancelar_exc.setObjectName(u"cancelar_exc")
        self.cancelar_exc.setFont(font5)

        self.gridLayout_3.addWidget(self.cancelar_exc, 1, 1, 1, 1)

        self.comboBox_exc = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_exc.setObjectName(u"comboBox_exc")
        self.comboBox_exc.setFont(font3)

        self.gridLayout_3.addWidget(self.comboBox_exc, 0, 0, 1, 2)

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

        self.spinBox_card = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_card.setObjectName(u"spinBox_card")
        self.spinBox_card.setFont(font2)

        self.gridLayout_4.addWidget(self.spinBox_card, 0, 4, 1, 1)

        self.comboBox_card = QComboBox(self.gridLayoutWidget_4)
        self.comboBox_card.setObjectName(u"comboBox_card")
        self.comboBox_card.setFont(font2)

        self.gridLayout_4.addWidget(self.comboBox_card, 0, 2, 1, 2)

        self.listView_card = QListView(self.gridLayoutWidget_4)
        self.listView_card.setObjectName(u"listView_card")
        self.listView_card.setFont(font1)

        self.gridLayout_4.addWidget(self.listView_card, 1, 2, 1, 3)

        self.ok_card = QPushButton(self.gridLayoutWidget_4)
        self.ok_card.setObjectName(u"ok_card")
        self.ok_card.setFont(font5)

        self.gridLayout_4.addWidget(self.ok_card, 2, 3, 1, 1)

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
        self.finalizar_ped = QPushButton(self.gridLayoutWidget_5)
        self.finalizar_ped.setObjectName(u"finalizar_ped")
        self.finalizar_ped.setFont(font5)

        self.gridLayout_5.addWidget(self.finalizar_ped, 1, 0, 1, 2)

        self.cancelar_card = QPushButton(self.gridLayoutWidget_5)
        self.cancelar_card.setObjectName(u"cancelar_card")
        self.cancelar_card.setFont(font5)

        self.gridLayout_5.addWidget(self.cancelar_card, 1, 2, 1, 1)

        self.totalList = QListView(self.gridLayoutWidget_5)
        self.totalList.setObjectName(u"totalList")

        self.gridLayout_5.addWidget(self.totalList, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        '''
            Os atributos criados pelo grupo começam aqui 
        '''
        
        self.ok_cad.clicked.connect(self.exibirBoxEdicao)
        

        QMetaObject.connectSlotsByName(MainWindow)


    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_nome_cad.setText(QCoreApplication.translate("MainWindow", u"NOME:", None))
        self.label_valor_cad.setText(QCoreApplication.translate("MainWindow", u"VALOR:", None))
        self.ok_cad.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_desc_cad.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O:", None))
        self.cancelar_cad.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.cad_title.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE PRODUTOS/PRATOS", None))
        self.edicao_tit.setText(QCoreApplication.translate("MainWindow", u"EDI\u00c7\u00c3O DE PRODUTOS/PRATOS", None))
        self.ok_edi.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"NOME:", None))
        self.cancelar_edi.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VALOR:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O:", None))
        self.exclusao_tit.setText(QCoreApplication.translate("MainWindow", u"EXCLUS\u00c3O DE PRODUTOS/PRATOS", None))
        self.ok_exc.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.cancelar_exc.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"PRODUTO", None))
        self.cardapio_label.setText(QCoreApplication.translate("MainWindow", u"CARD\u00c1PIO", None))
        self.ok_card.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.finalizar_ped.setText(QCoreApplication.translate("MainWindow", u"FINALIZAR PEDIDO", None))
        self.cancelar_card.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"PEDIDO", None))
    # retranslateUi

    '''
        Os métodos criados pelo grupo começam a partir daqui 
    '''
    def exibirBoxEdicao(self):
        text = self.nome_cad.text()
        self.comboBox_edi.addItem(" ")
        self.comboBox_exc.addItem(" ")
        self.comboBox_card.addItem(" ")
        if text != "":
            
            items = [self.comboBox_edi.itemText(i) for i in range(self.comboBox_edi.count())]
            items = [self.comboBox_exc.itemText(i) for i in range(self.comboBox_edi.count())] 
            items = [self.comboBox_card.itemText(i) for i in range(self.comboBox_edi.count())] 
           
            if text not in items: 
                self.comboBox_edi.addItem(text)
                self.comboBox_exc.addItem(text)
                self.comboBox_card.addItem(text)
    
    
