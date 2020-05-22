from PyQt5 import QtCore, QtGui, QtWidgets
from .load_srt_UI import UiLoadSrt
from configs.config_manip import Config
from os import getcwd

from srt_parsing_modules.srt_parser import srt_to_line, line_to_tokens
from filters.word_filter import WordFilter, LemmaAPIError
from dictionaries.dict_api import DictAPI
from database_integration_module.db_helpers import DbHelpers
from srt_parsing_modules.srt_parser import process_srt_file

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

        self.ui.load_btn.setEnabled(False)
        
        self.show()
    def load_file_action(self): #srt file I mean
        self.ui.load_btn.setText("loading...")
        def progress_bar_setter(value):
            bar = self.ui.progressBar
            bar.setValue(value)
        self.no_translations_words = process_srt_file(self.filename, self.config, progress_bar_setter)
        self.ui.load_btn.setText("loaded")
        self.ui.proceed_btn.setEnabled(True)
        self.ui.load_btn.setEnabled(False)
        self.ui.proceed_btn.setText("proceed")
       
    def proceed_clicked(self):
        self.close()


    def open_file_dialog(self): # srt file
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', getcwd())
        self.filename = fname[0]
        if(self.filename == ""):
            self.ui.select_file_btn.setText("select file")
            self.ui.load_btn.setEnabled(False)
        else:
            self.ui.load_btn.setEnabled(True)
            self.ui.select_file_btn.setText(self.filename.split("/")[-1])
    
        
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

