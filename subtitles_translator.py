#from .srt_parsing_modules.srt_parser import parse_srt
from csv_importer import csv_importer
from filters.word_filter import word_filter
from tinydb import TinyDB, Query

def db_insert_wrapper(db, word):
    qur = Query()
    if not db.search(qur.word == word['word']):
        db.insert(word)
        print("dodano: " + word['word'])

if __name__ == "__main__":
    #db section
    db = TinyDB('db.json')
    # document format: {'word' : <word>, 'translation': <translation>, 'freq' : <freq>}

    anki = csv_importer("testAnki.csv")

    fl = word_filter()
    
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

