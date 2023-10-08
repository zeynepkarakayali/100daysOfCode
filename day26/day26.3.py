list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:
integers = [int(strings) for strings in list_of_strings]
print(integers)

# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [num for num in integers if num%2 == 0]

# Write your code 👆 above:
print(result)