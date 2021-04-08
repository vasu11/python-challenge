import os

import csv

csvpath = os.path.join('', 'Resources', 'budget_data.csv')

count = 0
net_total = 0
greatest_increase = 0
greatest_decrease = 0

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
        net_total = net_total + int(row[1])
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_date = row[0]

        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_date = row[0]

print ("total months: " + str(count))
print ("net total: " + str(net_total))
print ("greatest increase in profits: " + greatest_increase_date + " " + str(greatest_increase))
print ("Greatest decrease in profits: " + greatest_decrease_date + " " + str(greatest_decrease))

