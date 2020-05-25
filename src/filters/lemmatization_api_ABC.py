from abc import ABC, abstractmethod

class LemmaAPIError(Exception):
    pass


class LemmatizationAPI(ABC):

    @abstractmethod
    def fetch(self, word):
        pass

    @abstractmethod
    def is_verb_conjugated(self):
        pass

    @abstractmethod
    def get_basic_verb(self):
        pass

    @abstractmethod
    def is_noun_plural(self):
        pass

    @abstractmethod
    def get_singular_noun(self):
        pass