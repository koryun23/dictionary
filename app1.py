import json
from difflib import SequenceMatcher, get_close_matches
data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()] 
    elif len(get_close_matches(word, data.keys())) > 0:
        print('Did you mean %s instead?' % get_close_matches(word, data.keys())[0])
        validation = input("press Y if yes or N if no: ")
        if validation == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif validation == 'N':
            return 'The word does not exist. Please double check it.'
        else:
            return "We didn't understand your entry"
    return 'The word does not exist. Please double check it.'

waiting = True
while waiting:
    word = input("Enter a word: ")
    output = translate(word)
    if type(output) ==  list:
        for item in output:
            print(item)
    else:
        print(output)
    stop = input("do you want to close the program? Y/N ")
    if stop == "Y":
        waiting = False
