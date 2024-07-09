import pandas

data = pandas.read_csv("day_25/great_squirrel_analysis/squirrel_census.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

count_gray_squirrels = len(gray_squirrels)
count_cinnamon_squirrels = len(cinnamon_squirrels)
count_black_squirrels = len(black_squirrels)

new_dict = {
    "Fur_color": ["Gray", "Cinnamon", "Black"],
    "Count": [
        f"{count_gray_squirrels}",
        f"{count_cinnamon_squirrels}",
        f"{count_black_squirrels}",
    ],
}
new_data = pandas.DataFrame(new_dict)
print(new_data)
new_data.to_csv("day_25/great_squirrel_analysis/new_data.csv")
