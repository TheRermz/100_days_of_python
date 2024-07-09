numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Murilo"
new_list = [letter for letter in name]
print(new_list)

num = [n * 2 for n in range(1, 5)]
print(num)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Fred"]
short_names = [name.upper() for name in names]
print(short_names)
