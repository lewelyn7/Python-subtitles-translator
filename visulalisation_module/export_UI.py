# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_export_dialog(object):
    def setupUi(self, export_dialog):
        export_dialog.setObjectName("export_dialog")
        export_dialog.setEnabled(True)
        export_dialog.resize(751, 316)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(export_dialog.sizePolicy().hasHeightForWidth())
        export_dialog.setSizePolicy(sizePolicy)
        export_dialog.setMaximumSize(QtCore.QSize(16777215, 316))
        self.gridLayout_2 = QtWidgets.QGridLayout(export_dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(export_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout_5.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.file_label = QtWidgets.QLabel(self.groupBox)
        self.file_label.setObjectName("file_label")
        self.gridLayout_3.addWidget(self.file_label, 0, 0, 1, 1)
        self.open_file_selector_btn = QtWidgets.QPushButton(self.groupBox)
        self.open_file_selector_btn.setObjectName("open_file_selector_btn")
        self.gridLayout_3.addWidget(self.open_file_selector_btn, 0, 2, 1, 1)
        self.file_extension_box = QtWidgets.QComboBox(self.groupBox)
        self.file_extension_box.setObjectName("file_extension_box")
        self.file_extension_box.addItem("")
        self.gridLayout_3.addWidget(self.file_extension_box, 0, 3, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.column_order_combo = QtWidgets.QComboBox(self.groupBox_2)
        self.column_order_combo.setObjectName("column_order_combo")
        self.column_order_combo.addItem("")
        self.column_order_combo.addItem("")
        self.gridLayout.addWidget(self.column_order_combo, 1, 2, 1, 1)
        self.record_separator_label = QtWidgets.QLabel(self.groupBox_2)
        self.record_separator_label.setObjectName("record_separator_label")
        self.gridLayout.addWidget(self.record_separator_label, 0, 1, 1, 1)
        self.record_separator_combo_box = QtWidgets.QComboBox(self.groupBox_2)
        self.record_separator_combo_box.setObjectName("record_separator_combo_box")
        self.record_separator_combo_box.addItem("")
        self.record_separator_combo_box.addItem("")
        self.gridLayout.addWidget(self.record_separator_combo_box, 1, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 3, 1, 1)
        self.column_order_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.column_order_lbl.setObjectName("column_order_lbl")
        self.gridLayout.addWidget(self.column_order_lbl, 0, 2, 1, 1)
        self.column_separator_box = QtWidgets.QLineEdit(self.groupBox_2)
        self.column_separator_box.setObjectName("column_separator_box")
        self.gridLayout.addWidget(self.column_separator_box, 1, 0, 1, 1)
        self.column_separator_label = QtWidgets.QLabel(self.groupBox_2)
        self.column_separator_label.setObjectName("column_separator_label")
        self.gridLayout.addWidget(self.column_separator_label, 0, 0, 1, 1)
        self.translations_num_lbl = QtWidgets.QLabel(self.groupBox_2)
        self.translations_num_lbl.setObjectName("translations_num_lbl")
        self.gridLayout.addWidget(self.translations_num_lbl, 2, 0, 1, 1)
        self.translations_num_spin = QtWidgets.QSpinBox(self.groupBox_2)
        self.translations_num_spin.setMinimum(0)
        self.translations_num_spin.setMaximum(15)
        self.translations_num_spin.setProperty("value", 3)
        self.translations_num_spin.setObjectName("translations_num_spin")
        self.gridLayout.addWidget(self.translations_num_spin, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 4)
        self.export_btn = QtWidgets.QPushButton(self.groupBox)
        self.export_btn.setObjectName("export_btn")
        self.gridLayout_3.addWidget(self.export_btn, 3, 1, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(export_dialog)
        self.tabWidget.setCurrentIndex(1)
        self.open_file_selector_btn.clicked.connect(export_dialog.select_file)
        self.column_separator_box.editingFinished.connect(export_dialog.column_sep_changed)
        self.record_separator_combo_box.currentIndexChanged['QString'].connect(export_dialog.record_sep_changed)
        self.column_order_combo.currentIndexChanged['QString'].connect(export_dialog.column_order_changed)
        self.export_btn.clicked.connect(export_dialog.export_clicked)
        self.file_extension_box.currentIndexChanged['QString'].connect(export_dialog.file_extension_changed)
        self.checkBox.stateChanged['int'].connect(export_dialog.header_changed)
        QtCore.QMetaObject.connectSlotsByName(export_dialog)

    def retranslateUi(self, export_dialog):
        _translate = QtCore.QCoreApplication.translate
        export_dialog.setWindowTitle(_translate("export_dialog", "Export"))
        self.label_2.setText(_translate("export_dialog", "5/30"))
        self.label.setText(_translate("export_dialog", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("export_dialog", "Score"))
        self.groupBox.setTitle(_translate("export_dialog", "GroupBox"))
        self.file_label.setText(_translate("export_dialog", "File:"))
        self.open_file_selector_btn.setText(_translate("export_dialog", "Select file"))
        self.file_extension_box.setItemText(0, _translate("export_dialog", "csv"))
        self.column_order_combo.setItemText(0, _translate("export_dialog", "translation first"))
        self.column_order_combo.setItemText(1, _translate("export_dialog", "word first"))
        self.record_separator_label.setText(_translate("export_dialog", "new record separator"))
        self.record_separator_combo_box.setItemText(0, _translate("export_dialog", "NL"))
        self.record_separator_combo_box.setItemText(1, _translate("export_dialog", "CR+NL"))
        self.checkBox.setText(_translate("export_dialog", "Include header"))
        self.column_order_lbl.setText(_translate("export_dialog", "Column order:"))
        self.column_separator_box.setText(_translate("export_dialog", ";"))
        self.column_separator_label.setText(_translate("export_dialog", "column Separator"))
        self.translations_num_lbl.setText(_translate("export_dialog", "maximum number of translations:"))
        self.export_btn.setText(_translate("export_dialog", "Export"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("export_dialog", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    export_dialog = QtWidgets.QDialog()
    ui = Ui_export_dialog()
    ui.setupUi(export_dialog)
    export_dialog.show()
    sys.exit(app.exec_())
