import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from most_frequent_list_UI import Ui_mostFrequentList

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
        output = ""
        i = 0
        for word in words:
            if i > 2:
                break
            if i > 0:
                output = output + "\n"
            output = output + word.rstrip("\n")
            i+=1
        print(output)
        return output


    def getScore(self):
        output = 0
        for word in self.wordList:
            output+=word[2]
        return output
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    load_srt = MostFrequentController([["is",["byc\n"], 0],  ["do",["robic"], 0],  ["easy",["1. <Adj> \u0142atwy\n", "2. <Adv> \u0142atwo\n", "3. <Adj> swobodny, na luzie\n", "4. idiom easier said than done = \u0142atwiej powiedzie\u0107 ni\u017c zrobi\u0107\n", "5. (nieform) idiom take it/things easy = nie przejmowa\u0107 si\u0119\n", "6. (nieform) idiom go easy on sth = da\u0107 sobie z czym\u015b spok\u00f3j\n", "7. <N Comp> (also easy chair \u02cciz\u026a \u02c8\u02a7e\u0259) fotel\n"], 0],  ["to",["1. wyst\u0119puje z bezokolicznikiem, nie t\u0142umaczone (to love = kocha\u0107)\n", "2. <Prep> (z I form\u0105 czasownika) aby, \u017ceby (he stopped to look at her = stan\u0105\u0142, aby na ni\u0105 spojrze\u0107)\n", "3. (przed rzeczownikiem) cz\u0119sto nie t\u0142umaczone, odpowiada polskiemu celownikowi (he showed the letter to John = pokaza\u0142 Johnowi list)\n", "4. do\n", "5. (wskazywa\u0107) na\n", "6. po  (np. po prawej), z\n", "7. (uldze, wt\u00f3rowi) ku\n", "8. (korzy\u015bci) dla\n", "9. (przy okre\u015blaniu godziny) za (ten to eight = za dziesi\u0119\u0107 \u00f3sma)\n", "10. idiom from ... to ... = od ... do ..., z ... do ...\n", "11. idiom they have been to (Germany) = byli ju\u017c w Niemczech, byli ju\u017c w\n", "12. idiom to and fro = tam i z powrotem, tam i sam\n"], 0],  ["subtitle",["(na filmie) podpis, napis\n"], 0],  ["understand",["rozumie\u0107, pojmowa\u0107\n"], 0]])
    app.exec_()
    list1 = load_srt.getList()
    print(list1)