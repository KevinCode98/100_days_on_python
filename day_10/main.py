from art import logo

print(logo)

# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
   }

def calculator():
    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue: 
        operation_symbol = input('Pick an operation: ')
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        answare = calculation_function(num1, num2)
        print(f'{num1} {operation_symbol} {num2} = {answare}')

        if input(f"Type 'y' to continue calculating with {answare}, or type 'n' to exit: ") == 'y':
            num1 = answare
        else:
            should_continue = False
            if input ("Type 'y' to exit the calculation, or type 'n' to continue.") == 'n':
                calculator()
            else: 
                break

            
calculator()
