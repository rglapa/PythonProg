import pandas as pd

list = [
    {
        "Student": [{"Exam": 90, 'Grade':"a"},
                    {"Exam": 99, 'Grade':"b"},
                    {"Exam": 97, 'Grade':"c"}],
        "Name": "Paras Jain"
    },
    {
        "Student":[{'Exam': 89, 'Grade':"a"},
                   {'Exam': 80, 'Grade':"b"}],
        "Name": "Chunky Pandey"
    }
]

rows = []

for data in list:
    data_row = data['Student']
    time = data['Name']

    for row in data_row:
        row['Name'] = time
        rows.append(row)

df = pd.DataFrame(rows)

print(df)