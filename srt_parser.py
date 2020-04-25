def clean_line(line):
    cleaned_line=""
    for letter in line:
        if letter not in "(<{[)>}]\"":
            cleaned_line+=letter
    return cleaned_line

def clean_word(word):
    cleaned_word = ""
    if word[0]=='\'':
        word = word[1:]
    if word[-1]=='\'':
        word = word[0:-1]
    for letter in word:
        if letter not in "-.:;,?!":
            cleaned_word+=letter
        elif letter not in ".:;,?!":
            cleaned_word+=' '
    return cleaned_word

def parse_srt(srt_file):
    for line in srt_file:
        if line=="":
            break
        if len(line)<2:
            break
        if line.find("-->") != -1:
            break
        line = clean_line(line)
        words = [word for word in line.split(' ') if len(word) > 0]
        for i in range(len(words)):
            word = words[i]
            if not word.isalpha():
                break
            if i == 0 or words[i-1][-1] in '.!?':
                yield word
            if word.islower():
                yield word
            if word.isupper():
                yield word
        line = srt_file.readline()