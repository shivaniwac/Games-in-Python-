import random

def PlayRPS():

  player_choice = input('enter a choice (rock, paper, scissors): ')
  options = ['rock', 'paper', 'scissors']
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"you chose  {player} computer chose {computer}" )
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
      if computer == "scissors":
        return "Rock Smashes scissors! You won."
      else:
        return "I'll wrap your rock in this paper! You loose!"
  elif player == "paper":
      if computer == "scissors":
         return "I am going to cut you now! I Won!"
      else:
        return "You won."
  elif player == "scissors":
      if computer == "paper":
         return "You Won."
      else:
        return "Rock Smashes scissors! I won"
  else:
    return "Enter a vaild option"
     
while True:
  choice = PlayRPS()
  result = check_win(choice["player"], choice["computer"])
  print(result)
  play_again = input("Fo you want to play again?  (yes/no):")
  if play_again.lower() != "yes":
    break


