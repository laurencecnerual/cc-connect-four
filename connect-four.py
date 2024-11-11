board = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]

def main():
  gameOver = False
  print("Let the games begin!")
  print_board()
  while not gameOver:
    isValidColumn = False
    while not isValidColumn:
      column = int(input("Choose a column number. Column chosen: "))
      if column >= 0 and column <= 6:
        isValidColumn = True
      else:
        print("Invalid selection. Try again.")
    row = get_bottom(column)
    if row >= 0:
      board[row][column] = "O"
      print_board()
      gameOver = check_win(row, column)
    else:
      print("That column is full. Try again")
  print("Winner!")

def print_board(): 
  print ("  0 1 2 3 4 5 6 ")
  for i in range(len(board)):
    print(str(i) + "|" + board[i][0] + "|" + board[i][1] + "|" + board[i][2] + "|" + board[i][3] + "|" + board[i][4] + "|" + board[i][5] + "|" + board[i][6] + "|" )

def get_bottom(column):
  for row in reversed(range(len(board))):
    if board[row][column] == " ":
      return row
  return -1

def check_win(row, column):
  if check_row(row) or check_column(column) or check_positive_diagonal(row, column) or check_negative_diagonal(row, column):
    return True
  else:
    return False

def check_row(row):
  count = 0
  for i in range(7):
    if board[row][i] == "O":
      count += 1
    else:
      count = 0
    if count >= 4:
      return True
  return False

def check_column(column):
  count = 0
  for i in range(6):
    if board[i][column] == "O":
      count += 1
    else:
      count = 0
    if count >= 4:
      return True
  return False

def check_positive_diagonal(row, column):
  bottomLeftCorner = get_bottom_left_corner(row, column)
  topRightCorner = get_top_right_corner(row, column)
  diagonalRange = topRightCorner[0] - bottomLeftCorner[0]
  count = 0
  for i in range(diagonalRange):
    if board[bottomLeftCorner[0]+i][bottomLeftCorner[1]+i] == "O":
      count += 1
    else:
      count = 0
    if count >= 4:
      return True
  return False

def check_negative_diagonal(row, column): 
  topLeftCorner = get_top_left_corner(row, column)
  bottomRightCorner = get_bottom_right_corner(row, column)
  diagonalRange = abs(topLeftCorner[0] - bottomRightCorner[0])
  count = 0
  for i in range(diagonalRange):
    if board[topLeftCorner[0]+i][topLeftCorner[1]+i] == "O":
      count += 1
    else:
      count = 0
    if count >= 4:
      return True
  return False

def get_bottom_left_corner(row, column):
  bottommostRow = row
  leftmostColumn = column
  while bottommostRow < 5 and leftmostColumn > 0:
    leftmostColumn -= 1
    bottommostRow += 1
  print("bottomleft- row, column: " + str(bottommostRow) + ", " + str(leftmostColumn))
  return [bottommostRow, leftmostColumn]

def get_top_right_corner(row, column):
  topmostRow = row
  rightmostColumn = column
  while topmostRow > 0 and rightmostColumn < 6:
    rightmostColumn += 1
    topmostRow -= 1
  print("topright- row, column: " + str(topmostRow) + ", " + str(rightmostColumn))
  return [topmostRow, rightmostColumn]

def get_top_left_corner(row, column):
  topmmostRow = row
  leftmostColumn = column
  while topmmostRow > 0 and leftmostColumn > 0:
    leftmostColumn -= 1
    topmmostRow -= 1
  print("topleft- row, column: " + str(topmmostRow) + ", " + str(leftmostColumn))
  return [topmmostRow, leftmostColumn]

def get_bottom_right_corner(row, column):
  bottommostRow = row
  rightmostColumn = column
  while bottommostRow < 5 and rightmostColumn < 6:
    rightmostColumn += 1
    bottommostRow += 1
  print("bottomright- row, column: " + str(bottommostRow) + ", " + str(rightmostColumn))
  return [bottommostRow, rightmostColumn]

if __name__ == '__main__':
    main()