from tinydb import TinyDB, Query


class DictAPI:
    """API class for manipulating offline dictionary stored in TinyDB"""
    def __init__(self, db_file):
        """Constructor takes filename to db json file."""
        self.db = TinyDB(db_file)

    def get_translation(self, word):
        """Returns list of translations."""
        qr = Query()
        val = self.db.search(qr.word == word)
        if val:
            return val[0]["translations"]
        else:
            return []