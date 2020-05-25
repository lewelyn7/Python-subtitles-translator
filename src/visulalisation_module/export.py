from PyQt5 import QtCore, QtGui, QtWidgets
from configs.config_manip import Config
from .export_UI import Ui_export_dialog
from os import getcwd

from ..csv_manip.csv_exporter import CsvExporter, ExportError

class ExportDialog(QtWidgets.QDialog):
    def __init__(self, config, word_list, score, max_score):
        super(ExportDialog, self).__init__()

        self.score = score
        self.max_score = max_score
        self.config = config
        self.ui = Ui_export_dialog()
        self.ui.setupUi(self)
        self.ui.export_btn.setEnabled(False)
        self.ui.label_2.setText(str(score) + '/' + str(max_score))
        if self.score/self.max_score<0.3:
            self.ui.label.setText("This is too hard for you!")
        elif self.score/self.max_score<0.5:
            self.ui.label.setText("This might be too much of a challange, consider trying something simpler first.")
        elif self.score/self.max_score<0.7:
            self.ui.label.setText("This is an appropriate challange. You will learn a lot from this one.")
        elif self.score/self.max_score<0.9:
            self.ui.label.setText("This is a great way to relax while polishing your skills.")
        else:
            self.ui.label.setText("Isn't it a bit to easy? ;)")
        self.cfg = self.config.get()
        self.word_list = word_list
        self.show()
        self.col_sep = ";"
        self.col_order = "translation first"
        self.filename = ""
        self.rec_sep = "\n"
        self.include_header = False
        self.file_extension = "csv"
        self.translations_max = self.ui.translations_num_spin.value

    def select_file(self):
        fname = QtWidgets.QFileDialog.getSaveFileName(self, 'Open file', getcwd())
        self.filename = fname[0]
        if self.filename == "":
            self.ui.open_file_selector_btn.setText("select file")
            self.ui.export_btn.setEnabled(False)
        else:
            self.ui.export_btn.setEnabled(True)
            self.ui.open_file_selector_btn.setText(self.filename.split("/")[-1])


    def column_order_changed(self):
        if(self.ui.column_order_combo.currentText() == "translation first"):
            self.col_order = "translation first"
        else:
            self.col_order = "word first"      

    def column_sep_changed(self):
        self.col_sep = self.ui.column_separator_box.text()

    def record_sep_changed(self, word):
        if word == "CR+NL":
            self.rec_sep = "\r\n"
        else:
            self.rec_sep = "\n"

    def export_clicked(self):
        self.translations_max = int(self.ui.translations_num_spin.value())
        print(self.translations_max)
        csv_exporter = CsvExporter()
        try:
            csv_exporter.export(self.word_list, self.filename, self.col_order, self.col_sep, self.rec_sep, self.include_header, self.translations_max)
            print("exported")
            self.ui.export_btn.setText("exported")
            self.ui.export_btn.setEnabled(False)
        except ExportError:
            print("not exported - error")
        
    def file_extension_changed(self, word):
        self.file_extension = word

    def header_changed(self):
        self.include_header = self.ui.checkBox.isChecked()

    

