from PyQt5 import QtCore, QtGui, QtWidgets
from configs.config_manip import Config
from .export_UI import Ui_export_dialog
from os import getcwd

from csv_manip.csv_exporter import CsvExporter

class ExportDialog(QtWidgets.QDialog):
    def __init__(self, config, word_list):
        super(ExportDialog, self).__init__()

        self.config = config
        self.ui = Ui_export_dialog()
        self.ui.setupUi(self)
        self.cfg = self.config.get()
        self.word_list
        self.show()
        self.col_sep = ";"
        self.col_order = "translation first"
        self.filename = ""
        self.rec_sep = "\n"

    def select_file(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Open file', getcwd())
        self.filename = fname[0]
        if self.filename == "":
            self.ui.open_file_selector_btn.setText("select file")
        else:
            self.ui.open_file_selector_btn.setText(self.filename.split("/")[-1])


    def column_order_changed(self):
        if(self.ui.column_order_combo.currentText() == "translation first"):
            self.translation_first = True
        else:
            self.translation_first = False      

    def column_sep_changed(self):
        pass

    def record_sep_changed(self):
        pass

    def export_clicked(self):
        csv_exporter = CsvExporter()
        csv_exporter.export(self.word_list, self.filename, self.col_order, self.col_sep, self.rec_sep)

    def file_extension_changed(self):
        pass
    

