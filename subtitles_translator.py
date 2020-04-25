from srt_parser import parse_srt

if __name__ == "__main__":
    srt_file = open("example_srt_file.txt", "r")
    srt_words = parse_srt(srt_file)
    for word in srt_words:
        print(word)