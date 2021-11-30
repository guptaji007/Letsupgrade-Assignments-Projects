# Game Name
print("!!!Welcome to Tic-Tac-Toe Game!!!")
blist = [' ']*10 # Set Board Size

def display_board():
    print("Test Tic-Tac-Toe")
    print(blist[1]+'|'+blist[2]+'|'+blist[3])
    print('-----')
    print(blist[4]+'|'+blist[5]+'|'+blist[6])
    print('-----')
    print(blist[7]+'|'+blist[8]+'|'+blist[9])

# test_board = ['#', 'X', 'O', 'X', 'O', 'O', 'X', 'X', 'O', 'X']
display_board()

# For checking win case
def win(mark):
    # across the top 1st ()
    # across the middle 2nd ()
    # across the bottom 3rd ()
    # across left diagonally 4th ()
    # across right diagonally 5th ()
    # across left top-bottom 6th ()
    # across middle top-bottom 7th ()
    # across right top-bottom 8th ()
    return((blist[1] == blist[2] == blist[3] == mark) or (blist[4] == blist[5] == blist[6] == mark) or (blist[7] == blist[8] == blist[9] == mark) or (blist[1] == blist[5] == blist[9] == mark) or (blist[3] == blist[5] == blist[7] == mark) or (blist[1] == blist[4] == blist[7] == mark) or (blist[2] == blist[5] == blist[8] == mark) or (blist[3] == blist[6] == blist[9] == mark))
    # or
    # # return((blist[1] == blist[2] == blist[3] == mark) or (blist[4] == blist[5] == blist[6] == mark) or (blist[7] == blist[8] == blist[9] == mark) or (blist[1] == blist[5] == blist[9] == mark) or (blist[3] == blist[5] == blist[7] == mark))
# Check if the position is blank or not
def blank_pos(position):
    return blist[position] == ' '

# Start the game
def game():
    choose=input("choose 'X' or 'O' = ").upper()
    if(choose=='X'):
        First_player=choose
    else:
        second_player=choose
    turn='first'
    while(1):
        # Check if there is any empty position is there to X or 0 or it will draw the game
        if(' ' not in blist):
            print('Draw')
            break
        elif(turn=='first'):
            print('player 1 turn')
            position=int(input('Enter your position: '))
            if(blank_pos(position)):
                blist[position]='X'
                display_board()
            else:
                print('Give correct position: ')
            if(win('X')):
                print("player 1 wins")
                break
            else:
                turn='second'
        elif(turn=='second'):
            print('player 2 turn')
            position=int(input('Enter your position: '))
            if(blank_pos(position)):
                blist[position]='O'
                display_board()
            else:
                print('Give correct position')
            if(win('O')):
                print("player 2 wins")
                break
            else:
                turn='first'


game()
