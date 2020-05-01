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

if __name__ == "__main__":
    file = open('./friends3_but_short.srt')
    lines = srt_to_line(file)
    for line in lines:
        for token in line_to_tokens(line):
            print(token)