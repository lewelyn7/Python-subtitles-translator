from srt_parsing_modules.srt_parser import srt_to_line, line_to_tokens
from csv_importer import csv_importer
from filters.word_filter import WordFilter
from tinydb import TinyDB, Query
from dictionaries.dict_api import DictAPI
from database_integration_module.db_helpers import db_helpers

def db_insert_wrapper(db, word):
    qur = Query()
    if not db.search(qur.word == word['word']):
        db.insert(word)
        print("dodano: " + word['word'])

def process_srt_file(filename):
    dictapi = DictAPI("dictionaries/eng_pol_dict.json")
    flAPI = WordFilter()

    dbh = db_helpers("db_test.json")

    interpunction = "!@#$%^&*()_-=+`~[]\\{}|:\";''<>?,./".split()
    last_token = ""
    fil = open(filename)
    lines = srt_to_line(fil)
    for line in lines:
        for token in line_to_tokens(line):
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
                    basic_form = flAPI.filter(token)
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
                        dbh.insert_basic_form(token, 5.0, translations)
                        dbh.insert_known_word(token, token)
                        

            last_token = token



if __name__ == "__main__":
    #db section
    # document format: {'word' : <word>, 'translation': <translation>, 'freq' : <freq>}

    anki = csv_importer("testAnki.csv")

    # fl = word_filter()

    
    # srt_file = open("friends3_but_short.srt", "r")
    # srt_words = parse_srt(srt_file)
    # for word in srt_words:
    #     print(word + " podstawowa forma " + fl.filter(word.lower()))


    # for word in anki.read():
    #     db_item = {}
    #     # print( word[0] + " - " + word[1])
    #     db_item['word'] = word[0]
    #     db_item['translation'] = word[1]
    #     db_insert_wrapper(db, db_item)

