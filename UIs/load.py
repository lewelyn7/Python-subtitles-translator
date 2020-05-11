# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows3.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_load_srt(object):
    def setupUi(self, load_srt):
        load_srt.setObjectName("load_srt")
        load_srt.resize(400, 147)
        self.gridLayout = QtWidgets.QGridLayout(load_srt)
        self.gridLayout.setObjectName("gridLayout")
        self.select_file_btn = QtWidgets.QPushButton(load_srt)
        self.select_file_btn.setObjectName("select_file_btn")
        self.gridLayout.addWidget(self.select_file_btn, 0, 1, 1, 1)
        self.load_btn = QtWidgets.QPushButton(load_srt)
        self.load_btn.setObjectName("load_btn")
        self.gridLayout.addWidget(self.load_btn, 2, 0, 1, 2)
        self.file_lbl = QtWidgets.QLabel(load_srt)
        self.file_lbl.setObjectName("file_lbl")
        self.gridLayout.addWidget(self.file_lbl, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(load_srt)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 2)
        self.status_lbl = QtWidgets.QLabel(load_srt)
        self.status_lbl.setObjectName("status_lbl")
        self.gridLayout.addWidget(self.status_lbl, 4, 0, 1, 1)

        self.retranslateUi(load_srt)
        QtCore.QMetaObject.connectSlotsByName(load_srt)

    def retranslateUi(self, load_srt):
        _translate = QtCore.QCoreApplication.translate
        load_srt.setWindowTitle(_translate("load_srt", "Load srt file"))
        self.select_file_btn.setText(_translate("load_srt", "Select file"))
        self.load_btn.setText(_translate("load_srt", "Load"))
        self.file_lbl.setText(_translate("load_srt", "File: "))
        self.status_lbl.setText(_translate("load_srt", "Not loaded..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    load_srt = QtWidgets.QDialog()
    ui = Ui_load_srt()
    ui.setupUi(load_srt)
    load_srt.show()
    sys.exit(app.exec_())
