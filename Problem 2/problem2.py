import Jewel
import stdarray
import p2Mod
import stddraw as sd

ROWS = 9
COLUMNS = 7
FINALTURN = 10
score = 0
turn = 0
board = stdarray.create2D(COLUMNS, ROWS, " ")
sd.setCanvasSize(560, 800)
sd.setXscale(0, 7)
sd.setYscale(-1, 9)
p2Mod.fill(board, COLUMNS, ROWS)
while p2Mod.winCheck(board, COLUMNS, ROWS):
    p2Mod.fill(board, COLUMNS, ROWS)
while not p2Mod.isDraw(board, COLUMNS, ROWS) and turn < FINALTURN:
    #Note a turn is used up if a turn is Valid but does not result in any pieces getting removed and thus the move is
    #reversed but a turn is still counted. This is intentional. If this is not wanted the turn+1 can be moved to the
    #combo loop
    turn += 1
    p2Mod.drawBoard(board, COLUMNS, ROWS, score, turn)
    sd.show(1)
    validMove = False
    while not validMove:

        piece1 = p2Mod.getMove(board, COLUMNS, ROWS)
        sd.square(piece1[0]+.5, piece1[1]+.5, .5)
        sd.show(1)
        piece2 = p2Mod.getMove(board, COLUMNS, ROWS)
        sd.square(piece2[0] + .5, piece2[1] + .5, .5)
        sd.show(500)
        dif1 = (piece1[0] - piece2[0]) * (piece1[0] - piece2[0])
        dif2 = (piece1[1] - piece2[1]) * (piece1[1] - piece2[1])
        p2Mod.drawBoard(board, COLUMNS, ROWS, score, turn)
        if (dif1 == 0 and dif2 == 1) or (dif1 == 1 and dif2 == 0):
            validMove = True
    p2Mod.move(board, piece1, piece2)
    sd.clear()
    p2Mod.drawBoard(board, COLUMNS, ROWS, score, turn)
    sd.show(200)
    if not p2Mod.winCheck(board, COLUMNS, ROWS):
        p2Mod.move(board, piece1, piece2)
    p2Mod.drawBoard(board, COLUMNS, ROWS, score, turn)
    sd.show(500)
    sd.clear()
    score += p2Mod.fill(board, COLUMNS, ROWS)
    p2Mod.drawBoard(board, COLUMNS, ROWS, score, turn)
    sd.show(1)
    combo = True
    while combo:
        combo = p2Mod.winCheck(board, COLUMNS, ROWS)
        p2Mod.drawBoard(board, COLUMNS, ROWS, score, turn)
        sd.show(500)
        score += p2Mod.fill(board, COLUMNS, ROWS)
        sd.show(1)
sd.setFontSize(70)
sd.text(3.5, 4.5, "Game Over")
sd.show()
