with open("day26/file1.txt") as file1:
  f1 = file1.readlines()
with open("day26/file2.txt") as file2:
  f2 = file2.readlines()

filter_f1 = [int(num) for num in f1]
filter_f2 = [int(num) for num in f2]
#print(filter_f1)
#print(filter_f2)

result = [int(num) for num in f1 if num in f2]
# Write your code above 👆
print(result)