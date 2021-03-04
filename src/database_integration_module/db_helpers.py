from tinydb import TinyDB, Query


class DbHelpers(Exception):
    """Provides methods for accessing data stored in database."""
    unchecked_get_exception = Exception("Getter used without checking if the value exists.")

    def __init__(self,db_path):
        self.db_path = db_path
        self.db = TinyDB(db_path)
        self.known_words_table = self.db.table('known_words')
        self.basic_forms_table = self.db.table('basic_forms')
        self.film_stats_table = self.db.table('film_stats')
        self.blacklist_table = self.db.table('blacklist')

        
    def is_word_known(self, word):
        """Checks if word is stored in the database as one of the alredy processed words.

        Args:
            word (string): word to check

        Returns:
            bool: information if the word is stored.
        """
        Words = Query()
        found_word = self.known_words_table.search(Words['word'] == word)
        if found_word:
            return True
        return False

    def get_word(self, word):
        """Gets data associated with the given words basic form.

        Args:
            word (string): Word of which basic form data to get.

        Raises:
            self.unchecked_get_exception: Throws when there is no data associated with the given word.

        Returns:
            Map : Data stored in the database connected to a given basic form.
        """
        if not self.is_word_known(word):
            raise self.unchecked_get_exception
        Words = Query()
        basic_forms = self.known_words_table.search(Words['word'] == word)
        basic_form_id = basic_forms[0]['basic_formID']
        basic_form = self.basic_forms_table.get(doc_id = basic_form_id)
        return basic_form

    def get_basic_form(self, word):
        """Returns the basic form of a given word.

        Args:
            word (string): Word of which basic form to get.

        Returns:
            string: The basic form of a given word.
        """
        basic_form_word = self.get_word(word)['word']
        return basic_form_word

    def get_stats(self, word):
        """Returns statistics associated with the given word. The statistics are bound to the last translated srt file. 

        Args:
            word (string): Word of which basic form to get.

        Returns:
            Map: Map representing the statistics entitty in database connected to the given word.
        """
        basic_form = self.get_word(word)
        Stats = Query()
        stats = self.film_stats_table.search(Stats['wordID'] == basic_form.doc_id)
        if not stats:
            self.insert_film_stats(basic_form.doc_id)
            stats = self.film_stats_table.search(Stats['wordID'] == basic_form.doc_id)
            
        return stats[0]

    def increment_frequency(self, word):
        """Increments the frequency statistic of a given word in the database.

        Args:
            word (string): The word of which frequency to increment.
        """
        stats = self.get_stats(word)
        current_frequency = stats['frequency']
        current_frequency+=1
        self.film_stats_table.update({'frequency': current_frequency}, doc_ids=[stats.doc_id])
        return

    def get_words_from_stats(self):
        """Returns all words that have stats associated to them(of the currently translated srt file).

        Returns:
            List<Map>: A list of maps representing each word as a basic form entitty.
        """
        most_frequent_words = [stat['wordID'] for stat in self.film_stats_table.all()]
        output = []
        for id in most_frequent_words:
            output.append(self.basic_forms_table.get(doc_id = id))
        return output

    def get_most_frequent_words(self, treshold):
        """The function gets a specially formated list of words with translations that have a frequency above treshold. The main pourpose of this function is to have its output pluggged into the most_frequent_list.py class.

        Args:
            treshold (int): A minimum value of requency that the word has to have to be outputted.

        Returns:
            List: A list of 3 attributes: the word itself, a list of translations for a given word, and 0.
        """
        most_frequent_words = [stat['wordID'] for stat in self.film_stats_table.search(Query()['frequency']>=treshold)]
        output = []
        for id in most_frequent_words:
            output.append(self.basic_forms_table.get(doc_id = id))
        output = [[value['word'], value['translations'], 0] for value in output]
        return output
    
    def insert_film_stats(self, wordID):
        """Helper function that inserts word into the film_stats table. Should only be accessed by another function of this class.

        Args:
            wordID (int): Id of the word to be inserted.
        """
        self.film_stats_table.insert({'frequency': 1, 'wordID': wordID})
        return
    
    def insert_basic_form(self, word, rating, translations):
        """Creates a basic form entitty and inserts it into the basic_forms table.

        Args:
            word (string): Basic form of the word.
            rating (int): Words rating.
            translations (List<string>): List of translations.
        """
        word_id = self.basic_forms_table.insert({'word': word, 'rating': rating, "translations": translations})
        self.insert_film_stats(word_id)
        return

    def insert_known_word(self, word, word_basic_form):
        """Creates a known_words entitty and inserts it into the basic_forms table.

        Args:
            word (string): Word to be inserted.
            word_basic_form (string): The basic form of the word.

        Raises:
            self.unchecked_get_exception: Throws when basic form entitty doesnt exist.
        """
        
        Forms = Query()
        basic_forms = self.basic_forms_table.search(Forms['word'] == word_basic_form)
        if not basic_forms:
            raise self.unchecked_get_exception
        self.known_words_table.insert({'word': word, 'basic_formID': basic_forms[0].doc_id})
        return

    def in_blacklist(self, word):
        """Checks if word is blacklisted.

        Args:
            word (string): Word to check.

        Returns:
            bool: Is the word is blacklisted.
        """
        blacklisted_words = self.blacklist_table.search(Query()['word'] == word)
        if len(blacklisted_words)==0:
            return False
        return True
        
    def add_to_blacklist(self, word):
        """Adds word to blacklist.

        Args:
            word (string): Word to add.
        """
        if not self.in_blacklist(word):
            self.blacklist_table.insert({'word': word})

    def get_biggest_frequency(self):
        """Gets the frequency of the most frequent word.

        Returns:
            int: The frequency.
        """
        words = self.film_stats_table.all()
        most_frequent_word = words[0]
        for word in words:
            if most_frequent_word['frequency'] < word['frequency']:
                most_frequent_word = word

        return most_frequent_word['frequency']
    
    def reset_film_stats(self):
        """Clears film stats.
        """
        self.film_stats_table.truncate()

    
if __name__ == "__main__":
    db = DbHelpers('db.json')
    print(db.get_most_frequent_words(1))

