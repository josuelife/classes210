def board():
  board = []
  for i in range(9):
    board.append(i + 1)
  return board

def display_board(board):
  print()
  print("{}|{}|{}".format(board[0], board[1], board[2]))
  print('-+-+-')
  print("{}|{}|{}".format(board[3], board[4], board[5]))
  print('-+-+-')
  print("{}|{}|{}".format(board[6], board[7], board[8]))
  print()

#Situations for the winner
def winner(board):
  return (board[0] == board[1] == board[2] or 
          board[3] == board[4] == board[5] or
          board[6] == board[7] == board[8] or 
          board[0] == board[3] == board[6] or 
          board[1] == board[4] == board[7] or 
          board[2] == board[5] == board[6] or 
          board[0] == board[4] == board[8] or 
          board[2] == board[4] == board[6])
    
#situation for a Draw
def draw(board):
  for place in range(9):
    if board[place] != "x" or board[place] != "o":
      return False
  return True

def turn(p, board):
  place = int(input("Your turn, {}! Choose a place the for next {}: ".format(p, p)))
  board[place - 1] = p

def next(now):
  if now == "" or now == "o":
    return "x"
  elif now == "x":
    return "o"

def main():
  p = next("")
  theboard = board()
  while not (winner(theboard) or draw(theboard)):
    display_board(theboard)
    turn(p, theboard)
    p = next(p)
  display_board(theboard)
  print("You Won!")
  

if __name__ == '__main__':
  main()