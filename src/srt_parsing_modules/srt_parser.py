from ..dictionaries.dict_api import DictAPI
from ..database_integration_module.db_helpers import DbHelpers
from ..filters.word_filter import WordFilter, LemmaAPIError

def clean_line(line):
    cleaned_line=""
    for letter in line:
        if letter in ",;:\'1234567890#@$^%&*`~\\(<{[)>}]\"\n":
            continue
        elif letter in "-=+_":
            cleaned_line = cleaned_line + " "
        elif letter in "?.!":
            cleaned_line = cleaned_line + " " + letter
        else:
            cleaned_line = cleaned_line + letter
        
    return cleaned_line


def srt_to_line(srt_file):
    for line in srt_file:
        if line=="":
            continue
        if len(line)<2:
            continue
        if "-->" in line:
            continue
        yield line

def line_to_tokens(line):
    if len(line) < 1:
        yield from[]
    cleaned_line = clean_line(line)
    if len(cleaned_line) < 1:
        yield from[]
    for token in cleaned_line.split(" "):
        if len(token) > 0:
            yield token

def process_srt_file(filename, config, progress_bar_setter=None):
    dictapi = DictAPI("src/dictionaries/eng_pol_dict.json")
    flAPI = WordFilter()

    no_translations = []

    dbh = DbHelpers(config.get()["database_filename"])

    interpunction = "!@#$%^&*()_-=+`~[]\\{}|:\";''<>?,./"
    last_token = ""
    try:
        fil = open(filename)
    except IOError:
        print("file cant be loaded")
        return False
    lines_num = 0
    for line in fil: lines_num += 1
    lines_num /= 2
    fil.seek(0)
    lines = srt_to_line(fil)
    lines_processed = 0
    for line in lines:
        for token in line_to_tokens(line):
            print(token, end=" ")
            if token in interpunction:
                print(" interpunkcja")
            elif last_token != "." and token[0].isupper():
                print(" nazwa wlasna")
                pass # it means that token is nazwa wlasna
            elif token.isupper():
                print(" strange upper word")
                pass # it means that token is strange uppercase word
            elif dbh.in_blacklist(token.lower()):
                print(" w blacklist")
            else:
                token = token.lower()
                if dbh.is_word_known(token):
                    basic_form= dbh.get_basic_form(token)
                    print(" slowo jest znane")
                    dbh.increment_frequency(basic_form)
                else:
                    try:
                        filtered_word = flAPI.filter(token)
                        basic_form = flAPI.get_basic_form()
                    except LemmaAPIError:
                        print(" lemma api error")
                        no_translations.append([token])
                    else:
                        if dbh.is_word_known(filtered_word):
                            print(" slowo nie jest znane ale basic juz jest")
                            dbh.insert_known_word(token, filtered_word)
                        else:
                            print(" kompletnie nie znane slowo")  
                            translations = dictapi.get_translation(filtered_word)
                            if translations == []:
                                translations = dictapi.get_translation(basic_form)
                                if translations != []:
                                    translations.insert(0, "*" + basic_form)
                                else:
                                    no_translations.append([token])
                            if translations:
                                dbh.insert_basic_form(filtered_word, 5.0, translations)
                                dbh.insert_known_word(token, filtered_word)
            last_token = token
        lines_processed += 1
        if progress_bar_setter:
            bar_val = round(lines_processed/lines_num*100.0)
            if(bar_val > 97):
                bar_val = 98
            progress_bar_setter(bar_val)

    if progress_bar_setter:
        progress_bar_setter(100)
    return no_translations