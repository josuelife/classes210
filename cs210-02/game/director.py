
from card import Card

class Director:
  def __init__(self):
    self.card = []
    self.hilo_guess = ""
    self.play_again = True
    self.score = 300

    for i in range (2):
      self.card.append(Card())

  def start_game(self):
    while self.play_again and (self.score > 0):
      for i in range (2):
        self.card[i].generate()
      print(f"The card is: {self.card[0].value}")
      self.get_high_low_guess()
      self.output_result()
      self.get_play_again_input()

  def get_high_low_guess(self):

    if not self.play_again:
      return

    self.hilo_guess = str(input("Higher or Lower? [h/l] "))

    while (self.hilo_guess.lower() != "h") and (self.hilo_guess.lower() != "1"):
      print("\nInvalid Entry!")
      self.hilo_guess = input("Higher or Lower? [h/l] ")

    if (self.hilo_guess.lower() == "h") and (self.card[0].value < self.card[1].value) | (self.hilo_guess.lower() == "l") & (self.card[0].value > self.card[1].value):
      self.score += 100

    elif (self.card[0].value == self.card[1].value):
      self.score += 0
    
    else:
      self.score -= 75
      
  def output_results(self):
    
    if not self.play_again:
      return
    
    print(f"The next card is: {self.card[1].value}")
    print(f"Your score is: {self.score}\n")

  def get_play_again_input(self):

    if self.score <= 0:
      print("All out of points. Better luck next time!")
      return

    play = input("Play again? [y/n] ")
    while (play.lower() != "y") and (play.lower() != "n"):
      print("\nInvalid Entry!")
      play = input("Play again? [y/n] ")

    if play.lower() == "n":
      print("Thanks for playing!")
      self.play_again = False

    else:
      print()
      self.play_again = True