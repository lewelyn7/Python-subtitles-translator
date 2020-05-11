# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_config_dialog(object):
    def setupUi(self, config_dialog):
        config_dialog.setObjectName("config_dialog")
        config_dialog.resize(400, 210)
        self.gridLayout = QtWidgets.QGridLayout(config_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.word_lemma_combo = QtWidgets.QComboBox(config_dialog)
        self.word_lemma_combo.setObjectName("word_lemma_combo")
        self.word_lemma_combo.addItem("")
        self.word_lemma_combo.addItem("")
        self.word_lemma_combo.addItem("")
        self.gridLayout.addWidget(self.word_lemma_combo, 3, 1, 1, 1)
        self.db_file_label = QtWidgets.QLabel(config_dialog)
        self.db_file_label.setObjectName("db_file_label")
        self.gridLayout.addWidget(self.db_file_label, 0, 0, 1, 1)
        self.select_file_btn = QtWidgets.QPushButton(config_dialog)
        self.select_file_btn.setObjectName("select_file_btn")
        self.gridLayout.addWidget(self.select_file_btn, 0, 1, 1, 1)
        self.word_trans_combo = QtWidgets.QComboBox(config_dialog)
        self.word_trans_combo.setObjectName("word_trans_combo")
        self.word_trans_combo.addItem("")
        self.gridLayout.addWidget(self.word_trans_combo, 4, 1, 1, 1)
        self.word_scoring_combo = QtWidgets.QComboBox(config_dialog)
        self.word_scoring_combo.setObjectName("word_scoring_combo")
        self.word_scoring_combo.addItem("")
        self.gridLayout.addWidget(self.word_scoring_combo, 2, 1, 1, 1)
        self.word_scoring_lbl = QtWidgets.QLabel(config_dialog)
        self.word_scoring_lbl.setObjectName("word_scoring_lbl")
        self.gridLayout.addWidget(self.word_scoring_lbl, 2, 0, 1, 1)
        self.word_lemma_lbl = QtWidgets.QLabel(config_dialog)
        self.word_lemma_lbl.setObjectName("word_lemma_lbl")
        self.gridLayout.addWidget(self.word_lemma_lbl, 3, 0, 1, 1)
        self.word_trans_lbl = QtWidgets.QLabel(config_dialog)
        self.word_trans_lbl.setObjectName("word_trans_lbl")
        self.gridLayout.addWidget(self.word_trans_lbl, 4, 0, 1, 1)

        self.retranslateUi(config_dialog)
        QtCore.QMetaObject.connectSlotsByName(config_dialog)

    def retranslateUi(self, config_dialog):
        _translate = QtCore.QCoreApplication.translate
        config_dialog.setWindowTitle(_translate("config_dialog", "Config"))
        self.word_lemma_combo.setItemText(0, _translate("config_dialog", "WiktionaryAPI"))
        self.word_lemma_combo.setItemText(1, _translate("config_dialog", "UltraLinguaAPI"))
        self.word_lemma_combo.setItemText(2, _translate("config_dialog", "LinguaRobotAPI"))
        self.db_file_label.setText(_translate("config_dialog", "Database file:"))
        self.select_file_btn.setText(_translate("config_dialog", "Select File"))
        self.word_trans_combo.setItemText(0, _translate("config_dialog", "Offline Database"))
        self.word_scoring_combo.setItemText(0, _translate("config_dialog", "TwinWordAPI"))
        self.word_scoring_lbl.setText(_translate("config_dialog", "Word scoring engine"))
        self.word_lemma_lbl.setText(_translate("config_dialog", "Word lemmatization engine"))
        self.word_trans_lbl.setText(_translate("config_dialog", "Word translation engine"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    config_dialog = QtWidgets.QDialog()
    ui = Ui_config_dialog()
    ui.setupUi(config_dialog)
    config_dialog.show()
    sys.exit(app.exec_())
