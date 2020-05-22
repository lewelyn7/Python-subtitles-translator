from visulalisation_module.load_srt import LoadSrtDialog
from visulalisation_module.export import ExportDialog
from visulalisation_module.no_translation_list import NoTranslationController
from visulalisation_module.export import ExportDialog
from visulalisation_module.most_frequent_list import MostFrequentController
from database_integration_module.db_helpers import DbHelpers
from PyQt5 import QtWidgets
from configs.config_manip import Config
import sys
from os import path

if __name__ == "__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # load_srt = QtWidgets.QDialog()
    # ui = Ui_load_srt()
    # ui.setupUi(load_srt)
    # load_srt.show()
    # sys.exit(app.exec_())
    config = Config("config.yaml")
    config.read()
    dbh = DbHelpers(config.get()["database_filename"])

    dbh.reset_film_stats()

    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    app = QtWidgets.QApplication(sys.argv)



    load_srt = LoadSrtDialog(config)
    app.exec_()



    if load_srt.no_translations_words:
        no_translations = NoTranslationController(load_srt.no_translations_words)
        app.exec_()
        black_list = no_translations.getBlacklist()
        print(black_list)
        for item in black_list:
            dbh.add_to_blacklist(item)

        translated_words = no_translations.getList()
        for item in translated_words:
            dbh.insert_basic_form(item[0], 5.0, item[1:])
            dbh.insert_known_word(item[0], item[0])

    treshold = min(dbh.get_biggest_frequency()*0.7, 10)

    most_frequent_words = dbh.get_most_frequent_words(treshold)
    print(most_frequent_words)
    if most_frequent_words:
        most_frequent = MostFrequentController(most_frequent_words)
        app.exec_()

    score = most_frequent.getScore()
    print(score)
    print(len(most_frequent_words))

    test_dic_list = [{"word": "next", "translation": "nastepny"}, {"word": "today", "translation": "dzisiaj"}]
    to_be_exported = dbh.get_words_from_stats()
    print(to_be_exported)
    export_dialog = ExportDialog(config, to_be_exported, score, len(most_frequent_words))
    app.exec_()
    sys.exit()
