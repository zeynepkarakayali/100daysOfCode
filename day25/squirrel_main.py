import pandas

data = pandas.read_csv("day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black_squirrel = data[data["Primary Fur Color"] == "Black"]
len_black = len(black_squirrel)
# print(len_black)
# print(black_squirrel)
gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
len_gray = len(gray_squirrel)
cinnamon_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
len_cinnamon = len(cinnamon_squirrel)

new_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len_gray, len_cinnamon, len_black],
}

dF = pandas.DataFrame(new_dict)
dF.to_csv("day25/squirrel_dataFrame.csv")