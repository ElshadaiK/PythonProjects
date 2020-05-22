import json
import random

data = json.load(open("dictionary.json"))

def border():
    for i in range(15):
        print("=", end="")
    print("=")
def choose():
    word = random.choice(list(data))
    if " " in word:
        splitted = word.split(" ")
        n = random.randint(0, len(splitted)-1)
        word = splitted[n]
    print("Try to guess the word in less than 10 attempts")
    return word
def draw(n, word):
    if n>9:
        return
    if n == 0:
        print("_"*5, end ="")
        print("O")
    if n == 1:
        print("_"*4, end ="")
        print("O")
    if n == 2:
        print("_"*2, end ="")
        print(" "*1, "O")
    if n <= 9 and n >= 3:
        print(" "*3, "O")
    if n == 8:
        print(" "*3, "|")
    elif n <= 7:
        print(" "*2, "/", end ="")
        print("|", end ="")
    if n == 7:
        print()
    if n <= 6:
        print("\\")
    if n == 5:
        print(" "*3, "|")
    elif n <= 4:
        print(" "*2, "_", end ="")
        print("|", end ="")
    if n == 4:
        print()
    if n <= 3:
        print("_")
    if n ==0:
        border()
        print('GAME OVER!!!!')
        print("The word is: ", word)
def ask(word):
    word = word.lower()
    trys = 10
    splitted = list(word)
    found = list((len(splitted))* "_")
    while(len(splitted) != 0 and trys > 0):
        print("Guess the word: ", end="")
        for i in found:
            print(i, end = " ")
        print()
        trial = input(" ")
        if trial in splitted:
            ind = word.index(trial)
            splitted.remove(trial)
            found[ind] = trial
        else:
            trys -= 1
            print(trys, " turns left")
            border()
            draw(trys, word)
            border()
    if(len(splitted) == 0):
        print("CONGRATULATIONS!!!", name, ", You Won!!!")
name = input("Enter your name: ")
print("Welcome", name)
border()
ask(choose())



