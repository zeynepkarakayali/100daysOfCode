# with open("day24/my_text.txt") as file:
#     contents = file.read()
#     print(contents)

with open("day24/my_text.txt", mode="a") as file:
    file.write("\nNew text...")

with open("day24/new_file.txt", mode="w") as file:
    file.write("New text.")

file.close()