from tinydb import TinyDB, Query

class DictionaryParser:
    """ TODO  """
    def __init__(self, database_file):
        self.db = TinyDB(database_file)

    def parse_dict_file(self, file_name):
        word = {}
        word["word"] = ""
        word["translations"] = []
        new_lines_cnt = 0
        dict_started = False
        new_word = True
        debug_cnt = 0
        with open(file_name, 'r') as inF:

            for line in inF:
                # print("line " + line)
                # if debug_cnt == 50:
                #     assert False, "koniec"
                if line == "\n" or line == "\r\n":
                    new_lines_cnt = new_lines_cnt + 1
                    # print("line  = " + str(new_lines_cnt))

                else:
                    # print(" nie enter " + str(new_lines_cnt))
                    if dict_started == False and new_lines_cnt == 2:
                        dict_started = True
                        new_lines_cnt = 1
                    if dict_started == True:
                        if new_lines_cnt == 1:
                            new_word = True
                            self.db.insert(word)
                            print(str(debug_cnt))
                            word["word"] = ""
                            word["translations"] = []
                        if new_word == True:
                            lst = line.split()
                            word["word"] = lst[0]
                            new_word = False
                        else:
                            word["translations"].append(line[1:])
                    new_lines_cnt = 0
                debug_cnt += 1