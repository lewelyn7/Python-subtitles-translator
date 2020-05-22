from csv import writer, Error


class ExportError( Exception):
    pass

class CsvExporter:
    def __init__(self):
        pass

    def export(self, word_list, filename, col_order, col_sep, rec_sep, include_header):
        """ word_list should be passed as list of dictionaries  TODO correct order"""
        
        outfile = open(filename, "w", newline=rec_sep)
        csvwriter = writer(outfile, delimiter=col_sep)

        try:
            if include_header:
                row = []
                if col_order == "translation first":
                    row.append("translation")
                    row.append("word")
                else:
                    row.append("word")
                    row.append("translation")
                csvwriter.writerow(row)                

            for item in word_list:
                print(item["translations"])
                row = []
                if col_order == "translation first":
                    row.append(str(item["translations"])) # TODO
                    row.append(item["word"])
                else:
                    row.append(item["word"])
                    row.append(item["translations"])
                csvwriter.writerow(row)
        except Error:
            raise ExportError
        finally:
            outfile.close()