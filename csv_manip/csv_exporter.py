from csv import writer, Error


class ExportError( Exception):
    pass

class CsvExporter:
    def __init__(self):
        pass

    def export(self, word_list, filename, col_order, col_sep, rec_sep):
        """ word_list should be passed as list of dictionaries  TODO correct order"""
        
        outfile = open(filename, "w", newline=rec_sep)
        csvwriter = writer(outfile, delimiter=col_sep)

        try:
            for item in word_list:
                row = []
                if col_order == "translation first":
                    row.append(item["translation"])
                    row.append(item["word"])
                else:
                    row.append(item["word"])
                    row.append(item["translation"])
                csvwriter.writerow(row)
        except Error:
            raise ExportError
        finally:
            outfile.close()