import random
import os
from blackjack_logo import logo
clear=lambda: os.system('cls')
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  rcard=random.choice(cards)
  return rcard

def calculate_sum(c):
    
    if sum(c)==21 and len(c)==2:
        return 0
    if 11 in c and sum(c)>21:
        c.remove(11)
        c.append(1)
    return sum(c)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "It's a draw😑"
    elif computer_score==0:
        return "You lose. Opponent has a blackjack!😮"
    elif user_score==0:
        return "Win with a blackjack🤩"
    elif user_score>21:
        return "You went over. You lose.😫"
    elif computer_score>21:
        return "Opponent went over. You win.😜"
    elif user_score>computer_score:
        return "You win🙂"
    else:
        return "You lose😑"
    
def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over=False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not is_game_over:    
        user_score=calculate_sum(user_cards)
        computer_score=calculate_sum(computer_cards)
        print(f"Your cards: {user_cards},current score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")

        if user_score==0 or user_score >21 or computer_score==0:
            is_game_over=True
        else:
            deal=input("Type 'y' to get another card, type 'n' to pass: ")
            if deal=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True
            
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_sum(computer_cards)   
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")    
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") =="y":
    clear()
    play_game()
    