import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from .most_frequent_list_UI import Ui_mostFrequentList

class MostFrequentController(QtWidgets.QDialog):
    wordList = []
    iterator = 0
    isTranslated = 0

    def __init__(self, wordList):
        super().__init__()
        self.wordList = wordList
        self.ui = Ui_mostFrequentList()
        self.ui.setupUi(self)
        self.ui.word_label_2.setText(self.wordList[0][0])
        self.show()

    def translateWord(self):
        self.isTranslated = (self.isTranslated+1)%2
        
        if self.isTranslated == 0:
            self.ui.word_label_2.setText(self.wordList[self.iterator][0])
        else:
             self.ui.word_label_2.setText(self.makeReadable(self.wordList[self.iterator][1]))
    
    def nextWord(self):
        if self.iterator < len(self.wordList)-1:
            self.iterator+=1
            self.isTranslated=0
            self.translateWord
        self.ui.word_label_2.setText(self.wordList[self.iterator][0])
        if self.wordList[self.iterator][2] == 0:
            self.ui.not_known_button_2.setChecked(True)
        else:
            self.ui.known_button_2.setChecked(True)

    def previousWord(self):
        if self.iterator > 0:
            self.iterator-=1
            self.isTranslated=0
            self.translateWord
        self.ui.word_label_2.setText(self.wordList[self.iterator][0])
        if self.wordList[self.iterator][2] == 0:
            self.ui.not_known_button_2.setChecked(True)
        else:
            self.ui.known_button_2.setChecked(True)
    
    def updateScore(self):
        if self.ui.known_button_2.isChecked():
            self.wordList[self.iterator][2] = 1
        else:
            self.wordList[self.iterator][2] = 0

    
    def saveAndExit(self):
        self.close()
        return self.wordList
        
    def getList(self):
        return self.wordList

    def makeReadable(self, words):
        pass

    def getScore(self):
        output = 0
        for word in self.wordList:
            output+=word[2]
        return output
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    load_srt = MostFrequentController([['apple', 'japko', 0], ['pear', 'gruszka', 0]])
    app.exec_()
    list1 = load_srt.getList()
    print(list1)