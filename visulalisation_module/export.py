# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_export_dialog(object):
    def setupUi(self, export_dialog):
        export_dialog.setObjectName("export_dialog")
        export_dialog.setEnabled(True)
        export_dialog.resize(401, 215)
        self.gridLayout_2 = QtWidgets.QGridLayout(export_dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.export_btn = QtWidgets.QPushButton(export_dialog)
        self.export_btn.setObjectName("export_btn")
        self.gridLayout_2.addWidget(self.export_btn, 4, 1, 1, 2)
        self.file_extension_box = QtWidgets.QComboBox(export_dialog)
        self.file_extension_box.setObjectName("file_extension_box")
        self.file_extension_box.addItem("")
        self.gridLayout_2.addWidget(self.file_extension_box, 0, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(export_dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.column_separator_label = QtWidgets.QLabel(self.groupBox)
        self.column_separator_label.setObjectName("column_separator_label")
        self.gridLayout.addWidget(self.column_separator_label, 0, 0, 1, 1)
        self.record_separator_label = QtWidgets.QLabel(self.groupBox)
        self.record_separator_label.setObjectName("record_separator_label")
        self.gridLayout.addWidget(self.record_separator_label, 0, 1, 1, 1)
        self.column_separator_box = QtWidgets.QLineEdit(self.groupBox)
        self.column_separator_box.setObjectName("column_separator_box")
        self.gridLayout.addWidget(self.column_separator_box, 1, 0, 1, 1)
        self.record_separator_combo_box = QtWidgets.QComboBox(self.groupBox)
        self.record_separator_combo_box.setObjectName("record_separator_combo_box")
        self.record_separator_combo_box.addItem("")
        self.record_separator_combo_box.addItem("")
        self.gridLayout.addWidget(self.record_separator_combo_box, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 4)
        self.file_label = QtWidgets.QLabel(export_dialog)
        self.file_label.setObjectName("file_label")
        self.gridLayout_2.addWidget(self.file_label, 0, 0, 1, 1)
        self.open_file_selector_btn = QtWidgets.QPushButton(export_dialog)
        self.open_file_selector_btn.setObjectName("open_file_selector_btn")
        self.gridLayout_2.addWidget(self.open_file_selector_btn, 0, 2, 1, 1)
        self.column_order_combo = QtWidgets.QComboBox(export_dialog)
        self.column_order_combo.setObjectName("column_order_combo")
        self.column_order_combo.addItem("")
        self.column_order_combo.addItem("")
        self.gridLayout_2.addWidget(self.column_order_combo, 2, 2, 1, 2)
        self.column_order_lbl = QtWidgets.QLabel(export_dialog)
        self.column_order_lbl.setObjectName("column_order_lbl")
        self.gridLayout_2.addWidget(self.column_order_lbl, 2, 0, 1, 2)

        self.retranslateUi(export_dialog)
        QtCore.QMetaObject.connectSlotsByName(export_dialog)

    def retranslateUi(self, export_dialog):
        _translate = QtCore.QCoreApplication.translate
        export_dialog.setWindowTitle(_translate("export_dialog", "Export"))
        self.export_btn.setText(_translate("export_dialog", "Export"))
        self.file_extension_box.setItemText(0, _translate("export_dialog", "csv"))
        self.column_separator_label.setText(_translate("export_dialog", "column Separator"))
        self.record_separator_label.setText(_translate("export_dialog", "new record separator"))
        self.column_separator_box.setText(_translate("export_dialog", ";"))
        self.record_separator_combo_box.setItemText(0, _translate("export_dialog", "NL"))
        self.record_separator_combo_box.setItemText(1, _translate("export_dialog", "CR+NL"))
        self.file_label.setText(_translate("export_dialog", "File:"))
        self.open_file_selector_btn.setText(_translate("export_dialog", "Select file"))
        self.column_order_combo.setItemText(0, _translate("export_dialog", "translation first"))
        self.column_order_combo.setItemText(1, _translate("export_dialog", "word first"))
        self.column_order_lbl.setText(_translate("export_dialog", "Column order:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    export_dialog = QtWidgets.QDialog()
    ui = Ui_export_dialog()
    ui.setupUi(export_dialog)
    export_dialog.show()
    sys.exit(app.exec_())
