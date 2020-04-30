from .wiktionaryEnAPI import wiktionary_api_filter
from .LinguaRobotAPI import LinguaRobotAPI
class w_filter:
    def __init__(self):
        self.engine = LinguaRobotAPI()

    def filter(self, word):
        return self.engine.filter(word)



