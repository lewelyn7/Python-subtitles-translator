from srt_parser import parse_srt
from csv_importer import csv_importer

if __name__ == "__main__":
    # srt_file = open("example_srt_file.txt", "r")
    # srt_words = parse_srt(srt_file)
    # for word in srt_words:
    #     print(word)
    
    anki = csv_importer("testAnki.csvd")
    for word in anki.read():
        print( word[0] + " - " + word[1])