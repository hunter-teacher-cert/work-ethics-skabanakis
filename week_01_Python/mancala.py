import random

def drawBoardForUser(gameBoard):
    print("    ", end="")
    print("AI")
    print("    ", end="")
    print("#13 ", end="")
    print("#12 ", end="")
    print("#11 ", end="")
    print("#10 ", end="")
    print("#9 ", end="")
    print("#8 ")
    print("    ", end="")
    print("["+str(gameBoard[13])+"] ", end="")
    print("["+str(gameBoard[12])+"] ", end="")
    print("["+str(gameBoard[11])+"] ", end="")
    print("["+str(gameBoard[10])+"] ", end="")
    print("["+str(gameBoard[9])+"] ", end="")
    print("["+str(gameBoard[8])+"] ")
    
    print("#0 ", end="")
    print("                          ", end="")
    print("#7 ")
    print("<"+str(gameBoard[0])+">", end="") 
    print("                          ", end="")
    print("<"+str(gameBoard[7])+">")
    
    print("    ", end="")
    print("User", end="\n")
    print("    ", end="")
    print("#1  ", end="")
    print("#2  ", end="")
    print("#3  ", end="")
    print("#4  ", end="")
    print("#5  ", end="")
    print("#6  ")
    
    print("    ", end="")

    print("["+str(gameBoard[1])+"] ", end="")
    print("["+str(gameBoard[2])+"] ", end="")
    print("["+str(gameBoard[3])+"] ", end="")
    print("["+str(gameBoard[4])+"] ", end="")
    print("["+str(gameBoard[5])+"] ", end="")
    print("["+str(gameBoard[6])+"] ")
def userChoice(gameBoard):
    choice = -1
    counter = gameBoard[choice]
    while choice < 1 or choice > 6:
        choice = int(input("PLease select pod 1 - 6 "))
    counter = gameBoard[choice]
    moves = 0
    while gameBoard[choice] > 0:
        moves = moves + 1
        gameBoard[(choice+moves)%14] = gameBoard[(choice+moves)%14] + 1
        gameBoard[choice] = gameBoard[choice] - 1
    return choice
    
def AIChoice(gameBoard):
    counter = random.randint(8, 13)
    print("I selected bucket #" + str(counter))
    mmoves = 0
    while gameBoard[counter] > 0:
        mmoves = mmoves + 1
        gameBoard[(counter + mmoves) % 14] = gameBoard[(counter + mmoves) % 14] + 1
        gameBoard[counter] = gameBoard[counter] - 1
    return counter;
    
    
def main():
    mancalaBoard = [None] * 14
    print("Welcome to Mancala!")
    numberOfPlayers = 0
    while not(numberOfPlayers == 1 or numberOfPlayers == 2):
        numberOfPlayers = int(input("Would you like to play with 1 or 2 players "))
    for counter in range(1, 14):
        mancalaBoard[counter] = 4
    mancalaBoard[7] = mancalaBoard[0] = 0
    stonesOnBoard = 48
    while stonesOnBoard > 0:
        drawBoardForUser(mancalaBoard)
        userChoice(mancalaBoard)
        if numberOfPlayers == 2:
            AIChoice(mancalaBoard)
        stonesOnBoard = 48 - mancalaBoard[0] - mancalaBoard[7]
    if mancalaBoard[0] < mancalaBoard[7]:
        print("You won! You: " + str(mancalaBoard[7]) + " AI: " + str(mancalaBoard[0]))
    elif mancalaBoard[7] < mancalaBoard[0]:
        print("You lost! You: " + str(mancalaBoard[7]) + " AI: " + str(mancalaBoard[0]))
    elif mancalaBoard[7] == mancalaBoard[0]:
        print("It was a tie! You: " + str(mancalaBoard[7]) + " AI: " + str(mancalaBoard[0]))
        

main()