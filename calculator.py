from art import calulator_logo
#
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def add(n1, n2):
    return n1+n2
def sub(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divison(n1, n2):
    return n1/n2

operations = {
    '+': add,
    '-': sub,
    '*': multiply,
    '/': divison,
}

def calculator_function():
    print(calulator_logo)
    num1 = float(input("What's your first number?: "))
    for symbol in operations:
        print(symbol)
    operation_input = input('pick the operation: ')
    flag = True
    while flag: 
        num2 = float(input("What your next number?: "))   
        ans = operations[operation_input](num1, num2)
        print(f"{num1} {operation_input} {num2} = {ans}")
        check_further = input('Do you want to perform any action on the above results. y or n or end ? ')
        check_further.lower()
        if check_further == 'n':
            flag = False
            cls()
            calculator_function()
            break
        elif check_further == 'y' :
            num1 = ans
            operation_input = input('pick the operation: ')
        else:
            break


calculator_function()




