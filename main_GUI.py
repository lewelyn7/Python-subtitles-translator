from src.visulalisation_module.load_srt import LoadSrtDialog
from src.visulalisation_module.export import ExportDialog
from src.visulalisation_module.no_translation_list import NoTranslationController
from src.visulalisation_module.export import ExportDialog
from src.visulalisation_module.most_frequent_list import MostFrequentController
from src.database_integration_module.db_helpers import DbHelpers
from PyQt5 import QtWidgets
from src.config_manip.config_manip import Config
import sys
from os import path
import logging

if __name__ == "__main__":

    #config
    config = Config("configs/config.yaml")
    config.read()
    
    #database
    dbh = DbHelpers(config.get()["database_filename"])
    dbh.reset_film_stats()


    #logging module
    logger = logging.getLogger("main_logger")
    logger.setLevel(logging.INFO)
    err_stream_handler = logging.StreamHandler()
    err_stream_handler.setLevel(logging.WARNING)
    log_file_handler = logging.FileHandler(config.get()["logs_filename"])
    log_file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s:%(levelname)s: %(message)s')
    err_stream_handler.setFormatter(formatter)
    log_file_handler.setFormatter(formatter)
    logger.addHandler(log_file_handler)
    logger.addHandler(err_stream_handler)


    #GUI
    app = QtWidgets.QApplication(sys.argv)
    load_srt = LoadSrtDialog(config)
    app.exec_()

    if load_srt.no_translations_words:
        logger.info("number of words without translation: %d", len(load_srt.no_translations_words))
        no_translations = NoTranslationController(load_srt.no_translations_words)
        app.exec_()
        black_list = no_translations.getBlacklist()
        for item in black_list:
            dbh.add_to_blacklist(item)

        translated_words = no_translations.getList()
        for item in translated_words:
            dbh.insert_basic_form(item[0], 5.0, item[1:])
            dbh.insert_known_word(item[0], item[0])

    treshold = min(dbh.get_biggest_frequency()*0.7, 10)

    most_frequent_words = dbh.get_most_frequent_words(treshold)
    logger.info("number of most frequent words: %d", len(most_frequent_words))
    if most_frequent_words:
        most_frequent = MostFrequentController(most_frequent_words)
        app.exec_()

    score = most_frequent.getScore()
    known_words = most_frequent.get_known_words()
    logger.info("most frequent score: %d", score)

    from_stats = dbh.get_words_from_stats()
    to_be_exported = []
    for word in from_stats:
        if word['word'] not in known_words:
            to_be_exported.append(word)


    logger.info("number of words to be exported: %d", len(to_be_exported))
    export_dialog = ExportDialog(config, to_be_exported, score, len(most_frequent_words))
    app.exec_()
    sys.exit()
