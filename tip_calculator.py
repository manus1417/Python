print("Welcome to tip calculator!")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people=int(input('How many people to split the bill? '))
tip_percent=tip/100
total_tip=tip_percent*bill
bill_with_tip=bill+total_tip
bill_per_person=(bill_with_tip/people)
final_amount=round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")