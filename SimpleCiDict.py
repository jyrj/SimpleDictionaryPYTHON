import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()

    if w in data:
        return data[w]

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you meant %s?, If yes enter Y, if no enter N: " % get_close_matches(w, data.keys())[0])
        yn = yn.lower()

        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "Word you entered doesn't exists, kindly recheck."
        else:
            return "We couldn't understand your entry."
        
    else:
        return "Word you entered doesn't exists, kindly recheck."

word = input("Enter a word to lookup: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)