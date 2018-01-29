
board = ["","1","2","3","4","5","6","7","8","9"]
playerChoice = ""
def boardDraw():
  print("[",board[7],"]","[",board[8],"]","[",board[9],"]")
  print("[",board[4],"]","[",board[5],"]","[",board[6],"]")
  print("[",board[1],"]","[",board[2],"]","[",board[3],"]")
      
boardDraw()
board = [" "]*10


def playerTurn():
  global playerChoice
  playerChoice = ""
  while playerChoice is not int and playerChoice not in range(1,10):
    playerChoice = input("Choose a number between 1 and 9:")
    while playerChoice is not int:
      try:
        playerChoice = int(playerChoice)
        break
      except:
        playerChoice = input("That is not correct, you need to enter a number!")
    if playerChoice not in range(1,10):#Its 1,10 because python stops counting at 9
      print("The number you entered is not between 1 and 9!")

def playerBoardMove(pC):
  board[pC] = "X"

for i in range(9):
  playerTurn()
  playerBoardMove(playerChoice)
  boardDraw()
