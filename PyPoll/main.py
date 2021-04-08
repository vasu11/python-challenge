import os

import csv

csvpath = os.path.join('', 'Resources', 'election_data.csv')

count = 0
x = 0
candidates = []
candidate_votes = []

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
        found_candidate = "no"
        if count == 1:
            candidates.append(row[2])
            candidate_votes.append(count)
        else:
            for x in candidates:
                if x == row[2]:
                    index = candidates.index(row[2])
                    candidate_votes[index] = candidate_votes[index] + 1
                    found_candidate = "yes"
                    break
            if found_candidate == "no":
                candidates.append(row[2])
                candidate_votes.append(1) 
            #        candidates.append(row[2])
            #        candidate_votes.append(1)
            #    else:
                    #index = candidates.index(row[2])
                    # candidate_votes[index] = candidate_votes[index] + 1
        if count == 10:
            break

print ("candidates " + str(len(candidates)))
    
        



