
def switchPlayer(player):
    if player == choices[0]:
        return choices[1]
    else:
        return choices[0]

def checkMove(move, board):
    if move in board:
        return True
    else:
        return False

def displayBoard(board):
    print(f'{board[6]} | {board[7]} | {board[8]}')
    print('-'*9)
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('-'*9)
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('\n')

def clearBoard():
    print('\n'*100)

def iswinner(board):
    wins = ([1,2,3],[4,5,6],[7,8,9],[1.4,7],[2,5,8],[3,6,9],[7,5,3],[9,5,3])
    xchoice = [x + 1 for x,value in enumerate(board) if value == 'X']
    ochoice = [o + 1 for o,value in enumerate(board) if value == 'O']
    fullboard = xchoice + ochoice

    for i in wins:
        if set(i).issubset(xchoice):
            print("X IS THE WINNER!!!")
            print('\n')
            return True
        elif set(i).issubset(ochoice):
            print("O IS THE WINNER!!!")
            print('\n')
            return True

    if len(fullboard) == 9:
        print("THERE IS NO WINNER!!!")
        print('\n')
        return True
    else:
        return False




    pass

def playgame(player):

    board = ['1','2','3','4','5','6','7','8','9']
    winner = False
    again = ('Y', 'N')
    while winner == False:
        if iswinner(board):
            break
        move = input(f"'{player}', Please enter a move (1-9):")
        if checkMove(move, board):
            clearBoard()
            board[int(move)-1] =  player
            displayBoard(board)
        else:
            print("Move is unavailable... Please try again.")
            continue

        player = switchPlayer(player)

    play = input("Would you like to play again? Y or N? ")
    if play.upper() in again:
        if play.upper() == again[0]:
            return True
        else: return False



print('starting')
playing = True
choices = ('X', 'O')
while playing:
    player = input("would you like to be X or O? ").upper()
    if player in choices:
        print("Okay! Let's Play!")
        playing = playgame(player)
    else:
        print("Thats not a choice! Try again!")
        continue

print('ending')
