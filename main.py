############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


#Creating a deal_card() function that uses the List below to *return* a random card. 
#11 is the Ace.
from art import logo
from replit import clear
import random

def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
#Creating a function called calculate_score() to take a List of cards as input 
#and return the score. 
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  #Checking for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
#Checking for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
  
def compare(user_score, computer_score):
  """Compares the user's score with the computer's score and sets the winner"""
  if user_score == computer_score:
    return "It's a tie."
  elif computer_score == 0:
    return "Lose, dealer has a Blackjack."
  elif user_score == 0:
    return "Win, you have a Blackjack."
  elif user_score > 21:
    return "You went over. You lose."
  elif computer_score > 21:
    return "Dealer went over. You win."
  elif user_score > computer_score:
    return "You win."
  else:
    return "Dealer wins."

def play_game():
  """Function to set up the game and play it"""
  print(logo)
  #Dealing the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  #Calling calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
  #The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  while game_over == False:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"  Your cards: {user_cards}, current score: {user_score}.")
    print(f"  Computer's cards: {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      #If the game is not over, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      deal_more = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if deal_more == "y":
        user_cards.append(deal_card())
      else:
        game_over = True
  
  #The computer should keep drawing cards as long as it has a score less than 21.
  while computer_score != 0 and computer_score < 21:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  
  print(f"  Your final hand: {user_cards}, Your final score: {user_score}.")
  print(f"  Computer's final hand: {computer_cards}, dealer's final score: {computer_score}.")
  print(compare(user_score, computer_score))


#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Wanna play Blackjack? Type 'y' or 'n': ").lower() == "y":
  clear()
  play_game()