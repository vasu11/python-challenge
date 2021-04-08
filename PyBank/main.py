import os

import csv

csvpath = os.path.join('', 'Resources', 'budget_data.csv')

count = 0
net_total = 0

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

print ("net total: " + str(net_total))
