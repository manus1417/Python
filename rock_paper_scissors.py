import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice=int(input('What is your choice? 0 for rock, 1 for paper or 2 for scissors\n'))
comp_choice=random.randint(0,2)
if choice==0:
    print(rock)
elif choice==1:
    print(paper)
elif choice==2:
    print(scissors)
print(f'Computer chose: \n{comp_choice}')
if comp_choice==0:
    print(rock)
elif comp_choice==1:
    print(paper)
elif comp_choice==2:
    print(scissors)

if choice==0 and comp_choice==2:
    print('You win!')
elif choice==2 and comp_choice==0:
    print('You lose!')
elif choice>=3 or choice<0:
    print('Invalid input you lose!')  
elif comp_choice>choice:
    print('You lose!')
elif choice>comp_choice:
    print('You win!')
elif choice==comp_choice:
    print("It's a draw!")