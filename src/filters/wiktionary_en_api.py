from wiktionaryparser import WiktionaryParser
import re
from .lemmatization_api_ABC import LemmatizationAPI, LemmaAPIError

class WiktionaryEnAPI:
    def __init__(self):
        self.wiki_parser = WiktionaryParser()

    def fetch(self, word):
        self.word_info = self.wiki_parser.fetch(word)
        self.definitions_info = self.word_info[0]['definitions']
        self.part_of_speeches = []
        for item in self.definitions_info:
            self.part_of_speeches.append(item["partOfSpeech"].lower())
            if item["partOfSpeech"].lower() == "verb":
                self.verb_definition = item["text"]
            elif item["partOfSpeech"].lower() == "noun":
                self.noun_definition = item["text"]

    def is_verb_conjugated(self):
        pat = re.compile('.*of.*')
        return pat.match(self.verb_definition[1]) != None
    
    def get_basic_verb(self):
        return (self.verb_definition[1].split())[-1]

    def is_noun_plural(self):
        pat = re.compile('.*plural of.*')
        return pat.match(self.noun_definition[1]) != None

    def get_singular_noun(self):
        return (self.noun_definition[1].split())[-1]




