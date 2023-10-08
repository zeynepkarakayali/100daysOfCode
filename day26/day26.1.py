numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]

print(new_numbers)

name = "Angela"
new_name = [letter for letter in name]
print(new_name)

new_nums = [n*2 for n in range(1,5)]
print(new_nums)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor","Freddie"]
short_names = [name for name in names if len(name) < 5]
upper_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(upper_names)