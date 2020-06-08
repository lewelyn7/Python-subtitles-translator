from csv import writer, Error


class ExportError( Exception):
    pass

class CsvExporter:
    """Exporter of words to csv file."""
    def __init__(self):
        pass

    def export(self, word_list, filename, translation_first, col_sep, rec_sep, include_header, translations_max):
        """
        Exports word_list dictionary to a csv file.

        Parameteres:
            word_list(dict): dictionary with words
            filename(str): filename
            translation_first(boolean): if translation has to be in first column, set to True
            col_sep(char): column separator in the exported csv file
            include_header(boolean): obvious
            translation_max(int): maximum number of translations to be exported

        Raises:
            ExportError: in case of any failure
        """

        outfile = open(filename, "w", newline=rec_sep)
        csvwriter = writer(outfile, delimiter=col_sep)

        try:
            if include_header:
                row = []
                if translation_first == True:
                    row.append("translation")
                    row.append("word")
                else:
                    row.append("word")
                    row.append("translation")
                csvwriter.writerow(row)                

            for item in word_list:
                translations_string = ""
                for i in range(translations_max):
                    if i < len(item["translations"]):
                        translations_string += item["translations"][i].replace("\n", "")
                        translations_string += " "
                row = []
                if translation_first == True:
                    row.append(translations_string)
                    row.append(item["word"])
                else:
                    row.append(item["word"])
                    row.append(item["translations"])
                csvwriter.writerow(row)
        except Error:
            raise ExportError
        finally:
            outfile.close()