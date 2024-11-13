from browser import document # type: ignore

board = [
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "]
  ]

answers = []
playerNames = ["", ""]
playerToken = ["O"]
gameOver = [False]

def print_output(text):
  document["terminal"].text += text + "\n"

def get_input(event): 
  userInput = document["userInput"].value
  document["userInput"].value = ""
  answers.append(userInput)

def main():
  print_output("Player One, please input your name")

  def handle_submission(event):
    if event.keyCode == 13:
      get_input(event)

      if len(answers) == 1:
        playerNames[0] = answers[0]

        if not playerNames[0]:
          playerNames[0] = "Player One"

        print_output("\""+ playerNames[0] + "\" registered as name")
        
        print_output("\nPlayer Two, please input your name")
      elif len(answers) == 2:
        playerNames[1] = answers[1]

        if not playerNames[1]:
          playerNames[1] = "Player Two"
          
        print_output("\""+ playerNames[1]+ "\" registered as name")

        print_output("\nLet the games begin!")
        print_output("Input \"quit\" at any time to abort the game\n")

        print_board()
        print_output("\n" + playerNames[0] + " (O)'s turn")
      elif not gameOver[0]:
        print_output("\nChoose a column number")
        column = answers[len(answers)-1]

        if column == "quit":
          print_output("Match aborted by player request\n")
          gameOver[0] = True
          return

        try:
          column = int(column)
        except:
          print_output("Please enter the column number only and nothing else.")
          return

        if column < 0 or column > 6:
          print_output("Please enter a column number between 0 and 6.")
          return

        row = get_bottom(column)

        if row >= 0:
          board[row][column] = playerToken[0]
          print_board()
          gameOver[0] = check_win(row, column, playerToken[0])

          if not gameOver[0]:
            if playerToken[0] == "X":
              playerToken[0] = "O"
              print_output("\n" + playerNames[0] + " (O)'s turn")
            else:
              playerToken[0] = "X"
              print_output("\n" + playerNames[1] + " (X)'s turn")
          else:
            if playerToken[0] == "O":
              print_output("\n*** " + playerNames[0] + " (O) wins! ***\n")
            else:
              print_output("\n*** " + playerNames[1] + " (X) wins! ***\n")

        else:
          print_output("That column is full. Try again")
      else:
        print_output("The match is over. Please refresh the page to play again")

  document["userInput"].bind("keydown", handle_submission)

def print_board(): 
  print_output("   0 1 2 3 4 5 6 ")

  for i in range(len(board)):
    print_output(str(i) + " |" + board[i][0] + "|" + board[i][1] + "|" + board[i][2] + "|" + board[i][3] + "|" + board[i][4] + "|" + board[i][5] + "|" + board[i][6] + "|" )

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