
def playGame():
  yetToWin = True
  min = 0
  max = 100
  print "Please think of a number between 0 and 100!"
  while yetToWin:
    medium = (min + max) / 2
    print "Is your secret number " + str(medium) + "?"
    response = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if response == "h":
      max = medium
    elif response == "l":
      min = medium
    elif response == "c":
      print "Game over. Your secret number was: " + str(medium)
      yetToWin = False
    else:
      print "Sorry, I did not understand your input."
      continue   
      
playGame()      
      
      