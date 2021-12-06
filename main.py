def whichValue(board):
    count = 0
    for r in range(3):
        for c in range(3):
            if (board[r][c] != 0):
                count += 1
    if (count % 2 == 1):
        return "O"
    else:
        return "X"

def checkForRows(board):
    for row in board:
        

def play_ttt(board):
    while (true):
        inp = list(map(int,input("Give me two numbers separated by a space. Both numbers must be greater than -1 and less than 3: ").split()))
        if (len(inp) != 2):
            continue
        else:
            if (board[len[0]][len[1]] != 0):
                break
            else:
                continue
    # At this point we have gotten a point like [0, 1]
    # Now we have to change the board to be the actual value, whether it be "X" or "O".
    letter = whichValue(board)
    board[inp[0]][inp[1]] = letter
    # We have now set the letter of the player onto the board
    
    # Now we check if the user has won in the rows
    checkForRows(board)




board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]