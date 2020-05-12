import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from no_translation_list_UI import UiNoTranslationList

class NoTranslationController(QtWidgets.QDialog):
    word_list = []
    blacklist = []
    iterator = 0
    def __init__(self, wordList):
        super().__init__()
        self.word_list = wordList
        self.ui = UiNoTranslationList()
        self.ui.setupUi(self)
        self.ui.word_label.setText(self.word_list[0][0])
        self.show()

    
    def nextWord(self):
        if self.iterator < len(self.word_list)-1:
            self.iterator+=1
        self.ui.word_label.setText(self.word_list[self.iterator][0])
        self.ui.translationText.clear()

    def previousWord(self):
        if self.iterator > 0:
            self.iterator-=1
        self.ui.word_label.setText(self.word_list[self.iterator][0])
        self.ui.translationText.clear()

    def saveAndExit(self):
        output = []
        for word in self.word_list:
            if len(word)>1:
                output.append(word)
        self.word_list = output
        self.close()
        
    def addTranslation(self):
        translation = self.ui.translationText.toPlainText()
        if len(translation) == 0:
            return
        if translation not in self.word_list[self.iterator]:
            self.word_list[self.iterator].append(translation)
        self.ui.translationText.clear()
    
    def deleteWord(self):
        self.blacklist.append(self.word_list[self.iterator][0])
        if len(self.word_list) <= 1:
            self.saveAndExit()
            return

        self.word_list.remove(self.word_list[self.iterator])

        if self.iterator >= len(self.word_list)-1:
            self.iterator-=1

        self.ui.word_label.setText(self.word_list[self.iterator][0])
        
    def getList(self):
        return self.word_list

    def getBlacklist(self):
        return self.blacklist
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    load_srt = NoTranslationController([['apple'], ['pear'], ['orange'], ['pineaple']])
    app.exec_()
    print(load_srt.getList())
    print(load_srt.getBlacklist())
    