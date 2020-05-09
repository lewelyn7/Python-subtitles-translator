from tinydb import TinyDB, Query

class DictAPI:
    """ TODO  """
    def __init__(self):
        self.db = TinyDB('dictionaries/eng_pol_dict.json')

    def get_translation(self, word):
        qr = Query()
        return self.db.search(qr.word == word)