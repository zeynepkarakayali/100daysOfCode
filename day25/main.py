# import csv

# temperatures = []
# with open("day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#             print(temperatures)

import pandas

# data = pandas.read_csv("day25/weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data["temp"].mean())
# print(f"the max value is: {data['temp'].max()}")

# Get data in columns
# print(data["condition"])
# print("\n")
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# max_temp = int(data["temp"].max())
# print(data[data.temp == max_temp])

# monday_temp = data[data.day == "Monday"].temp[0]
# monday_fahr = (monday_temp *(9/5)) + 32
# print(f"monday fahrenheit: {monday_fahr}")

# Create dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [53, 76, 93]
}
data = pandas.DataFrame(data_dict)
data.to_csv("day25/new_data.csv")
