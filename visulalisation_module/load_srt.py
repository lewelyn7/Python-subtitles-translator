from PyQt5 import QtCore, QtGui, QtWidgets
from .load_srt_UI import UiLoadSrt
from configs.config_manip import Config
from os import getcwd
class LoadSrtDialog(QtWidgets.QDialog):
    def __init__(self, config):
        super(LoadSrtDialog, self).__init__()

        self.config = config

        self.ui = UiLoadSrt()
        self.ui.setupUi(self)
        self.cfg = self.config.get()
        self.ui.word_lemma_combo.setCurrentText(self.cfg["word_lemmatization_API"])
        self.ui.word_scoring_combo.setCurrentText(self.cfg["word_scoring_API"])
        self.ui.word_trans_combo.setCurrentText(self.cfg["word_translation_API"])
        self.ui.select_file_btn_2.setText(self.cfg["database_filename"].split("/")[-1])
        
        self.show()
    def load_file_action(self): #srt file I mean
        self.ui.load_btn.setText("loading...")
        self.ui.progressBar.setValue(10)

    def open_file_dialog(self): # srt file
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.filename = fname[0]
        if(self.filename == ""):
            self.ui.select_file_btn.setText("select file")
        else:
            self.ui.select_file_btn.setText(self.filename("/")[-1])
        
    def open_database_file(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', getcwd())
        self.cfg['database_filename'] = fname[0]
        self.ui.select_file_btn_2.setText(self.cfg["database_filename"].split("/")[-1])
        self.config.save()
    def API_settings_changed(self):
        self.cfg["word_lemmatization_API"] = str(self.ui.word_lemma_combo.currentText())
        self.cfg["word_translation_API"] = str(self.ui.word_scoring_combo.currentText())
        self.cfg["word_scoring_API"] = str(self.ui.word_trans_combo.currentText())
        self.config.save()

