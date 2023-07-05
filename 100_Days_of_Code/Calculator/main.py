from art import logo
# Calculator functions
print(logo)
#Add
def add(x, y):
    return x + y

#Subtract
def sub(x, y):
    return x - y

#Multiply
def mul(x, y):
    return x * y

#Division
def div(x, y):
    return x / y

#Dictionary
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

num1 = float(input("What's the first number? "))
num2 = float(input("What's the second number? "))

for symbols in operations:
    print(symbols)

operation_symbol = input("Pick an operation from the line above: ")

calc_function = operations[operation_symbol]

answer = calc_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

Aditional_op = True
while Aditional_op:
    operation_symbol = input("Pick another operation: ")
    num3 = float(input("What's the next number? "))
    calc_function = operations[operation_symbol]
    prev_answer = answer
    answer = calc_function(answer, num2)
    print(f"{prev_answer} {operation_symbol} {num3} = {answer}")

    again = input("Do you want to do another operation? Enter 'y' or 'n': ")

    if again == 'n':
        Aditional_op = False

