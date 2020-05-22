from tinydb import TinyDB, Query


class DictAPI:
    """ TODO  """
    def __init__(self, db_file):
        self.db = TinyDB(db_file)

    def get_translation(self, word):
        qr = Query()
        return [item["translations"] for item in self.db.search(qr.word == word)]