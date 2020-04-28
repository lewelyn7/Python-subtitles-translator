from wiktionaryparser import WiktionaryParser

class w_filter:
    def __init__(self):
        self.wiki_parser = WiktionaryParser()

    def filter(self, word):
        return self.wiktionary_filter(word)

    def is_verb_regular(self, verb, word_info):
        normal_form = (word_info[0]['definitions'][0]['text'][1].split())[-1]

        if normal_form + 'ed' == verb:
            return True
        elif normal_form + 'ing' == verb:
            return True
        else:
            return False
    def is_conjugated(self, verb, word_info):
        text_begining = (word_info[0]['definitions'][0]['text'][1].split())[0]
        return verb != text_begining
    
    def get_regular_verb(self, word_info):
        return (word_info[0]['definitions'][0]['text'][1].split())[-1]

    def wiktionary_filter(self, word):
        word_info = self.wiki_parser.fetch(word)
        partOfSpeech = word_info[0]["definitions"][0]["partOfSpeech"]
        if partOfSpeech == 'verb':
            if self.is_conjugated(word, word_info):
                print("słowo " + word + " jest odmienione ")
                if self.is_verb_regular(word, word_info):
                    return word
                else:
                    return self.get_regular_verb(word_info)
            else:
                print("słowo " + word  + "  jest nieodmienione")
        elif partOfSpeech == 'Noun':
            pass


