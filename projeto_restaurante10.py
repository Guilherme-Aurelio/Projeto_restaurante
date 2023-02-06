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
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QWidget, QMessageBox)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 616)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(110, 40, 681, 520))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setMaximumSize(QSize(700, 550))
        self.tab.setAutoFillBackground(False)
        self.tab.setStyleSheet(u"")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 50, 315, 205))
        self.frame.setFont(font)
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
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        self.desc_cad.setFont(font1)

        self.gridLayout.addWidget(self.desc_cad, 1, 1, 1, 1)

        self.label_nome_cad = QLabel(self.gridLayoutWidget)
        self.label_nome_cad.setObjectName(u"label_nome_cad")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        self.label_nome_cad.setFont(font2)

        self.gridLayout.addWidget(self.label_nome_cad, 0, 0, 1, 1)

        self.label_valor_cad = QLabel(self.gridLayoutWidget)
        self.label_valor_cad.setObjectName(u"label_valor_cad")
        self.label_valor_cad.setFont(font2)

        self.gridLayout.addWidget(self.label_valor_cad, 2, 0, 1, 1)

        self.ok_cad = QPushButton(self.gridLayoutWidget)
        self.ok_cad.setObjectName(u"ok_cad")
        self.ok_cad.setFont(font2)

        self.gridLayout.addWidget(self.ok_cad, 3, 0, 1, 1)

        self.label_desc_cad = QLabel(self.gridLayoutWidget)
        self.label_desc_cad.setObjectName(u"label_desc_cad")
        self.label_desc_cad.setFont(font2)

        self.gridLayout.addWidget(self.label_desc_cad, 1, 0, 1, 1)

        self.valor_cad = QLineEdit(self.gridLayoutWidget)
        self.valor_cad.setObjectName(u"valor_cad")
        self.valor_cad.setFont(font1)

        self.gridLayout.addWidget(self.valor_cad, 2, 1, 1, 1)

        self.nome_cad = QLineEdit(self.gridLayoutWidget)
        self.nome_cad.setObjectName(u"nome_cad")
        self.nome_cad.setFont(font1)

        self.gridLayout.addWidget(self.nome_cad, 0, 1, 1, 1)

        self.cancelar_cad = QPushButton(self.gridLayoutWidget)
        self.cancelar_cad.setObjectName(u"cancelar_cad")
        self.cancelar_cad.setFont(font2)

        self.gridLayout.addWidget(self.cancelar_cad, 3, 1, 1, 1)

        self.cad_title = QLabel(self.frame)
        self.cad_title.setObjectName(u"cad_title")
        self.cad_title.setGeometry(QRect(20, 10, 281, 21))
        self.cad_title.setFont(font)
        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(340, 50, 315, 205))
        self.frame_2.setFont(font2)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.edicao_tit = QLabel(self.frame_2)
        self.edicao_tit.setObjectName(u"edicao_tit")
        self.edicao_tit.setGeometry(QRect(30, 10, 251, 21))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.edicao_tit.setFont(font3)
        self.gridLayoutWidget_2 = QWidget(self.frame_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(30, 40, 251, 151))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ok_edi = QPushButton(self.gridLayoutWidget_2)
        self.ok_edi.setObjectName(u"ok_edi")
        self.ok_edi.setFont(font2)

        self.gridLayout_2.addWidget(self.ok_edi, 4, 0, 1, 1)

        self.comboBox_edi = QComboBox(self.gridLayoutWidget_2)
        self.comboBox_edi.setObjectName(u"comboBox_edi")
        self.comboBox_edi.setEnabled(True)
        self.comboBox_edi.setFont(font1)
        self.comboBox_edi.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.comboBox_edi, 0, 0, 1, 2)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.cancelar_edi = QPushButton(self.gridLayoutWidget_2)
        self.cancelar_edi.setObjectName(u"cancelar_edi")
        self.cancelar_edi.setFont(font2)

        self.gridLayout_2.addWidget(self.cancelar_edi, 4, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.nome_edi = QLineEdit(self.gridLayoutWidget_2)
        self.nome_edi.setObjectName(u"nome_edi")
        self.nome_edi.setFont(font1)

        self.gridLayout_2.addWidget(self.nome_edi, 1, 1, 1, 1)

        self.valor_edi = QLineEdit(self.gridLayoutWidget_2)
        self.valor_edi.setObjectName(u"valor_edi")
        self.valor_edi.setFont(font1)

        self.gridLayout_2.addWidget(self.valor_edi, 3, 1, 1, 1)

        self.desc_edi = QLineEdit(self.gridLayoutWidget_2)
        self.desc_edi.setObjectName(u"desc_edi")
        self.desc_edi.setFont(font1)

        self.gridLayout_2.addWidget(self.desc_edi, 2, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(180, 280, 301, 181))
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.exclusao_tit = QLabel(self.frame_3)
        self.exclusao_tit.setObjectName(u"exclusao_tit")
        self.exclusao_tit.setGeometry(QRect(10, 20, 281, 16))
        self.exclusao_tit.setFont(font)
        self.gridLayoutWidget_3 = QWidget(self.frame_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(30, 50, 241, 101))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ok_exc = QPushButton(self.gridLayoutWidget_3)
        self.ok_exc.setObjectName(u"ok_exc")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        self.ok_exc.setFont(font4)

        self.gridLayout_3.addWidget(self.ok_exc, 1, 0, 1, 1)

        self.cancelar_exc = QPushButton(self.gridLayoutWidget_3)
        self.cancelar_exc.setObjectName(u"cancelar_exc")
        self.cancelar_exc.setFont(font4)

        self.gridLayout_3.addWidget(self.cancelar_exc, 1, 1, 1, 1)

        self.comboBox_exc = QComboBox(self.gridLayoutWidget_3)
        self.comboBox_exc.setObjectName(u"comboBox_exc")
        self.comboBox_exc.setFont(font2)

        self.gridLayout_3.addWidget(self.comboBox_exc, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_5 = QFrame(self.tab_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(160, 0, 321, 241))
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.cardapio_label = QLabel(self.frame_5)
        self.cardapio_label.setObjectName(u"cardapio_label")
        self.cardapio_label.setGeometry(QRect(120, 10, 101, 31))
        self.cardapio_label.setFont(font)
        self.gridLayoutWidget_4 = QWidget(self.frame_5)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(-10, 50, 321, 182))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.comboBox_card = QComboBox(self.gridLayoutWidget_4)
        self.comboBox_card.setObjectName(u"comboBox_card")
        self.comboBox_card.setFont(font1)

        self.gridLayout_4.addWidget(self.comboBox_card, 0, 2, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.label_desc_card = QLabel(self.gridLayoutWidget_4)
        self.label_desc_card.setObjectName(u"label_desc_card")
        self.label_desc_card.setFont(font4)
        self.label_desc_card.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_desc_card.setFrameShape(QFrame.Box)
        self.label_desc_card.setFrameShadow(QFrame.Sunken)
        self.label_desc_card.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_desc_card, 1, 2, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.spinBox_card = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_card.setObjectName(u"spinBox_card")
        self.spinBox_card.setFont(font1)

        self.gridLayout_4.addWidget(self.spinBox_card, 0, 5, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 1, 1, 1)

        self.label_valor_card = QLabel(self.gridLayoutWidget_4)
        self.label_valor_card.setObjectName(u"label_valor_card")
        self.label_valor_card.setFont(font4)
        self.label_valor_card.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_valor_card.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_valor_card, 0, 4, 1, 1)

        self.ok_card = QPushButton(self.gridLayoutWidget_4)
        self.ok_card.setObjectName(u"ok_card")
        self.ok_card.setFont(font4)

        self.gridLayout_4.addWidget(self.ok_card, 2, 3, 1, 2)

        self.frame_6 = QFrame(self.tab_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(145, 230, 341, 241))
        self.frame_6.setFont(font)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_5 = QWidget(self.frame_6)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(20, 40, 301, 191))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.cancelar_card = QPushButton(self.gridLayoutWidget_5)
        self.cancelar_card.setObjectName(u"cancelar_card")
        self.cancelar_card.setFont(font4)

        self.gridLayout_5.addWidget(self.cancelar_card, 2, 2, 1, 1)

        self.finalizar_ped = QPushButton(self.gridLayoutWidget_5)
        self.finalizar_ped.setObjectName(u"finalizar_ped")
        self.finalizar_ped.setFont(font4)

        self.gridLayout_5.addWidget(self.finalizar_ped, 2, 0, 1, 2)

        self.label_VTotal = QLabel(self.gridLayoutWidget_5)
        self.label_VTotal.setObjectName(u"label_VTotal")
        self.label_VTotal.setMaximumSize(QSize(16777215, 15))
        self.label_VTotal.setFont(font4)
        self.label_VTotal.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_VTotal, 1, 0, 1, 3)

        self.label_nota = QLabel(self.gridLayoutWidget_5)
        self.label_nota.setObjectName(u"label_nota")
        self.label_nota.setFont(font2)
        self.label_nota.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_nota.setFrameShape(QFrame.Box)
        self.label_nota.setFrameShadow(QFrame.Sunken)
        self.label_nota.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_nota, 0, 0, 1, 3)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        '''
            Os atributos criados pelo grupo começam aqui 
        '''
        self.comboBox_edi.addItem(" ")
        self.comboBox_exc.addItem(" ")
        self.comboBox_card.addItem(" ")
        self.ok_cad.clicked.connect(self.showCBoxs)
        self.ok_exc.clicked.connect(self.removeProduto)
        #self.ok_edi.clicked.connect(self.excluirProduto) rever a conexão. faz sentido isso????
        
        self.desc_cad.textChanged.connect(self.label_desc_card.setText)
        self.ok_cad.clicked.connect(self.addCBoxs)
        self.desc_dict = {} 
        self.valor_dict = {}        
        self.quant_dict = {}
        self.comboBox_card.currentTextChanged.connect(self.updateLabelDescricao)
        self.ok_cad.clicked.connect(self.showMessageCad)
        self.ok_exc.clicked.connect(self.showMessageExc)
        self.ok_edi.clicked.connect(self.showMessageEdi)
        self.ok_card.clicked.connect(self.showNotaFiscal)
        self.ok_edi.clicked.connect(self.editCBoxs)
        self.cancelar_cad.clicked.connect(self.cancBotCad)
        self.cancelar_edi.clicked.connect(self.cancBotEdi)
        self.cancelar_card.clicked.connect(self.cancPedido)
        self.cancelar_exc.clicked.connect(self.cancBotExc)
        self.finalizar_ped.clicked.connect(self.showMessageFinPed)

        self.total = 0
        self.lista_total = []
        self.exibir_todos_ped = []
        self.exibir_todos_ped.append("QUANT       V UNIT       PROD       V TOT \n")
        #self.label_VTotal = 0

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
        self.label_desc_card.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O DO PRODUTO", None))
        self.label_valor_card.setText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.ok_card.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.cancelar_card.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.finalizar_ped.setText(QCoreApplication.translate("MainWindow", u"FINALIZAR PEDIDO", None))
        self.label_VTotal.setText(QCoreApplication.translate("MainWindow", u"TOTAL DA COMPRA", None))
        self.label_nota.setText(QCoreApplication.translate("MainWindow", u"NOTA", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"PEDIDO", None))
    # retranslateUi
    '''
        Os métodos criados pelo grupo começam a partir daqui 
    '''
    def showCBoxs(self):
        text = self.nome_cad.text()

        if text != "":
            items = [self.comboBox_edi.itemText(i) for i in range(self.comboBox_edi.count())]
            items = [self.comboBox_exc.itemText(i) for i in range(self.comboBox_edi.count())] 
            items = [self.comboBox_card.itemText(i) for i in range(self.comboBox_edi.count())] 
            
            if text not in items: 
                self.comboBox_edi.addItem(text)
                self.comboBox_exc.addItem(text)
                self.comboBox_card.addItem(text)


    def removeProduto(self):
        #for i in range(len(self.comboBox_edi)):
        '''texto_combo = self.comboBox_exc.text()
        index = self.comboBox_edi.findText(texto_combo)
        self.comboBox_edi.removeItem(index)'''

        current_index_cb_exc = self.comboBox_exc.currentIndex()
        current_index_cb_edi = current_index_cb_exc
        current_index_cb_card = current_index_cb_exc
        print(current_index_cb_exc)
        self.comboBox_edi.removeItem(current_index_cb_edi)
        self.comboBox_exc.removeItem(current_index_cb_exc)
        self.comboBox_card.removeItem(current_index_cb_card)
        self.comboBox_exc.setCurrentIndex(0)
        

    def addCBoxs(self):
        # Get text from desc_cad
        desc = self.desc_cad.text()
        nome = self.nome_cad.text()
        valor = self.valor_cad.text()

        # Add text to combo
        # self.comboBox_card.addItem(text)
 
        self.desc_dict[nome] = desc
        self.valor_dict[nome] = valor

        print(self.desc_dict)
        print(self.valor_dict)
        # Clear desc_cad
        self.desc_cad.clear()
        self.nome_cad.clear()
        self.valor_cad.clear()
        # Connect combo currentTextChanged signal to slot


    def updateLabelDescricao(self):
        # Set label_card text to combo current text
        nome = self.comboBox_card.currentText()
        desc = self.desc_dict.get(nome)
        valor = self.valor_dict.get(nome)
        self.label_desc_card.setText(desc)
        self.label_valor_card.setText(valor)
        #self.label_card.setText(self.desc_cad.text())
        #desc = self.desc_dict[index]
        #self.label_card.setText(index)
        #self.label_card.setText(desc)

        
    def showMessageCad(self):
        message_box = QMessageBox()
        message_box.setText("Cadastro realizado.")
        message_box.exec_()
        
        
    def showMessageExc(self):
        message_box = QMessageBox()
        message_box.setText("Excluido com sucesso!")
        message_box.exec_()

    def showMessageEdi(self):
        message_box = QMessageBox()
        message_box.setText("Editado com sucesso!")
        message_box.exec_()
        
    
    def showNotaFiscal(self):
        exibir = []
        
        
        nome = self.comboBox_card.currentText()
        quant = self.spinBox_card.value()
        valor = self.valor_dict.get(nome)
        descricao = self.desc_dict[nome]
        #quant = self.quant_dict.get(nome)

        
        #self.quant_dict[nome] = quant

        if valor != '':
            valor = float(valor)
            multiplicacao = valor * quant
            self.total+=multiplicacao
            #multiplicacao_texto = str(multiplicacao)
            #resultado = self.label_nota.text(self.multiplicacao_texto)
            valor = str(valor)

        else:
            print("Valor inválido")

        #valor_string = str(valor)
        
        quant_string = str(quant)
        #quantidade_texto = self.label_nota.setText(quant)
        exibir.append(quant_string)
        exibir.append(valor)
        #exibir.append(' ')
        exibir.append(nome)
        #exibir.append(' ')
        exibir.append(descricao)
        #exibir.append(' ')
        #exibir.append(valor_string)
        #exibir.append(" ")
        exibir.append(str(multiplicacao))     

        print(exibir)

        lista = "  -  ".join(exibir)
        
        self.exibir_todos_ped.append(lista)
        self.exibir_todos_ped.append("\n")
        novo_exibir = "".join(self.exibir_todos_ped)
        total_str = str(self.total)
        self.label_VTotal.setText(total_str)

        self.label_nota.setText(novo_exibir)
        self.comboBox_card.setCurrentIndex(0)
        self.spinBox_card.setValue(0)

    def editCBoxs(self):
        '''self.nome_atual = self.comboBox_edi.currentText()
        self.nome_atual = self.comboBox_edi.setItemText()'''
        
        indice = self.comboBox_edi.currentIndex()


        desc = self.desc_edi.text()
        nome = self.nome_edi.text()
        valor = self.valor_edi.text()

        self.comboBox_edi.setItemText(indice,nome)
        self.comboBox_exc.setItemText(indice,nome)
        self.comboBox_card.setItemText(indice,nome)

        #novo_nome = nome_atual.setItemText()

        
        self.desc_dict[nome] = desc
        self.valor_dict[nome] = valor

        self.desc_edi.clear()
        self.nome_edi.clear()
        self.valor_edi.clear()

        self.comboBox_edi.setCurrentIndex(0)
        
        
        
        '''
        nome_novo = self.nome_edi
        desc_nova = self.desc_edi
        valor_novo = self.valor_edi
        
        
        self.desc_dict[nome] = str(desc_nova)
        self.valor_dict[nome] = valor_novo
        '''
    def cancBotCad(self):
        self.desc_cad.clear()
        self.nome_cad.clear()
        self.valor_cad.clear()

    def cancBotEdi(self):
        self.desc_edi.clear()
        self.nome_edi.clear()
        self.valor_edi.clear()
        self.comboBox_edi.setCurrentIndex(0)
    
    def cancPedido(self):
        self.label_nota.clear()
        self.total=0
        self.label_VTotal.clear()
        self.exibir_todos_ped = []
        self.exibir_todos_ped.append("QUANT       V UNIT       PROD       V TOT \n")

    def cancBotExc(self):
        self.comboBox_exc.setCurrentIndex(0)

    def showMessageFinPed(self):
        message_box = QMessageBox()
        message_box.setText("Pedido efetuado com sucesso!")
        message_box.exec_()
        self.comboBox_edi.clear()
        self.comboBox_exc.clear()
        self.comboBox_card.clear()
        self.label_nota.clear()
        self.label_VTotal.clear()
        self.comboBox_edi.addItem(" ")
        self.comboBox_exc.addItem(" ")
        self.comboBox_card.addItem(" ")
