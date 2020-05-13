from tinydb import TinyDB, Query


class DbHelpers(Exception):
    unchecked_get_exception = Exception("Getter used without checking if the value exists.")

    def __init__(self,db_path):
        self.db = TinyDB(db_path)
        self.known_words_table = self.db.table('known_words')
        self.basic_forms_table = self.db.table('basic_forms')
        self.film_stats_table = self.db.table('film_stats')
        self.blacklist_table = self.db.table('blacklist')

        
    def is_word_known(self, word):
        Words = Query()
        found_word = self.known_words_table.search(Words['word'] == word)
        if found_word:
            return True
        return False

    def get_word(self, word):
        if not self.is_word_known(word):
            raise self.unchecked_get_exception
        Words = Query()
        basic_forms = self.known_words_table.search(Words['word'] == word)
        basic_form_id = basic_forms[0]['basic_formID']
        basic_form = self.basic_forms_table.get(doc_id = basic_form_id)
        return basic_form

    def get_basic_form(self, word):
        basic_form_word = self.get_word(word)['word']
        return basic_form_word

    def get_stats(self, word):
        basic_form = self.get_word(word)
        Stats = Query()
        stats = self.film_stats_table.search(Stats['wordID'] == basic_form.doc_id)
        return stats[0]

    def increment_frequency(self, word):
        stats = self.get_stats(word)
        current_frequency = stats['frequency']
        current_frequency+=1
        self.film_stats_table.update({'frequency': current_frequency}, doc_ids=[stats.doc_id])
        return

    def get_words_from_stats(self):
        most_frequent_words = [stat['wordID'] for stat in self.film_stats_table.all()]
        output = []
        for id in most_frequent_words:
            output.append(self.basic_forms_table.get(doc_id = id))
        return output

    def get_most_frequent_words(self, treshold):
        most_frequent_words = [stat['wordID'] for stat in self.film_stats_table.search(Query()['frequency']>=treshold)]
        output = []
        for id in most_frequent_words:
            output.append(self.basic_forms_table.get(doc_id = id))
        return output
    
    def insert_film_stats(self, wordID):
        self.film_stats_table.insert({'frequency': 1, 'wordID': wordID})
        return
    
    def insert_basic_form(self, word, rating, translations):
        word_id = self.basic_forms_table.insert({'word': word, 'rating': rating, "translations": translations})
        self.insert_film_stats(word_id)
        return

    def insert_known_word(self, word, word_basic_form):
        Forms = Query()
        basic_forms = self.basic_forms_table.search(Forms['word'] == word_basic_form)
        if not basic_forms:
            raise self.unchecked_get_exception
        self.known_words_table.insert({'word': word, 'basic_formID': basic_forms[0].doc_id})
        return

    def in_blacklist(self, word):
        blacklisted_words = self.blacklist_table.search(Query()['word'] == word)
        if len(blacklisted_words)==0:
            return False
        return True
        
    def add_to_blacklist(self, word):
        if not self.in_blacklist(word):
            self.blacklist_table.insert({'word': word})

    def get_biggest_frequency(self):
        words = self.film_stats_table.all()
        most_frequent_word = words[0]
        for word in words:
            if most_frequent_word['frequency'] < word['frequency']:
                most_frequent_word = word

        return most_frequent_word['frequency']
    
    
if __name__ == "__main__":
    db = DbHelpers('db.json')
    print(db.get_most_frequent_words(1))

