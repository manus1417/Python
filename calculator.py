# Calculator
from calculator_art import logo

def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
operations={
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  print(logo)
  cont=True
  num1=float(input("What's the first number?: "))  
  for opn in operations:
    print(opn)
  while cont:
    print('Pick an operation: ')
    op=input()
    num2=float(input("What's the next number?: "))
    op_func=operations[op]
    answer=op_func(num1,num2)
    print(f"{num1} {op} {num2} = {answer}")
    con=input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ")
    if con=='y':
      num1=answer
    else:
      cont=False
      calculator()
calculator()