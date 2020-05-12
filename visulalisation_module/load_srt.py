from PyQt5 import QtCore, QtGui, QtWidgets
from .load_srt_UI import Ui_load_srt
from configs.config_manip import Config
from os import getcwd

from srt_parsing_modules.srt_parser import srt_to_line, line_to_tokens
from filters.word_filter import WordFilter, LemmaAPIError
from dictionaries.dict_api import DictAPI
from database_integration_module.db_helpers import db_helpers
#co poradzic co poradzic
def process_srt_file(filename, bar, config):
    dictapi = DictAPI("dictionaries/eng_pol_dict.json")
    flAPI = WordFilter()

    no_translations = []
    no_lemma = []

    dbh = db_helpers(config.get()["database_filename"])

    interpunction = "!@#$%^&*()_-=+`~[]\\{}|:\";''<>?,./".split()
    last_token = ""
    try:
        fil = open(filename)
    except IOError:
        print("file cant be loaded")
        return False
    lines_num = 0
    for line in fil: lines_num += 1
    lines_num /= 2
    fil.seek(0)
    lines = srt_to_line(fil)
    lines_processed = 0
    for line in lines:
        for token in line_to_tokens(line):
            print(token)
            if token in interpunction:
                print(token + " interpunkcja")
            elif last_token != "." and token[0].isupper():
                print(token + " nazwa wlasna")
                pass # it means that token is nazwa wlasna
            elif token.isupper():
                print(token + " strange upper word")
                pass # it means that token is strange uppercase word
            else:
                if dbh.is_word_known(token):
                    basic_form= dbh.get_basic_form(token)
                    print(token  + " slowo jest znane slowo")
                    dbh.increment_frequency(basic_form)
                else:
                    try:
                        basic_form = flAPI.filter(token)
                    except LemmaAPIError:
                        no_lemma.append([token])
                    else:
                        if dbh.is_word_known(basic_form):
                            print(token + " slowo nie jest znane ale basic juz jest")
                            dbh.insert_known_word(token, basic_form)
                        else:
                            print(token + " kompletnie nie znane slowo")
                            # co robimy jak jest nieregularna odmiana bo fajnie jest sie nauczyc nieregularnej odmiany 
                            # ale z slownik nie przetlumaczy odmienionych slow
                            # dlatego moznaby do bazy wrzucac odmienione slowo z tłumaczeniem nieodmienionego i dać adnnotacje
                            # ze uwaga to jest odmienione  uzytkowniku sprawdz ta fiszke i ewentualnie popraw
                            # albo co jak nie znaleziono tlumaczenia dla slowa
                            # albo scoringu     
                            translations = dictapi.get_translation(token)
                            if translations == []:
                                translations = dictapi.get_translation(basic_form)
                                if translations != []:
                                    translations.insert(0, "*" + basic_form)
                                else:
                                    no_translations.append([token])
                            
                            dbh.insert_basic_form(token, 5.0, translations)
                            dbh.insert_known_word(token, token)
            last_token = token
        lines_processed += 1
        bar_val = round(lines_processed/lines_num*100.0)
        if(bar_val > 94):
            bar_val = 95
        bar.setValue(bar_val)
    bar.setValue(100)
    return (no_translations, no_lemma)

class LoadSrtDialog(QtWidgets.QDialog):
    def __init__(self, config):
        super(LoadSrtDialog, self).__init__()

        self.config = config

        self.ui = Ui_load_srt()
        self.ui.setupUi(self)
        self.cfg = self.config.get()
        self.ui.word_lemma_combo.setCurrentText(self.cfg["word_lemmatization_API"])
        self.ui.word_scoring_combo.setCurrentText(self.cfg["word_scoring_API"])
        self.ui.word_trans_combo.setCurrentText(self.cfg["word_translation_API"])
        self.ui.select_file_btn_2.setText(self.cfg["database_filename"].split("/")[-1])
        
        self.show()
    def load_file_action(self): #srt file I mean
        self.ui.load_btn.setText("loading...")
        tup = process_srt_file(self.filename, self.ui.progressBar, self.config)
        print(tup)

    def open_file_dialog(self): # srt file
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', getcwd())
        self.filename = fname[0]
        if(self.filename == ""):
            self.ui.select_file_btn.setText("select file")
        else:
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

