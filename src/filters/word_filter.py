from .wiktionary_en_api import WiktionaryEnAPI
from .linguarobot_api import LinguaRobotAPI
from. conjugation_en_api import ConjugationAPI
from .ultralingua_api import UltraLinguaAPI
from .twinword_api import TwinwordAPI
from .lemmatization_api_ABC import LemmaAPIError
import socket
class WordFilter:
    def __init__(self):
        self.engine = UltraLinguaAPI()
        self.conEngine = ConjugationAPI()

    def filter(self, word):
        """
        Returns form of a word that should be put in the database,
        so it's either basic form of a word or conjungated form in case of
        irregular conjungation.

        Raises:
            LemaAPIError: raised in case of lemmatization api error e.g. connection problem
        """
            
        word = word.lower()
        try:
            self.engine.fetch(word)
        except socket.error:
            raise LemmaAPIError
        part_of_speeches = self.engine.part_of_speeches

        # print(part_of_speeches)
        
        self.basic_form = word
        for part in part_of_speeches:
            if part == 'verb':
                if self.engine.is_verb_conjugated():
                    if not self.conEngine.is_verb_regular(word, self.engine.get_basic_verb()):
                        self.basic_form = self.engine.get_basic_verb()
                        return word
                    else:
                        self.basic_form = self.engine.get_basic_verb()

            elif part == 'noun':
                if self.engine.is_noun_plural():
                    if not self.conEngine.is_noun_regular(word, self.engine.get_singular_noun()):
                        self.basic_form = self.engine.get_singular_noun()                        
                        return word
                    else:
                        self.basic_form = self.engine.get_singular_noun()

        return self.basic_form

    def get_basic_form(self):
        """Returns basic form of word fetched by a filter method. So filter method should be called firs."""
        return self.basic_form

