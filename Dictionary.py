import json
import difflib

data = json.load(open("076 data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The Word Does Not exist!"

word = input("Enter Word:")

print(translate(word))