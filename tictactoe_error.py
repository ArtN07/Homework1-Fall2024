"""tictactoe game for 2 players"""

choices = []

for x in range (1, 10) :
    choices.append(x)

playerOneTurn = True
winner = False


def printBoard() :
    print( '\n -----')
    print( '|' + str(choices[0]) + '|' + str(choices[1]) + '|' + str(choices[2]) + '|')
    print( ' -----')
    print( '|' + str(choices[3]) + '|' + str(choices[4]) + '|' + str(choices[5]) + '|')
    print( ' -----')
    print( '|' + str(choices[6]) + '|' + str(choices[7]) + '|' + str(choices[8]) + '|')
    print( ' -----\n')


while not winner:
    printBoard()

    if playerOneTurn :
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        choice = int(input(">> "))
    except:
        print("please enter a valid field")
        continue

    if choices[choice - 1] == 'X' or choices[choice - 1] == 'O':
        print("illegal move, please try again")
        continue

    if playerOneTurn :
        choices[choice - 1] = 'X'
    else :
        choices[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :  # Place break point at this line!
        y = x * 3
        if choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)] :
            printBoard()
            winner = True
        if choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)] :
            printBoard()
            winner = True

    if((choices[0] == choices[4] and choices[0] == choices[8]) or
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        printBoard()
        winner = True

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")