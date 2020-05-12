from visulalisation_module.load_srt import LoadSrtDialog
from visulalisation_module.export import ExportDialog
from PyQt5 import QtWidgets
from configs.config_manip import Config
import sys
from os import path

if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # load_srt = QtWidgets.QDialog()
    # ui = Ui_load_srt()
    # ui.setupUi(load_srt)
    # load_srt.show()
    # sys.exit(app.exec_())
    config = Config("config.yaml")
    config.read()

    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    app = QtWidgets.QApplication(sys.argv)
    load_srt = LoadSrtDialog(config)
    sys.exit(app.exec_())
