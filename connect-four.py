board = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
gameOver = False

#6hx7w
def main():
  print("Let the games begin!")
  print_board()
  column = int(input("Choose a column number. Column chosen: "))
  row = get_bottom(column)
  if row >= 0 :
    board[row][column] = "O"
    print_board()
  else:
    print("That column is full. Try again")

def print_board(): 
  print (" 0 1 2 3 4 5 6 ")
  for i in range(len(board)):
    print("|" + board[i][0] + "|" + board[i][1] + "|" + board[i][2] + "|" + board[i][3] + "|" + board[i][4] + "|" + board[i][5] + "|" + board[i][6] + "|" )

def get_bottom(column):
  for row in reversed(range(len(board))):
    if board[row][column] == " ":
      return row
  return -1

if __name__ == '__main__':
    main()