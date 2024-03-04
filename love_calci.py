print("Welcome to love calculator!")
name1=input("Enter your name: ")
name2=input("Enter their name: ")
combined_string=name1+name2
lower_case=combined_string.lower()
t=lower_case.count('t')
r=lower_case.count('r')
u=lower_case.count('u')
e=lower_case.count('e')
true=t+r+u+e
l=lower_case.count('l')
o=lower_case.count('o')
v=lower_case.count('v')
e=lower_case.count('e')
love=l+o+v+e
lovescore=int(str(true)+str(love))
if (lovescore<1) or (lovescore>90):
    print(f'Your lovescore is {lovescore}, you together are like coke and mentos.')
elif (lovescore>=40) and (lovescore<=50):
    print(f'Your lovescore is {lovescore},you together are alright.')
else: 
    print(f'Your lovescore is {lovescore}.')