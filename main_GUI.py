from visulalisation_module.load_srt import LoadSrtDialog
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # load_srt = QtWidgets.QDialog()
    # ui = Ui_load_srt()
    # ui.setupUi(load_srt)
    # load_srt.show()
    # sys.exit(app.exec_())

    app = QtWidgets.QApplication(sys.argv)
    load_srt = LoadSrtDialog()
    sys.exit(app.exec_())
