import pandas

data = pandas.read_csv("day_25/weather_data.csv")
print(data)
data_dict = data.to_dict()
print(data_dict)


temp_list = data["temp"].to_list()

avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

avg_temp = data["temp"].mean()
print(avg_temp)

max_temp = data["temp"].max()
print(max_temp)

# data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# create dataframe
new_data_dict = {"students": ["Amy", "James", "Maria"], "scores": [76, 56, 65]}

new_data = pandas.DataFrame(new_data_dict)
print(new_data)
new_data.to_csv("day_25/new_data.csv")
