import requests
from .conjugationEnAPI import conjugationAPI
import json

class LinguaRobotAPI(conjugationAPI):
    """Here we have 2,5k/day so a little better, support for lemmatization"""

    def __init__(self):
        self.url = "https://lingua-robot.p.rapidapi.com/language/v1/entries/en/"
        self.headers = {
        'x-rapidapi-host': "lingua-robot.p.rapidapi.com",
        'x-rapidapi-key': "2405fb23c9msh8dd436952fb8d10p1f59d6jsn97a6bf469ce9"
        }

    def filter(self, word):
        self.get_JSON(word)
        return self.linguarobot_filter(word)

    def get_JSON(self, word):
        self.response = json.loads(requests.request("GET", self.url + word, headers=self.headers).text)
        # return self.response

    def get_root(self, entry):
        return entry['lexemes']['lemma']

    def is_verb_conjugated(self, verb, lexem):
        root = self.get_basic_verb(lexem)
        return root != verb
    
    def get_basic_verb(self, lexem):
        return lexem['lemma']

    def is_noun_plural(self, lexem):
        return lexem['forms'][0]['grammar'][0]['number'][0] == "plural"

    def get_singular_noun(self, lexem):
        return lexem['lemma']

    def linguarobot_filter(self, word):
        # assert len(word_info[0]['definitions']) != 1, "word is a verb and noun too"
        basic_form = word
        for lexem in self.response['entries'][0]['lexemes']:
            part = lexem['partOfSpeech']
            if part == 'verb':
                if self.is_verb_conjugated(word, lexem):
                    if not self.is_verb_regular(word, self.get_basic_verb(lexem)):
                        return word
                    else:
                        basic_form = self.get_basic_verb(lexem)

            elif part == 'noun':
                if self.is_noun_plural(lexem):
                    if not self.is_noun_regular(word, self.get_singular_noun(lexem)):
                        return word
                    else:
                        basic_form = self.get_singular_noun(lexem)

        return basic_form
