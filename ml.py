# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ml.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QComboBox, QWidget, QPushButton, QLabel, QLineEdit, QScrollArea, QStatusBar, QMenuBar, \
    QVBoxLayout
from constants import SIZE_L, SIZE_W


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.setFixedSize(SIZE_L, SIZE_W)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Создаем QLabel для обработки перетаскивания файлов
        self.dropLabel = QLabel('Перетащите файл сюда', self.centralwidget)
        self.dropLabel.setGeometry(QtCore.QRect(90, 300, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dropLabel.setFont(font)
        self.dropLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dropLabel.setObjectName("dropLabel")
        self.dropLabel.setAcceptDrops(True)

        #   Кнопка для открывания второго окна
        self.window2_button = QPushButton("Проверить по ГОСТ", self.centralwidget)
        self.window2_button.setGeometry(QtCore.QRect(260, 395, 190, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.window2_button.setFont(font)
        self.window2_button.setObjectName("window2_button")

        # Кнопка выбора файла
        self.pickFileButton = QPushButton("Выбрать файл", self.centralwidget)
        self.pickFileButton.setGeometry(QtCore.QRect(20, 550, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pickFileButton.setFont(font)
        self.pickFileButton.setObjectName("pickFileButton")

        self.pickAligment = QComboBox(self.centralwidget)
        self.pickAligment.setGeometry(QtCore.QRect(20, 200, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pickAligment.setFont(font)
        self.pickAligment.setObjectName("pickAlignmentComboBox")

        self.labelAlignment = QLabel(self.centralwidget)
        self.labelAlignment.setGeometry(QtCore.QRect(20, 160, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelAlignment.setFont(font)
        self.labelAlignment.setObjectName("labelAlignment")

        self.pickAlignmentLabel = QLabel(self.centralwidget)
        self.pickAlignmentLabel.setGeometry(QtCore.QRect(120, 200, 160, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pickAlignmentLabel.setFont(font)
        self.pickAlignmentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pickAlignmentLabel.setObjectName("pickAlignmentLabel")

        self.pickIndent = QLabel(self.centralwidget)
        self.pickIndent.setGeometry(QtCore.QRect(280, 70, 270, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pickIndent.setFont(font)
        self.pickIndent.setObjectName("pickIndentLabel")

        self.enterIndent = QLineEdit(self.centralwidget)
        self.enterIndent.setGeometry(QtCore.QRect(280, 110, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.enterIndent.setFont(font)
        self.enterIndent.setObjectName("enterIndent")
        self.enterIndent.setPlaceholderText('0')
        self.enterIndent.setValidator(QtGui.QDoubleValidator())

        self.enterIndentLabel = QLabel(self.centralwidget)
        self.enterIndentLabel.setGeometry(QtCore.QRect(370, 110, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.enterIndentLabel.setFont(font)
        self.enterIndentLabel.setObjectName("entetIndentLabel")

        self.enterLineSpace = QLineEdit(self.centralwidget)
        self.enterLineSpace.setGeometry(QtCore.QRect(280, 200, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.enterLineSpace.setFont(font)
        self.enterLineSpace.setObjectName("pickLineSpace")
        self.enterLineSpace.setPlaceholderText('1')
        self.enterLineSpace.setValidator(QtGui.QDoubleValidator())

        self.pickLineSpace = QLabel(self.centralwidget)
        self.pickLineSpace.setGeometry(QtCore.QRect(280, 150, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pickLineSpace.setFont(font)
        self.pickLineSpace.setObjectName("pickLineSpaceLabel")

        self.enterLineSpaceLabel = QLabel(self.centralwidget)
        self.enterLineSpaceLabel.setGeometry(QtCore.QRect(370, 200, 60, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.enterLineSpaceLabel.setFont(font)
        self.enterLineSpaceLabel.setObjectName("enterLineSpaceLabel")

        self.titlePicked = QLabel(self.centralwidget)
        self.titlePicked.setGeometry(QtCore.QRect(100, 110, 160, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.titlePicked.setFont(font)
        self.titlePicked.setAlignment(QtCore.Qt.AlignCenter)
        self.titlePicked.setObjectName("titlePicked")

        self.choiceTitle = QComboBox(self.centralwidget)
        self.choiceTitle.setGeometry(QtCore.QRect(20, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.choiceTitle.setFont(font)
        self.choiceTitle.setObjectName("choiceTitle")

        self.pickTitle = QLabel(self.centralwidget)
        self.pickTitle.setGeometry(QtCore.QRect(20, 70, 220, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pickTitle.setFont(font)
        self.pickTitle.setObjectName("pickTitle")

        self.filePicked = QLabel(self.centralwidget)
        self.filePicked.setGeometry(QtCore.QRect(250, 280, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.filePicked.setFont(font)
        self.filePicked.setAlignment(QtCore.Qt.AlignCenter)
        self.filePicked.setObjectName("filePicked")

        self.pickFile = QLabel(self.centralwidget)
        self.pickFile.setGeometry(QtCore.QRect(90, 240, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pickFile.setFont(font)
        self.pickFile.setObjectName("pickFile")

        self.checkFile = QPushButton(self.centralwidget)
        self.checkFile.setGeometry(QtCore.QRect(160, 345, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkFile.setFont(font)
        self.checkFile.setObjectName("checkFile")

        self.title = QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(70, 20, 380, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        self.answer = QScrollArea(self.centralwidget)
        self.answer.setGeometry(QtCore.QRect(20, 550, 350, 150))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.answer.setFont(font)
        self.answer.setWidgetResizable(True)
        self.answer.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.answer.setObjectName("answer")

        # self.pickGost = QLabel(self.centralwidget)
        # self.pickGost.setGeometry(QtCore.QRect(20, 450, 220, 31))
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setBold(True)
        # font.setWeight(75)
        # self.pickGost.setFont(font)
        # self.pickGost.setObjectName("pickGost")
        #
        # self.gostPicked = QLabel(self.centralwidget)
        # self.gostPicked.setGeometry(QtCore.QRect(200, 480, 160, 31))
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # font.setBold(True)
        # font.setWeight(75)
        # self.gostPicked.setFont(font)
        # self.gostPicked.setAlignment(QtCore.Qt.AlignCenter)
        # self.gostPicked.setObjectName("gostPicked")
        #
        # self.choiceGost = QComboBox(self.centralwidget)
        # self.choiceGost.setGeometry(QtCore.QRect(20, 480, 180, 31))
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # font.setBold(True)
        # font.setWeight(75)
        # self.choiceGost.setFont(font)
        # self.choiceGost.setObjectName("choiceGost")

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 229, 119))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.answer.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Создаем вертикальный лейаут
        layout = QVBoxLayout(self.centralwidget)

        # Добавляем элементы в вертикальный лейаут
        layout.addWidget(self.title)
        layout.addWidget(self.pickTitle)
        layout.addWidget(self.choiceTitle)
        layout.addWidget(self.titlePicked)

        layout.addWidget(self.labelAlignment)
        layout.addWidget(self.pickAligment)
        layout.addWidget(self.pickAlignmentLabel)

        layout.addWidget(self.pickIndent)
        layout.addWidget(self.enterIndent)
        layout.addWidget(self.enterIndentLabel)

        layout.addWidget(self.pickLineSpace)
        layout.addWidget(self.enterLineSpace)
        layout.addWidget(self.enterLineSpaceLabel)

        # layout.addWidget(self.pickGost)
        # layout.addWidget(self.choiceGost)
        # layout.addWidget(self.gostPicked)

        layout.addWidget(self.pickFile)
        layout.addWidget(self.dropLabel)
        layout.addWidget(self.pickFileButton)
        layout.addWidget(self.filePicked)
        layout.addWidget(self.checkFile)

        layout.addWidget(self.answer)

        # Устанавливаем лейаут в центральный виджет
        self.centralwidget.setLayout(layout)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pickFileButton.setText(_translate("MainWindow", "Выбрать файл"))
        self.window2_button.setText(_translate("MainWindow", "Проверить по ГОСТ"))
        self.titlePicked.setText(_translate("MainWindow", "TextLabel"))
        self.pickTitle.setText(_translate("MainWindow", "Выберите заголовок:"))
        # self.pickGost.setText(_translate("MainWindow", "Выберите ГОСТ:"))
        # self.gostPicked.setText(_translate("MainWindow", "TextLabel"))
        self.filePicked.setText(_translate("MainWindow", "TextLabel"))
        self.pickFile.setText(_translate("MainWindow", "Выберите файл (docx): "))
        self.checkFile.setText(_translate("MainWindow", "Проверка файла"))
        self.title.setText(_translate("MainWindow", "Проверка файла по своим настройкам"))
        self.pickIndent.setText(_translate("MainWindow", "Укажите отступ в см:"))
        self.enterIndentLabel.setText(_translate("MainWindow", "0 см"))
        self.labelAlignment.setText(_translate("MainWindow", "Укажите выравнивание:"))
        self.pickLineSpace.setText(_translate("MainWindow", "Укажите межстрочный интервал в см:"))
        self.enterLineSpaceLabel.setText(_translate("MainWindow", "1 см"))
