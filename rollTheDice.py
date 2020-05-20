import random
def roll():
    x = random.randint(1, 6)
    return x
def draw(num):
    fill("-")
    if(num == 1):
        fill(" ")
        halfWay()
        fill(" ")
    elif(num == 2):
        fill(" ")
        twoInRow()
        fill(" ")
    elif(num == 3):
        halfWay()
        halfWay()
        halfWay()
    elif(num == 4):
        twoInRow()
        fill(" ")
        twoInRow()
    elif(num == 5):
        twoInRow()
        halfWay()
        twoInRow()
    else:
        twoInRow()
        twoInRow()
        twoInRow()
        
    fill("-")
def fill(x, n = 13):
    print("[", end="")
    for i in range(n):
        print(x, end="")
    print("]")
def halfWay():
    print("[", end="")
    for i in range(6):
        print(" ", end="")
    print("O", end="")
    for i in range(6):
        print(" ", end="")
    print("]")
def twoInRow():
    print("[", end="")
    print(" ", end="")
    print("O", end="")
    for i in range(9):
        print(" ", end="")
    print("O", end="")
    print(" ", end="")
    print("]")
def main():
    while(True):
        useInp = input("Enter y to roll the dice or any key to quit: ")
        if(useInp == "y" or useInp == "Y"):
            num = roll()
            draw(num)
        else:
            break
main()
