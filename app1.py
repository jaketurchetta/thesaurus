import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    pn = w.capitalize()
    if w in data:
        return data[w]
    elif pn in data:
        return data[pn]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no. " % get_close_matches(w, data.keys(), cutoff=0.8)[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys(), cutoff=0.8)[0]]
        elif yn == "N":
            return "Word not found. Please validate your input and try again. "
        else:
            return "We did not undertand your entry. "
    else:
        return "Word not found. Please validate your input and try again."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
            print(item)
else:
    print(output)