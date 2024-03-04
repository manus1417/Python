#Donot forget to download blind_auction_logo.py file.
import os
clear=lambda: os.system('cls')
from blind_auction_logo import logo
print(logo)
bids={}
bidding_done=False
def find_highest():
  highest=0
  winner=''
  for person in bids:
    bid_amount=bids[person]
    if bid_amount>highest:      
      highest=bid_amount
      winner=person
  print(f'The winner is {winner} with a bid of ${highest}')
      
while not bidding_done:
  name=input('What is your name?: ')
  bid=int(input('What is your bid?: $'))
  bids[name]=bid
  move_on=input("Are there any other bidders? Type 'yes' or 'no'\n")
  if move_on=='no':
    bidding_done=True
    find_highest()
  elif move_on=='yes':
    clear()
  
  


