import requests
import json
from .lemmatization_api_ABC import LemmatizationAPI, LemmaAPIError
import logging

class LinguaRobotAPI(LemmatizationAPI):
    """Here we have 2,5k/day so a little better, support for lemmatization"""

    def __init__(self):
        self.url = "https://lingua-robot.p.rapidapi.com/language/v1/entries/en/"
        self.headers = {
        'x-rapidapi-host': "lingua-robot.p.rapidapi.com",
        'x-rapidapi-key': "2405fb23c9msh8dd436952fb8d10p1f59d6jsn97a6bf469ce9"
        }
        self.logger = logging.getLogger("main_logger." + self.__class__.__name__)

    def fetch(self, word):
        self.word = word
        self.response = requests.request("GET", self.url + word, headers=self.headers)

        if self.response.status_code != 200 or len(json.loads(self.response.text)["entries"]) == 0:
            logger.warning("Request returned " + str(self.response.status_code) + " status code")
            raise LemmaAPIError

        self.word_info = json.loads(self.response.text)["entries"][0]

        self.part_of_speeches = []
        for item in self.word_info["lexemes"]:
            self.part_of_speeches.append(item["partOfSpeech"])
            if item["partOfSpeech"] == "verb":
                self.verb_info = item
            elif item["partOfSpeech"] == "noun":
                self.noun_info = item

    def is_verb_conjugated(self):
        root = self.get_basic_verb()
        return root != self.word

    def get_basic_verb(self):   
        return self.verb_info["lemma"]

    def is_noun_plural(self):
        try:
            val = (self.noun_info["forms"][0]["grammar"][0]["number"] == "plural")
        except KeyError:
            return False
        else:
            return val

    def get_singular_noun(self):
        return self.noun_info["lemma"]
