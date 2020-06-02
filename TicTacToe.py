board = [" " for x in range(10)]

def decideToPlay():
    question = "Do you want to play? Enter y for yes, and any key for no: "
    answer = input(question)
    if answer == 'y' or answer == 'Y':
        print("Continue")
    else:
        return
def spaceIsFree(position):
    return board[position]==" "
def insertLetter(letter, position):
    board[position] = letter







#Free space    
def emptySpace():
    print("   |   |   ")
def lineBreaker():
    print("-----------")
def valueSpace(val1, val2, val3):
    print(" " + val1 + " | " + val2 + " | " + val3)
def printBoard():
    lineBreaker()
    emptySpace()
    valueSpace(board[1], board[2], board[3])
    emptySpace()
    lineBreaker()
    emptySpace()
    valueSpace(board[4], board[5], board[6])
    emptySpace()
    lineBreaker()
    emptySpace()
    valueSpace(board[7], board[8], board[9])
    emptySpace()
    lineBreaker()
printBoard()
    
