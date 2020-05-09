from tinydb import TinyDB, Query

class db_helpers:
    def __init__(self,db_path):
        self.db = TinyDB(db_path)
        self.known_words_table = self.db.table('known_words')
        self.basic_forms_table = self.db.table('basic_forms')
        self.film_stats_table = self.db.table('film_stats')

        
    def is_word_known(self, word):
        Words = Query()
        found_word = self.known_words_table.search(Words['word'] == word)
        #try catch here later
        if found_word:
            return True
        return False

    def get_word(self, word):
        #try catch here later
        if not self.is_word_known(word):
            return None
        Words = Query()
        basic_forms = self.known_words_table.search(Words['word'] == word)
        basic_form_id = basic_forms[0].doc_id
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

    def get_most_frequent_words(self, frequency_treshold):
        Stats = Query()
        most_frequent_words = self.film_stats_table.search(Stats['frequency'] >= frequency_treshold)
        return most_frequent_words
    
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
        #try catch here
        if not basic_forms:
            print('no basic form')
            return None
        self.known_words_table.insert({'word': word, 'basic_formID': basic_forms[0].doc_id})
        return
    
    
if __name__ == "__main__":
    db = db_helpers('db.json')
    db.increment_frequency('apples')
    print(db.get_most_frequent_words(1))

