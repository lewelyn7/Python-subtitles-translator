from tinydb import TinyDB, Querry

class db_helpers:
    def __init__(self, known_words_path, basic_forms_path, film_stats_path):
        self.dbKnown = TinyDB(known_words_path)
        self.dbBasic = TinyDB(basic_forms_path)
        self.dbStats = TinyDB(film_stats_path)
        
    def is_word_known(self, word):
        found_word = self.dbKnown.search(Querry()['word'] == word)
        #try catch here later
        if found_word:
            return True
        return False

    def get_word(self, word):
        #try catch here later
        if not self.is_word_known(word):
            return None
        basic_form_id = self.dbKnown.search(Querry()['word']==word)[0].doc_id
        basic_form = self.dbBasic.get(doc_id = basic_form_id)
        return basic_form

    def get_basic_form(self, word):
        basic_form_word = self.get_word(word)['word']
        return basic_form_word

    def get_stats(self, word):
        basic_form = self.get_basic_form(word)
        stats = self.dbStats.search(Querry()['wordID'] == basic_form.doc_id)
        return stats[0]

    def increment_frequency(self, word):
        stats = self.get_stats(word)
        current_frequency = stats['frequency']
        current_frequency+=1
        self.dbStats.update({'frequency': current_frequency}, doc_ids=[stats.doc_id])
        return

    def get_most_frequent_words(self, frequency_treshold):
        most_frequent_words = self.dbStats.search(Querry()['frequency'] >= frequency_treshold)
        return most_frequent_words
    
    def insert_film_stats(self, wordID):
        self.dbStats.insert({'frequency': 1, 'wordID': wordID})
        return
    
    def insert_basic_form(self, word, rating, translations):
        word_id = self.dbBasic.insert({'word': word, 'rating': rating, "translations": translations})
        self.insert_film_stats(word_id)
        return

    def insert_known_word(self, word, word_basic_form):
        basic_forms = self.dbBasic.find(Querry()['word'] == word_basic_form)
        #try catch here
        if not basic_forms:
            return None
        self.dbKnown.insert({'word': word, 'basic_formID': basic_forms[0].doc_id})
        return
    
