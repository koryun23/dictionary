import json
data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    return 'The word does not exist. Please double check it.'
    

word = input("Enter a word: ")

print(translate(word))