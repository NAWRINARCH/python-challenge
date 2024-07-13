import csv
import os

path = os.path.join("Resources", "budget_data.csv")

with open(path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)
    data = list(csv_reader)

    total = 0
    for index in range(1, len(data)):
        total = total + (int(data[index][1]) - int(data[index-1][1]))
    
    print(total)
    print(total / (len(data)-1))