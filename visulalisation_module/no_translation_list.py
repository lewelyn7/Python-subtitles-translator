# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\no_translation_list.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 294)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
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
        self.go_left_button = QtWidgets.QPushButton(self.centralwidget)
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
        self.word_label = QtWidgets.QLabel(self.centralwidget)
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
        self.go_right_button = QtWidgets.QPushButton(self.centralwidget)
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
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(256, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textEdit.setFont(font)
        self.textEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textEdit.setObjectName("textEdit")
        self.horizontal_layout.addWidget(self.textEdit, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontal_layout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontal_layout.addWidget(self.pushButton_2)
        self.horizontal_layout.setStretch(1, 2)
        self.horizontal_layout.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.horizontal_layout)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setObjectName("save_button")
        self.verticalLayout_3.addWidget(self.save_button)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.go_left_button.setText(_translate("MainWindow", "<"))
        self.go_left_button.setShortcut(_translate("MainWindow", "Left"))
        self.word_label.setText(_translate("MainWindow", "TextLabel"))
        self.go_right_button.setText(_translate("MainWindow", ">"))
        self.go_right_button.setShortcut(_translate("MainWindow", "Right"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Tłumaczenie"))
        self.pushButton.setText(_translate("MainWindow", "Dodaj tłumaczenie"))
        self.pushButton.setShortcut(_translate("MainWindow", "Z"))
        self.pushButton_2.setText(_translate("MainWindow", "Usuń słowo"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "X"))
        self.save_button.setToolTip(_translate("MainWindow", "Zapisz wszystkie zmiany i przejdź do następniego kroku."))
        self.save_button.setText(_translate("MainWindow", "Zapisz wszyskie"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
