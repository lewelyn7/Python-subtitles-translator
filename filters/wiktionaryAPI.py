from wiktionaryparser import WiktionaryParser
import re

class wiktionary_api_filter:
    def __init__(self):
        self.wiki_parser = WiktionaryParser()

    def filter(self, word):
        return self.wiktionary_filter(word)

    def is_verb_conjugated(self, verb, definitions_info):
        pat = re.compile('.*of.*')
        return pat.match(definitions_info['text'][1]) != None
    
    def get_basic_verb(self, definitions_info):
        return (definitions_info['text'][1].split())[-1]
    
    def is_verb_regular(self, verb, definitions_info):
        normal_form = self.get_basic_verb(definitions_info)

        if normal_form + 'ed' == verb:
            return True
        elif normal_form + 'ing' == verb:
            return True
        elif normal_form + 's' == verb:
            return True
        else:
            return False

    def is_noun_plural(self, definitions_info):
        pat = re.compile('.*plural of.*')
        return pat.match(definitions_info['text'][1]) != None

    def get_singular_noun(self, definitions_info):
        return (definitions_info['text'][1].split())[-1]

    def is_noun_regular(self, word, definitions_info):
        normal = self.get_singular_noun(definitions_info)

        if word == normal + "s":
            return True
        else:
            return False

    def wiktionary_filter(self, word):
        word_info = self.wiki_parser.fetch(word)
        partOfSpeech = word_info[0]["definitions"][0]["partOfSpeech"].lower()
        definitions_info = word_info[0]['definitions'][0]
        
        # assert len(word_info[0]['definitions']) != 1, "word is a verb and noun too"

        if partOfSpeech == 'verb':

            if self.is_verb_conjugated(word, definitions_info):

                if self.is_verb_regular(word, definitions_info):
                    return self.get_basic_verb(definitions_info)
                else:
                    return word

        elif partOfSpeech == 'noun':
            if self.is_noun_plural(definitions_info):
                if self.is_noun_regular(word, definitions_info):
                    return self.get_singular_noun(definitions_info)
                else:
                    return word

        return word



