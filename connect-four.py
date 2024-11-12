board = [
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "]
  ]

def main():
  playerOneName = input("\nPlayer One - Input your name. Name input: ")
  if not playerOneName:
    playerOneName = "Player One"
  print("\""+ playerOneName+ "\" registered as name")

  playerTwoName = input("\nPlayer Two - Input your name. Name input: ")
  if not playerTwoName:
    playerTwoName = "Player Two"
  print("\""+ playerTwoName+ "\" registered as name")

  playerToken = "O"
  gameOver = False

  print("\nLet the games begin!")
  print("Input \"quit\" at any time to abort the game\n")
  print_board()
  print(playerOneName + " (O)'s turn")

  while not gameOver:
    isValidColumn = False

    while not isValidColumn:
      column = input("\nChoose a column number. Column chosen: ")

      if column == "quit":
        print("Match aborted by player request")
        quit()

      try:
        column = int(column)
      except:
        print("Please enter the column number only and nothing else.")
        continue

      if column < 0 or column > 6:
        print("Please enter a column number between 0 and 6.")
        continue

      isValidColumn = True

    row = get_bottom(column)

    if row >= 0:
      board[row][column] = playerToken
      print_board()
      gameOver = check_win(row, column, playerToken)

      if not gameOver:
        if playerToken == "X":
          playerToken = "O"
          print(playerOneName + " (O)'s turn")
        else:
          playerToken = "X"
          print(playerTwoName + " (X)'s turn")

    else:
      print("That column is full. Try again")

  if playerToken == "O":
    print("\n*** " + playerOneName + " (O) wins! ***")
  else:
    print("\n*** " + playerTwoName + " (X) wins! ***")

def print_board(): 
  print ("   0 1 2 3 4 5 6 ")

  for i in range(len(board)):
    print(str(i) + " |" + board[i][0] + "|" + board[i][1] + "|" + board[i][2] + "|" + board[i][3] + "|" + board[i][4] + "|" + board[i][5] + "|" + board[i][6] + "|" )

def get_bottom(column):
  for row in reversed(range(len(board))):
    if board[row][column] == " ":
      return row
    
  return -1

def check_win(row, column, playerToken):
  if check_row(row, playerToken) or check_column(column, playerToken) or check_positive_diagonal(row, column, playerToken) or check_negative_diagonal(row, column, playerToken):
    return True
  else:
    return False

def check_row(row, playerToken):
  count = 0

  for i in range(7):
    if board[row][i] == playerToken:
      count += 1
    else:
      count = 0

    if count >= 4:
      return True
    
  return False

def check_column(column, playerToken):
  count = 0

  for i in range(6):
    if board[i][column] == playerToken:
      count += 1
    else:
      count = 0

    if count >= 4:
      return True
    
  return False

def check_positive_diagonal(row, column, playerToken):
  bottomLeftCorner = get_bottom_left_corner(row, column)
  topRightCorner = get_top_right_corner(row, column)
  diagonalRange = abs(topRightCorner[0] - bottomLeftCorner[0]) + 1
  count = 0

  for i in range(diagonalRange):
    if board[bottomLeftCorner[0]-i][bottomLeftCorner[1]+i] == playerToken:
      count += 1
    else:
      count = 0

    if count >= 4:
      return True
    
  return False

def check_negative_diagonal(row, column, playerToken): 
  topLeftCorner = get_top_left_corner(row, column)
  bottomRightCorner = get_bottom_right_corner(row, column)
  diagonalRange = abs(topLeftCorner[0] - bottomRightCorner[0]) + 1
  count = 0

  for i in range(diagonalRange):
    if board[topLeftCorner[0]+i][topLeftCorner[1]+i] == playerToken:
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

  return [bottommostRow, leftmostColumn]

def get_top_right_corner(row, column):
  topmostRow = row
  rightmostColumn = column

  while topmostRow > 0 and rightmostColumn < 6:
    rightmostColumn += 1
    topmostRow -= 1

  return [topmostRow, rightmostColumn]

def get_top_left_corner(row, column):
  topmmostRow = row
  leftmostColumn = column

  while topmmostRow > 0 and leftmostColumn > 0:
    leftmostColumn -= 1
    topmmostRow -= 1

  return [topmmostRow, leftmostColumn]

def get_bottom_right_corner(row, column):
  bottommostRow = row
  rightmostColumn = column

  while bottommostRow < 5 and rightmostColumn < 6:
    rightmostColumn += 1
    bottommostRow += 1

  return [bottommostRow, rightmostColumn]

if __name__ == '__main__':
    main()