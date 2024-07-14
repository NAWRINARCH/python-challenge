import os
import csv

# Imported budget csv file and stored data in a list.
data_path = os.path.join("Resources","budget_data.csv")
with open (data_path, "r") as data_file :
    data_reader=csv.reader(data_file,delimiter=",")
    header=next (data_reader)
    data = list(data_reader)

# Calculating the number of months.
month = len(data)

# Calculated total profit.
total_profits=0
for row in data:
    total_profits =total_profits+int(row[1])

# Calculated average change in profit, 
# highest change and lowest change.
total=0
highest =int(data[0][1])
highest_month =data[0][0]
lowest= int(data[0][1])
lowest_month=data[0][0]

for index in range(len(data)-1):
    current=data[index][1]
    future=data[index+1][1]
    difference=int(future)-int(current)
    total=total+difference

    if difference > highest:
        highest_month = data[index+1][0]
        highest=difference
    if difference < lowest:
        lowest_month = data[index+1][0]
        lowest=difference

avg_change = total/(month - 1)

# Displaying results.
print("Financial Analysis" )
print("----------------------------")
print(f"Total Month: {month}")
print(f"Total: ${total_profits}")
print(f"Average Change: ${avg_change:0.2f}")
print(f"Greatest Increase in Profits: {highest_month} (${highest})")
print(f"Greatest Decrease in Profits: {lowest_month} (${lowest})")

out_path = os.path.join("analysis","results.txt")
with open(out_path,"w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Month: {month}\n")
    txt_file.write(f"Total: ${total_profits}\n")
    txt_file.write(f"Average Change: ${avg_change:0.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {highest_month} (${highest})\n")
    txt_file.write(f"Greatest Decrease in Profits: {lowest_month} (${lowest})\n")