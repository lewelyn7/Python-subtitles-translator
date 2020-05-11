import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from most_frequent_list_UI import Ui_MostFrequentList

class MostFrequentController(QtWidgets.QMainWindow):
    wordList = []
    iterator = 0
    def __init__(self, wordList):
        super().__init__()
        self.wordList = wordList
        self.ui = Ui_NoTranslationList()
        self.ui.setupUi(self)
        self.ui.word_label.setText(self.wordList[0][0])
        self.show()
    
    def nextWord(self):
        if self.iterator < len(self.wordList)-1:
            self.iterator+=1
        self.ui.word_label.setText(self.wordList[self.iterator][0])

    def previousWord(self):
        if self.iterator > 0:
            self.iterator-=1
        self.ui.word_label.setText(self.wordList[self.iterator][0])

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    load_srt = MostFrequentController([['apple', ''], ['pear', '']])
    sys.exit(app.exec_())