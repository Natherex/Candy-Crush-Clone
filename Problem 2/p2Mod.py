import Jewel
import stdarray
import stddraw as sd


def drawBoard(board, columns, rows, score, turn):
    """

    :param board: 2d array that is to be drawn
    :param columns: columns in 2d array
    :param rows: rows in 2d array
    :param score: current score
    :param turn: current turn

    prints the 2d array to the screen with the score and current turn at the bottom
    of the screen
    """
    sd.clear()
    for i in range(columns):
        for j in range(rows):
            if board[i][j] == " ":
                False
            else:
                board[i][j].draw(i, j)
    sd.setFontSize(40)
    sd.text(3.5, -.5, "Score " + str(score))
    sd.text(1, -.5, "Turn: " + str(turn))
    sd.show(1)


def fill(board, columns, rows):
    """

    :param board: 2d array to be filled
    :param columns: rows in 2d array
    :param rows: columns n 2d array

    Returns: Fills board with class:Jewels and returns how many Jewels have been filled
    """
    full = False
    score = 0
    while not full:
        dropPieces(board, columns, rows)
        full = True
        for i in range(columns):
            if board[i][rows - 1] == " ":
                board[i][rows - 1] = Jewel.Jewel()
                full = False
                score += 1
    return score


def dropPieces(board, columns, rows):
    """
    Drops all Jewels in board to the lowest empty row possible in its column
    """
    for i in range(columns):
        for j in range(rows - 1):
            if board[i][j] == " ":
                board[i][j] = board[i][j + 1]
                board[i][j + 1] = " "


def isDraw(board, columns, rows):
    """
    Returns true if there are no more valid moves
    """
    for i in range(columns - 1):
        for j in range(rows):
            move(board, (i, j), (i+1, j))
            for k in range(columns):
                for l in range(rows - 2):
                    if board[k][l].index == board[k][l + 1].index and board[k][l].index == board[k][l + 2].index:
                        move(board, (i, j), (i + 1, j))
                        return False
            move(board, (i, j), (i + 1, j))
    for i in range(rows - 1):
        for j in range(columns):
            move(board, (j, i), (j, i+1))
            for k in range(rows):
                for l in range(columns - 2):
                    if board[l][k].index == board[l + 1][k].index and board[l][k].index == board[l + 2][k].index:
                        move(board, (j, i), (j, i + 1))
                        return False
            move(board, (j, i), (j, i + 1))
    return True


def move(board, piece1, piece2):
    """
    :param board: 2d array
    :param piece1: list containing coordinates of piece1
    :param piece2: list containing coordinates of piece1
    :return: Swaps 2 jewels in board that have the coordinates of piece1 and piece2
    """
    temp = board[piece1[0]][piece1[1]]
    board[piece1[0]][piece1[1]] = board[piece2[0]][piece2[1]]
    board[piece2[0]][piece2[1]] = temp


def getMove(board, columns, rows):
    """
    Returns x and y coordinates where the user has clicked
    """
    while True:

        mouseClicked = sd.mousePressed()
        if mouseClicked:
            x = sd.mouseX()
            y = sd.mouseY()
            for i in range(columns):
                for j in range(rows):
                    if i < x < i + 1 and j < y < j + 1:
                        piece = [i, j]
                        return piece
        sd.show(0.05)


def checkColumns(board, columns, rows):
    """
    checks all columns to see if it has 3 matching Jewels in board
    """
    for i in range(columns):
        for j in range(rows - 2):
            if board[i][j].index == board[i][j + 1].index and board[i][j].index == board[i][j + 2].index:
                board[i][j].matched = True
                board[i][j + 1].matched = True
                board[i][j + 2].matched = True


def checkRows(board, columns, rows):
    """
    checks all rows to see if it has 3 matching Jewels in board. If it does set the matched Jewels matched
    variable to True
    """
    for i in range(rows):
        for j in range(columns - 2):
            if board[j][i].index == board[j + 1][i].index and board[j][i].index == board[j + 2][i].index:
                board[j][i].matched = True
                board[j + 1][i].matched = True
                board[j + 2][i].matched = True


def winCheck(board, columns, rows):
    """
     checks the board to see if any jewels matched variable is true. If it is true removes the Jewel and replaces it
      with " ". If no matches are found returns False otherwise returns True
     """
    check = False
    checkRows(board, columns, rows)
    checkColumns(board, columns, rows)
    for i in range(columns):
        for j in range(rows):
            if board[i][j].matched:
                board[i][j] = ' '
                check = True
    return check
