from .wiktionary_en_api import WiktionaryEnAPI
from .linguarobot_api import LinguaRobotAPI
from. conjugation_en_api import ConjugationAPI
from .ultralingua_api import UltraLinguaAPI
from .twinword_api import TwinwordAPI

class WordFilter:
    def __init__(self):
        self.engine = LinguaRobotAPI()
        self.conEngine = ConjugationAPI()
        self.scoringEngine = TwinwordAPI()

    def filter(self, word):
        self.engine.fetch(word)
        part_of_speeches = self.engine.part_of_speeches

        print(part_of_speeches)
        
        basic_form = word
        for part in part_of_speeches:
            if part == 'verb':
                if self.engine.is_verb_conjugated():
                    if not self.conEngine.is_verb_regular(word, self.engine.get_basic_verb()):
                        return word
                    else:
                        basic_form = self.engine.get_basic_verb()

            elif part == 'noun':
                if self.engine.is_noun_plural():
                    if not self.conEngine.is_noun_regular(word, self.engine.get_singular_noun()):
                        return word
                    else:
                        basic_form = self.engine.get_singular_noun()

        return basic_form



