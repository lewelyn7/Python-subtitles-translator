# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'most_frequent_list_UI2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mostFrequentList(object):
    def setupUi(self, mostFrequentList):
        mostFrequentList.setObjectName("mostFrequentList")
        mostFrequentList.resize(631, 276)
        self.gridLayout = QtWidgets.QGridLayout(mostFrequentList)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setSpacing(14)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.go_left_button_2 = QtWidgets.QPushButton(mostFrequentList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_left_button_2.sizePolicy().hasHeightForWidth())
        self.go_left_button_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.go_left_button_2.setFont(font)
        self.go_left_button_2.setObjectName("go_left_button_2")
        self.horizontalLayout_3.addWidget(self.go_left_button_2)
        self.word_label_2 = QtWidgets.QLabel(mostFrequentList)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.word_label_2.setFont(font)
        self.word_label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.word_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.word_label_2.setScaledContents(True)
        self.word_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.word_label_2.setIndent(1)
        self.word_label_2.setObjectName("word_label_2")
        self.horizontalLayout_3.addWidget(self.word_label_2)
        self.go_right_button_2 = QtWidgets.QPushButton(mostFrequentList)
        self.go_right_button_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_right_button_2.sizePolicy().hasHeightForWidth())
        self.go_right_button_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.go_right_button_2.setFont(font)
        self.go_right_button_2.setFlat(False)
        self.go_right_button_2.setObjectName("go_right_button_2")
        self.horizontalLayout_3.addWidget(self.go_right_button_2)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout()
        self.horizontal_layout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontal_layout_2.setContentsMargins(15, -1, 0, -1)
        self.horizontal_layout_2.setSpacing(0)
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        self.known_button_2 = QtWidgets.QRadioButton(mostFrequentList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.known_button_2.sizePolicy().hasHeightForWidth())
        self.known_button_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.known_button_2.setFont(font)
        self.known_button_2.setObjectName("known_button_2")
        self.horizontal_layout_2.addWidget(self.known_button_2)
        self.not_known_button_2 = QtWidgets.QRadioButton(mostFrequentList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.not_known_button_2.sizePolicy().hasHeightForWidth())
        self.not_known_button_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.not_known_button_2.setFont(font)
        self.not_known_button_2.setChecked(True)
        self.not_known_button_2.setObjectName("not_known_button_2")
        self.horizontal_layout_2.addWidget(self.not_known_button_2)
        self.pushButton_2 = QtWidgets.QPushButton(mostFrequentList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontal_layout_2.addWidget(self.pushButton_2)
        self.verticalLayout_5.addLayout(self.horizontal_layout_2)
        self.verticalLayout_5.setStretch(0, 3)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.save_button_2 = QtWidgets.QPushButton(mostFrequentList)
        self.save_button_2.setObjectName("save_button_2")
        self.verticalLayout_4.addWidget(self.save_button_2)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.retranslateUi(mostFrequentList)
        self.go_left_button_2.clicked.connect(mostFrequentList.previousWord)
        self.go_right_button_2.clicked.connect(mostFrequentList.nextWord)
        self.not_known_button_2.clicked.connect(mostFrequentList.updateScore)
        self.pushButton_2.clicked.connect(mostFrequentList.translateWord)
        self.known_button_2.clicked.connect(mostFrequentList.updateScore)
        self.save_button_2.clicked.connect(mostFrequentList.saveAndExit)
        QtCore.QMetaObject.connectSlotsByName(mostFrequentList)

    def retranslateUi(self, mostFrequentList):
        _translate = QtCore.QCoreApplication.translate
        mostFrequentList.setWindowTitle(_translate("mostFrequentList", "Dialog"))
        self.go_left_button_2.setText(_translate("mostFrequentList", "<"))
        self.go_left_button_2.setShortcut(_translate("mostFrequentList", "Left"))
        self.word_label_2.setText(_translate("mostFrequentList", "TextLabel"))
        self.go_right_button_2.setText(_translate("mostFrequentList", ">"))
        self.go_right_button_2.setShortcut(_translate("mostFrequentList", "Right"))
        self.known_button_2.setText(_translate("mostFrequentList", "Znam"))
        self.known_button_2.setShortcut(_translate("mostFrequentList", "Z"))
        self.not_known_button_2.setText(_translate("mostFrequentList", "Nie Znam"))
        self.not_known_button_2.setShortcut(_translate("mostFrequentList", "X"))
        self.pushButton_2.setText(_translate("mostFrequentList", "Tłumacz"))
        self.pushButton_2.setShortcut(_translate("mostFrequentList", "Space"))
        self.save_button_2.setToolTip(_translate("mostFrequentList", "Zapisz wszystkie zmiany i przejdź do następniego kroku."))
        self.save_button_2.setText(_translate("mostFrequentList", "Zapisz wszystkie"))
