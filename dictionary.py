import json
from difflib import get_close_matches

data = json.load(open("dictionary.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no: ")
        if decide == "y" or decide == "Y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("Word unknown")
        else:
            return("You have entered wrong input please enter just y or n: ")
    else:
        print("Word unknown")



while(True):
    word = input("Enter the word you want to search: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    cont = input("Press n to quit, and any key to continue searching: ")
    if cont == "N" or cont == "n":
        break

