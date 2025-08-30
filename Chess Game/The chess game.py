#setting up the program
import sys, copy

startingPieces = {'a8':'bR', 'b8':'bN', 'c8':'bB','d8':'bQ',
'e8':'bK', 'f8':'bB','g8':'bN','h8':'bR','a7':'bP','b7':'bP',
'c7':'bP','d7':'bP','e7':'bP','f7':'bP','g7':'bP','h7':'bP',
'a2':'wP', 'b2':'wP','c2':'wP','d2':'wP','e2':'wP','f2':'wP',
'g2':'wP','h2':'wP','a1':'wR','b1':'wN','c1':'wB','d1':'wQ','e1':'wK',
'f1':'wB','g1':'wN','h1':'wR'}

boardTemplate = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""
whiteSquare = '||'
blackSquare = '  '

def printChessBoard(board):
    squares = []
    isWhiteSquare = True
    for y in '87654321':
        for x in 'abcdefgh':
            #print (x,y,isWhiteSquare)  #debug show coordinates
            if x+y in board.keys():
                squares.append(board[x + y])
            else:
                if isWhiteSquare:
                    squares.append(whiteSquare)
                else:
                    squares.append(blackSquare)
            isWhiteSquare = not isWhiteSquare
        isWhiteSquare = not isWhiteSquare
    print(boardTemplate.format(*squares))

print('Interactive Chessboard')
print('by subham ')
print()
print('Pieces:')
print(' w - white,  b - black')
print(' p - pawn,  n - knight , b - bishop , r - rook , q - queen , k - king ')
print ('commands:')
print('move e2 e4 - moves the piece at e2 to e4 ')
print(' remove e2 - removes the  piece at e2 ')
print(' set e2 wP - sets square e2 to a white pawn')
print(' reset - resets pieces back to their starting squares')
print(' clear - clears the entire board')
print(' fill wP - fills entire board with white pawns.')
print(' quit - quits the program')

mainBoard = copy.copy(startingPieces)
while True:
    printChessBoard(mainBoard)
    response = input(' >').split()
    if response[0] == 'move':
        mainBoard[response[2]] = mainBoard[response[1]]
        del mainBoard[response[1]]
    elif response[0] == 'remove':
        del mainBoard[response[1]]
    elif response[0 ]== 'set':
        mainBoard[response[1]] = response[2]
    elif response[0] == 'reset':
        mainBoard = copy.copy(startingPieces)
    elif response [0] == 'clear':
        mainBoard = {}
    elif response[0] == 'fill':
        for y in '87654321':
            for x in 'abcdefgh':
                mainBoard[x + y] = response[1]
    elif response[0] == 'quit':
        sys.exit()

