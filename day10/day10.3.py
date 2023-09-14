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

num1 = int(input("What's the first number? : "))

print("The operations you can execute with the calculator are: ")

for i in operations:
    print(i)
choice = input("Which operation do you want to execute? Pick from the operations above: ")

num2 = int(input("What's the second number? : "))

func = operations[choice]
result = func(num1, num2)
print(f"{num1} {choice} {num2} = {result}")