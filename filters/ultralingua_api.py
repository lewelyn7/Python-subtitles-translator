import requests
import json

class UltraLinguaAPI():
    def __init__(self):
        """ nice people offered us free trial for academic project"""
        self.key = "UXUJKQWMIKHLIPQVHDICH"

    def fetch(self, word):
        self.word = word
        self.word_info = requests.request("GET", "https://api.ultralingua.com/api/2.0/lemmas/en/" + word + "?key=" + self.key)
        assert self.word_info.status_code == 200, "Request returned wrong status code"
        self.part_of_speeches = []
        for item in self.word_info:
            self.part_of_speeches.append(item["partofspeech"]["partofspeechcategory"])
            if item["partofspeech"]["partofspeechcategory"] == "verb":
                self.verb_info = item
            elif item["partofspeech"]["partofspeechcategory"] == "noun":
                self.noun_info = item

    def is_verb_conjugated(self):
        return self.verb_info["root"] == self.word
    
    def get_basic_verb(self):
        return self.verb_info["root"]

    def is_noun_plural(self):
        return self.noun_info["partofspeech"]["number"] == "plural"

    def get_singular_noun(self):
        return self.noun_info["root"]