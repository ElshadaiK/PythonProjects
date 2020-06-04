##Player's move
def proceedToPlay():
    question = "Enter O or X: "
    answer = input(question)
    if answer == 'O' or answer == 'o' or answer == 'X' or answer == 'x':
        player = answer.upper()
        if player == 'X':
            computer = 'O'
        else:
            computer = 'X'
        return (computer, player)
    else:
        print("Wrong Input")
        proceedToPlay()

def spaceIsFree(position, board):
    return board[position]==" "

def insertLetter(letter, position, board):
    board[position] = letter
    
def chooseNumber(letter, board):
    question = "Choose your slot: "
    try:
        answer = eval(input(question))
        if((answer <= 9 and answer >= 1) and spaceIsFree(answer, board)):
            insertLetter(letter, answer, board)
        else:
            print("Please enter a valid slot 1-9")
            chooseNumber(letter, board)
    except:
        print("Please enter a valid slot 1-9")
        chooseNumber(letter, board)



##Checking to end game
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True



##Checking winner
def isWinner(letter, board):
    return ((board[1] == letter and board[2] == letter and board[3] == letter)
            or
            (board[4] == letter and board[5] == letter and board[6] == letter)
            or
            (board[7] == letter and board[8] == letter and board[9] == letter)
            or
            (board[1] == letter and board[4] == letter and board[7] == letter)
            or
            (board[2] == letter and board[5] == letter and board[8] == letter)
            or
            (board[3] == letter and board[6] == letter and board[9] == letter)
            or
            (board[1] == letter and board[5] == letter and board[9] == letter)
            or
            (board[3] == letter and board[5] == letter and board[7] == letter)
            )
            





#Drawing the table    
def emptySpace():
    print("   |   |   ")
def lineBreaker():
    print("-----------")
def valueSpace(val1, val2, val3):
    print(" " + val1 + " | " + val2 + " | " + val3)
def printBoard(board):
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



##Computer Move
def selectRandom(lists):
    import random
    ln = len(lists)
    r = random.randrange(0, ln)
    return lists[r]
    
def computerMove(computer, board):
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in [computer]:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if(isWinner(computer, boardcopy)):
               move = i
               return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
    
    print(move)





##Main Game    
def mainGame():
    board = [" " for x in range(10)]
    winner = None 
    try:
        computer, player = proceedToPlay()
    except:
        return
    turn = player
    printBoard(board)
    while(not(isBoardFull(board))):
        if(turn == player):
            chooseNumber(player, board)
        elif(turn == computer):
            cm = computerMove(computer, board)
            insertLetter(computer, cm, board)
            printBoard(board)
        
        
        if(isWinner(turn, board)):
            winner = turn
            if winner == player:
               printBoard(board)
         
            print("Congratulations! "+ winner +" won")
            break
        else:
            if(turn == player):
                turn = computer
            else:
                turn = player
    if(not(winner)):
        print("Game Tie!")
                   
        
def decideToPlay():
    while(True):
        question = "Do you want to play? Enter y for yes, and any key for no: "
        answer = input(question)
        if answer == 'y' or answer == 'Y':
            mainGame()
        else:
            break     
            
decideToPlay()
    
