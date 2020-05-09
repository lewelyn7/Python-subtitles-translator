import requests
import json
class TwinwordAPI:
    """ Don't use it we have only 10k per month support for language scoring"""

    def __init__(self):        
        self.url = "https://twinword-language-scoring.p.rapidapi.com/text/"
        self.querystring = {"text":"The hippocampus is a major component of the brains of humans and other vertebrates. It belongs to the limbic system and plays important roles in the consolidation of information from short-term memory to long-term memory and spatial navigation. Humans and other mammals have two hippocampi%2C one in each side of the brain. The hippocampus is a part of the cerebral cortex%3B and in primates it is located in the medial temporal lobe%2C underneath the cortical surface. It contains two main interlocking parts%3A Ammon's horn and the dentate gyrus."}
        self.headers = {
            'x-rapidapi-host': "twinword-language-scoring.p.rapidapi.com",
            'x-rapidapi-key': "2405fb23c9msh8dd436952fb8d10p1f59d6jsn97a6bf469ce9"
            }

    def fetch(self, word):
        self.response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        assert self.response.status_code == 200, "Request returned " + str(self.response.status_code) + " status code"
        self.word_info = json.loads(self.response.text)
        self.ten_degree = self.word_info["ten_degree"]
        self.value = self.word_info["value"]