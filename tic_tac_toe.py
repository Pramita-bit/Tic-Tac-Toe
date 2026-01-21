print(" 👾 !! WELCOME TO TIC-TAC-TOE !! 👾 ")

print("🔸Player 1 = ✖️ \n🔸Player 2 = ⭕")
print("🔸Numbering Guide Board 👇")
def guide():
    print(" 1 | 2 | 3 ")
    print("----------")
    print(" 4 | 5 | 6 ")
    print("----------")
    print(" 7 | 8 | 9 ")
guide()    
print("🔸Let's get started !!")

board = ["--","--","--",
         "--","--","--",
         "--","--","--"]
currentPlayer = "✖️"
winner = None
gameOn = True


# printing the board
def printBoard(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("----------")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("----------")
    print(board[6]+"|"+board[7]+"|"+board[8])

    
# player input
def playerInput(board):
    global currentPlayer
    inp = int(input("Enter a number from 1 to 9 : "))
    while inp<1 or inp>9:
        print("Number is out of Range. Please enter a number between 1 to 9.")
        inp = int(input("Enter a number from 1 to 9 : "))
    while board[inp-1]!= "--":
        print("This place is occupied. Please try again.")
        inp = int(input("Enter a number from 1 to 9 : "))
    if inp>=1 and inp<=9 and board[inp-1]=="--":
        board[inp-1] = currentPlayer
        
    
# checking win or tie
def winnerRow(board):
    global winner
    if board[0]==board[1]==board[2] and board[0]!="--":
        winner = board[0]
        print(f"🏆PLAYER {winner} IS WINNER !!!!")
        return True
    elif board[3]==board[4]==board[5] and board[3]!="--":
        winner = board[3]
        print(f"🏆PLAYER {winner} IS WINNER !!!!")
        return True
    elif board[6]==board[7]==board[8] and board[6]!="--":
        winner = board[6]
        print(f"🏆PLAYER {winner} IS WINNER !!!!")
        return True

def winnerColumn(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="--":
        winner = board[0]
        print(f"🏆PLAYER {winner} IS WINNER !!!!")
        return True
    elif board[1]==board[4]==board[7] and board[1]!="--":
        winner = board[1]
        print(f"🏆PLAYER {winner} IS WINNER !!!!")
        return True
    elif board[2]==board[5]==board[8] and board[2]!="--":
        winner = board[2]
        print(f"🏆PLAYER {winner} IS WINNER !!!!")
        return True

def winnerDiagonal(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="--":
        winner = board[0]
        print(f"🏆PLAYER {winner} IS WINNER !!!!")
        return True
    elif board[2]==board[4]==board[6] and board[2]!="--":
        winner = board[2]
        print(f"🏆PLAYER {winner} IS WINNER !!!!")
        return True

def tie(board):
    global gameOn
    if "--" not in board:
        print("‼️ IT'S A DRAW ‼️")
        printBoard(board)
        gameOn = False

def win(board):
    global gameOn
    if winnerRow(board) or winnerColumn(board) or winnerDiagonal(board):
        printBoard(board)
        gameOn = False

        
# switching players
def switchPlayer(board):
    global currentPlayer
    if currentPlayer == "✖️":
        currentPlayer = "⭕"
    elif currentPlayer == "⭕":
        currentPlayer = "✖️"

        
# calling all functions
while gameOn:
    printBoard(board)
    playerInput(board)
    tie(board)
    win(board)
    switchPlayer(board)
