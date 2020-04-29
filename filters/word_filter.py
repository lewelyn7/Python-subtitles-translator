from .wiktionaryAPI import wiktionary_api_filter

class w_filter:
    def __init__(self):
        self.engine = wiktionary_api_filter()

    def filter(self, word):
        return self.engine.filter(word)



