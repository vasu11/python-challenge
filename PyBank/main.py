import os

import csv

csvpath = os.path.join('', 'Resources', 'budget_data.csv')

count = 0
net_total = 0
greatest_increase = 0
greatest_decrease = 0
current_value = 0
previous_value = 0
change_amount = 0
change_count = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        count = count + 1
        current_value = int(row[1])
        net_total = net_total + int(row[1])
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_date = row[0]

        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_date = row[0]
        
        if ((current_value > 0 and previous_value < 0) or (current_value < 0 and previous_value > 0)):
            change_count = change_count + 1
            change_amount = change_amount + current_value
       # (current_value < 0 and previous_value > 0)):


        previous_value = current_value

change_avg = change_amount / change_count
print ("Total Months: " + str(count))
print ("Total: $" + str(net_total))
print ("Average Change: $" + str(change_avg))
print ("Greatest Increase in Profits: " + greatest_increase_date + " $" + str(greatest_increase))
print ("Greatest Decrease in Profits: " + greatest_decrease_date + " $" + str(greatest_decrease))

file1 = open("Financial_Analysis.txt", "a")
file1.write("Financial Analysis\n")
file1.write("---------------------\n")
file1.write("Total Months: " + str(count) + "\n")
file1.write("Total: $" + str(net_total) + "\n")
file1.write("Average Change: $" + str(change_avg) + "\n")
file1.write("Greatest Increase in Profits: " + greatest_increase_date + " $" + str(greatest_increase) + "\n")
file1.write("Greatest Decrease in Profits: " + greatest_decrease_date + " $" + str(greatest_decrease) + "\n")
file1.close()

