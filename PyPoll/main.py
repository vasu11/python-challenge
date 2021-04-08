import os

import csv

csvpath = os.path.join('', 'Resources', 'election_data.csv')

count = 0
x = 0
cand = 0
candidates = []
candidate_votes = []
num_votes = 0

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

file1 = open("Election_Results.txt", "a")
file1.write("Election Results\n")
file1.write("----------------------\n")
file1.write("Total Votes: " + str(count) + "\n") 
file1.write("----------------------\n")

print ("Election Results")
print ("----------------------")
print ("Total Votes: " + str(count))
print ("----------------------")
for cand in candidates:
    person = cand
    votes_index = candidates.index(person)
    if (candidate_votes[votes_index] > num_votes):
        winner = person
    num_votes = candidate_votes[votes_index]
    percentage_votes = (num_votes / count) * 100
    print (person + ": " + str(round(percentage_votes,3)) + "% (" + str(num_votes) + ")")
    file1.write(person + ": " + str(round(percentage_votes,3)) + "% (" + str(num_votes) + ")\n")

print ("----------------------")
print ("Winner: " + winner)

file1.write("----------------------\n")
file1.write("Winner: " + winner)

        



