from csv import writer, Error


class ExportError( Exception):
    pass

class CsvExporter:
    def __init__(self):
        pass

    def export(self, word_list, filename, col_order, col_sep, rec_sep, translation_first):
        """ word_list should be passed as list of lists  TODO correct order"""
        
        outfile = open(filename, "w", newline=rec_sep)
        csvwriter = writer(outfile, delimiter=col_sep)

        try:
            for row in word_list:
                    csvwriter.writerow(row)
        except Error:
            raise ExportError
        finally:
            outfile.close()