from tinydb import TinyDB, Query


class DictAPI:
    """ TODO  """
    def __init__(self, db_file):
        self.db = TinyDB(db_file)

    def get_translation(self, word):
        qr = Query()
        # return [item["translations"] for item in self.db.search(qr.word == word)]
        val = self.db.search(qr.word == word)
        if val:
            return val[0]["translations"]
        else:
            return []