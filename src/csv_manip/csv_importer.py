from csv import reader, Error
import re

class ImportError(Exception):
    pass


class csv_importer:
    """Importer for using with Anki or Quizlet, file should be in csv format with comma as a delitmer
    and new line to indicate new row ( new word )"""

    def __init__(self, filename, header=False, firstcol="mylang"):
        """ Constructor accepts csv filename and optional header argument and order of words in csv fie.
         If translations are placed in first column, then firstcol should be set to "translations" """
         
        try:
            assert re.match(".*\.csv$", filename), "file has wrong extension"
            self.filename = filename
            self.header = header
            self.firstcol = firstcol
        except AssertionError as inst:
            print("assert error", inst.args)

    def read(self):
        """ returns an iterator over tuple of words (word, translation) in csvfile"""

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
                    if self.firstcol == "mylang":
                        yield (row[0], row[1])
                    else:
                        yield (row[1], row[0])
            except Error:
                raise ImportError
            finally:
                csvfile.close()
        
