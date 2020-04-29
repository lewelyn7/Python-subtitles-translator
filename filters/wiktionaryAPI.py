from wiktionaryparser import WiktionaryParser
from .API import API
import re

class wiktionary_api_filter(API):
    def __init__(self):
        self.wiki_parser = WiktionaryParser()

    def filter(self, word):
        return self.wiktionary_filter(word)

    def is_verb_conjugated(self, verb, definitions_info):
        pat = re.compile('.*of.*')
        return pat.match(definitions_info['text'][1]) != None
    
    def get_basic_verb(self, definitions_info):
        return (definitions_info['text'][1].split())[-1]

    def is_noun_plural(self, definitions_info):
        pat = re.compile('.*plural of.*')
        return pat.match(definitions_info['text'][1]) != None

    def get_singular_noun(self, definitions_info):
        return (definitions_info['text'][1].split())[-1]

    def wiktionary_filter(self, word):
        word_info = self.wiki_parser.fetch(word)
        defin = word_info[0]["definitions"]
        definitions_info = word_info[0]['definitions'][0]
        part_of_speeches = []
        for item in defin:
            part_of_speeches.append(item["partOfSpeech"].lower())

        print(part_of_speeches)
        # assert len(word_info[0]['definitions']) != 1, "word is a verb and noun too"
        basic_form = word
        for part in part_of_speeches:
            if part == 'verb':
                if self.is_verb_conjugated(word, definitions_info):
                    if not self.is_verb_regular(word, self.get_basic_verb(definitions_info)):
                        return word
                    else:
                        basic_form = self.get_basic_verb(definitions_info)

            elif part == 'noun':
                if self.is_noun_plural(definitions_info):
                    if not self.is_noun_regular(word, self.get_singular_noun(definitions_info)):
                        return word
                    else:
                        basic_form = self.get_singular_noun(definitions_info)

        return basic_form



