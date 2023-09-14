from art import logo

# ADD
def add(n1, n2):
    return n1 + n2

# SUBTRACT
def subtract(n1, n2):
    return n1 - n2

# MULTIPLY
def multiply(n1, n2):
    return n1 * n2

#DIVIDE
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print("Hello, Welcome to the calculator! ")
print("The operations you can execute with the calculator are: ")
for i in operations:
    print(i)

def calculator():
    print(logo)
    num1 = float(input("What's the first number? : "))

    operationFinished = False
    while not operationFinished:

        choice = input("Pick an operation: ")
        func = operations[choice]

        num2 = float(input("What's the second number? : "))

        result = func(num1, num2)
        print(f"{num1} {choice} {num2} = {result}")

        continuation = input(f"Type 'y' to continue calculating with {result} ,type 'n' to start a new calculation, or type 'e' to exit. ").lower()
        if(continuation == "y"):
            operationFinished = False
            num1 = result
        elif(continuation == "n"):
            operationFinished = True
            calculator()
        elif(continuation == "e"):
            operationFinished = True

calculator()