from csv import reader, Error
import re

class ImportError(Exception):
    pass


class csv_importer:
    """
    Importer for using with Anki or Quizlet, file should be in csv format with comma as a delitmer
    and new line to indicate new row ( new word ).
    """

    def __init__(self, filename, header=False, translation_first=True):
        """
        Constructor accepts csv filename and optional header argument and order of words in csv fie.
        
        Parameters:
            filename(str): path to imported file
            header(boolean): does file include header?
            translation_first(boolean): if translation is in first column
        """
         
        try:
            assert re.match(r".*\.csv$", filename), "file has wrong extension"
            self.filename = filename
            self.header = header
            self.translation_first = translation_first
        except AssertionError as inst:
            print("assert error", inst.args)

    def read(self):
        """
        Reads from file with parameters gicen in constructor.

        Returns:
            Generator over tuple (translation, word)

        Raises:
            ImportError: in case of IOError e.g.
        """

        try:
            csvfile = open(self.filename)
        except IOError:
            print("can't open csv file")
            csvfile.close()
            raise ImportError
        else:
            try:
                csvreader = reader(csvfile)
                if self.header == True:
                    next(csvreader)
                for row in csvreader:
                    # normalize strings
                    row[0] = row[0].lower().strip()
                    row[1] = row[1].lower().strip()
                    if self.translation_first == True:
                        yield (row[0], row[1])
                    else:
                        yield (row[1], row[0])
            except Error:
                raise ImportError
            finally:
                csvfile.close()
        

