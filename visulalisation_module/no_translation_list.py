import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from no_translation_list_UI import Ui_noTranslationList

class NoTranslationController(QtWidgets.QDialog):
    wordList = []
    iterator = 0
    def __init__(self, wordList):
        super().__init__()
        self.wordList = wordList
        self.ui = Ui_noTranslationList()
        self.ui.setupUi(self)
        self.ui.word_label.setText(self.wordList[0][0])
        self.show()

    
    def nextWord(self):
        if self.iterator < len(self.wordList)-1:
            self.iterator+=1
        self.ui.word_label.setText(self.wordList[self.iterator][0])
        self.ui.translationText.clear()

    def previousWord(self):
        if self.iterator > 0:
            self.iterator-=1
        self.ui.word_label.setText(self.wordList[self.iterator][0])
        self.ui.translationText.clear()

    def saveAndExit(self):
        output = []
        for word in self.wordList:
            if len(word)!=1:
                output.append(word)
        self.wordList = output
        self.close()
        


    def addTranslation(self):
        translation = self.ui.translationText.toPlainText()
        if len(translation) == 0:
            return
        if translation not in self.wordList[self.iterator]:
            self.wordList[self.iterator].append(translation)
        self.ui.translationText.clear()
    
    def deleteWord(self):
        if len(self.wordList) <= 1:
            self.saveAndExit()
            return

        self.wordList.remove(self.wordList[self.iterator])

        if self.iterator >= len(self.wordList)-1:
            self.iterator-=1

        self.ui.word_label.setText(self.wordList[self.iterator][0])
        
    def getList(self):
        return self.wordList
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    load_srt = NoTranslationController([['apple'], ['pear'], ['orange'], ['pineaple']])
    sys.exit(app.exec_())
    list1 = load_srt.getList()
    print(list1)
    