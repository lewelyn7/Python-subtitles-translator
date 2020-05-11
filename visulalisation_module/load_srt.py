from PyQt5 import QtCore, QtGui, QtWidgets
from .load_srt_UI import Ui_load_srt

class LoadSrtDialog(QtWidgets.QDialog):
    def __init__(self):
        super(LoadSrtDialog, self).__init__()
        self.ui = Ui_load_srt()
        self.ui.setupUi(self)
        self.show()
    def load_file_action(self):
        print("open file")

    def open_file_dialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        print(fname)
    def open_database_file(self):
        pass
    def API_settings_changed(self):
        pass