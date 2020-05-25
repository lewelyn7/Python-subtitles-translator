# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'no_translation_list_UI2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class UiNoTranslationList(object):
    def setupUi(self, noTranslationList):
        noTranslationList.setObjectName("noTranslationList")
        noTranslationList.resize(475, 300)
        self.gridLayout = QtWidgets.QGridLayout(noTranslationList)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setSpacing(14)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.go_left_button = QtWidgets.QPushButton(noTranslationList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_left_button.sizePolicy().hasHeightForWidth())
        self.go_left_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.go_left_button.setFont(font)
        self.go_left_button.setObjectName("go_left_button")
        self.horizontalLayout_2.addWidget(self.go_left_button)
        self.word_label = QtWidgets.QLabel(noTranslationList)
        self.word_label.setMinimumSize(QtCore.QSize(256, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.word_label.setFont(font)
        self.word_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.word_label.setTextFormat(QtCore.Qt.AutoText)
        self.word_label.setScaledContents(True)
        self.word_label.setAlignment(QtCore.Qt.AlignCenter)
        self.word_label.setIndent(1)
        self.word_label.setObjectName("word_label")
        self.horizontalLayout_2.addWidget(self.word_label)
        self.go_right_button = QtWidgets.QPushButton(noTranslationList)
        self.go_right_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_right_button.sizePolicy().hasHeightForWidth())
        self.go_right_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.go_right_button.setFont(font)
        self.go_right_button.setFlat(False)
        self.go_right_button.setObjectName("go_right_button")
        self.horizontalLayout_2.addWidget(self.go_right_button)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontal_layout.setContentsMargins(15, 5, 0, 5)
        self.horizontal_layout.setSpacing(5)
        self.horizontal_layout.setObjectName("horizontal_layout")
        self.translationText = QtWidgets.QTextEdit(noTranslationList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.translationText.sizePolicy().hasHeightForWidth())
        self.translationText.setSizePolicy(sizePolicy)
        self.translationText.setMinimumSize(QtCore.QSize(256, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.translationText.setFont(font)
        self.translationText.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.translationText.setObjectName("translationText")
        self.horizontal_layout.addWidget(self.translationText, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.addTranslationButton = QtWidgets.QPushButton(noTranslationList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTranslationButton.sizePolicy().hasHeightForWidth())
        self.addTranslationButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.addTranslationButton.setFont(font)
        self.addTranslationButton.setObjectName("addTranslationButton")
        self.horizontal_layout.addWidget(self.addTranslationButton)
        self.deleteWordButton = QtWidgets.QPushButton(noTranslationList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteWordButton.sizePolicy().hasHeightForWidth())
        self.deleteWordButton.setSizePolicy(sizePolicy)
        self.deleteWordButton.setObjectName("deleteWordButton")
        self.horizontal_layout.addWidget(self.deleteWordButton)
        self.horizontal_layout.setStretch(1, 2)
        self.horizontal_layout.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.horizontal_layout)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.saveButton = QtWidgets.QPushButton(noTranslationList)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout_3.addWidget(self.saveButton)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(noTranslationList)
        self.go_left_button.clicked.connect(noTranslationList.previousWord)
        self.go_right_button.clicked.connect(noTranslationList.nextWord)
        self.addTranslationButton.clicked.connect(noTranslationList.addTranslation)
        self.deleteWordButton.clicked.connect(noTranslationList.deleteWord)
        self.saveButton.clicked.connect(noTranslationList.saveAndExit)
        QtCore.QMetaObject.connectSlotsByName(noTranslationList)

    def retranslateUi(self, noTranslationList):
        _translate = QtCore.QCoreApplication.translate
        noTranslationList.setWindowTitle(_translate("noTranslationList", "Dialog"))
        self.go_left_button.setText(_translate("noTranslationList", "<"))
        self.go_left_button.setShortcut(_translate("noTranslationList", "Left"))
        self.word_label.setText(_translate("noTranslationList", "O<-< martfyczuowiek"))
        self.go_right_button.setText(_translate("noTranslationList", ">"))
        self.go_right_button.setShortcut(_translate("noTranslationList", "Right"))
        self.translationText.setPlaceholderText(_translate("noTranslationList", "Translation"))
        self.addTranslationButton.setText(_translate("noTranslationList", "Add translation"))
        self.addTranslationButton.setShortcut(_translate("noTranslationList", "Z"))
        self.deleteWordButton.setText(_translate("noTranslationList", "Ignore word"))
        self.deleteWordButton.setShortcut(_translate("noTranslationList", "X"))
        self.saveButton.setToolTip(_translate("noTranslationList", "Save all changes and go to the next step."))
        self.saveButton.setText(_translate("noTranslationList", "Save all"))