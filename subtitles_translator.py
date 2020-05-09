from srt_parsing_modules.srt_parser import srt_to_line, line_to_tokens
from csv_importer import csv_importer
from filters.word_filter import WordFilter
from tinydb import TinyDB, Query
from dictionaries.dict_api import DictAPI

def db_insert_wrapper(db, word):
    qur = Query()
    if not db.search(qur.word == word['word']):
        db.insert(word)
        print("dodano: " + word['word'])

def process_srt_file(filename):
    flAPI = WordFilter()
    lines = srt_to_line(filename)
    interpunction = "!@#$%^&*()_-=+`~[]\\{}|:\";''<>?,./".split()
    last_token = ""
    for line in lines:
        for token in line_to_tokens(line):
            if token in interpunction:
                pass # do nothing
            elif last_token != "." and token[0].isupper():
                pass # it means that token is nazwa wlasna
            elif token.isupper():
                pass # it means that token is strange uppercase world
            else:
                if dbw.is_word_known(token):
                    basic_word = dbw.get_basic_form(token)
                    dbw.increment_frequency(token)
                else:
                    basic_form = flAPI.filter(token)
                    if dbw.is_word_known(basic_form):
                        

            last_token = token



if __name__ == "__main__":
    #db section
    # document format: {'word' : <word>, 'translation': <translation>, 'freq' : <freq>}

    anki = csv_importer("testAnki.csv")

    # fl = word_filter()
    dictapi = DictAPI()
    
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

