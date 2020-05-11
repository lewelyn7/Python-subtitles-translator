from PyQt5 import QtCore, QtGui, QtWidgets
from .load_srt_UI import Ui_load_srt
from configs.config_manip import Config

class LoadSrtDialog(QtWidgets.QDialog):
    def __init__(self, config):
        super(LoadSrtDialog, self).__init__()

        self.config = config

        self.ui = Ui_load_srt()
        self.ui.setupUi(self)
        self.show()
    def load_file_action(self):
        print("open file")

    def open_file_dialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        print(fname)
    def open_database_file(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        cfg = Config("config.yaml")
        cfgdic = cfg.get()
        cfgdic['database_file'] = fname[0]
        cfg.save()
    def API_settings_changed(self):
        lemma_api = str(self.ui.word_lemma_combo.currentText())
        word_score_api = str(self.ui.word_scoring_combo.currentText())
        translation_api = str(self.ui.word_trans_combo.currentText())