def PrintBoard(board):
  for row in board:
    print ''.join(row)

def FindWinSpot(piece, board):
  def OnlyOnePlaceableSpot(line, piece):
    return line.count('-') == 1 and line.count(piece) == len(board)-1

  for x in xrange(len(board)):
    # check horizontal
    row = ''.join(board[x])
    if OnlyOnePlaceableSpot(row, piece):
      board[x][row.find('-')] = piece
      return True
    # check vertical
    col = ''.join(board[c][x] for c in xrange(len(board)))
    if OnlyOnePlaceableSpot(col, piece):
      board[col.find('-')][x] = piece
      return True
  # check diagonal
  major = ''.join(board[c][c] for c in xrange(len(board)))
  if OnlyOnePlaceableSpot(major, piece):
    board[major.find('-')][major.find('-')] = piece
    return True
  minor = ''.join(board[len(board)-1-c][c] for c in xrange(len(board)))
  if OnlyOnePlaceableSpot(minor, piece):
    board[len(board)-1-minor.find('-')][minor.find('-')] = piece
    return True
  return False

def Easy157(piece, board):
  win = FindWinSpot(piece, board)
  print PrintBoard(board) if win else "No Winning Move!"

def ParseInput(input):
  assert input.count("\n") == 3
  split = input.split("\n")
  piece = split[0]
  board = [ list(split[x]) for x in xrange(1, 4) ]
  return (piece, board)

input = r'''X
XX-
-XO
OO-'''

piece, board = ParseInput(input)
Easy157(piece, board)
