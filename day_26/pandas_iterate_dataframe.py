import pandas

student_dict = {"student": ["Murilo", "Camila", "Ana Julia"], "score": [76, 78, 75]}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through a dataframe
for key, value in student_data_frame.items():
    print(key, value)

# loop thru rows of a data frame
for i, row in student_data_frame.iterrows():
    print(row)
