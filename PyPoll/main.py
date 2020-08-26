#import module
import os
import csv

#read/open csv file
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',' )
    header = next(csvreader)

#define the variables/lists
    candidates = []
    votes_per_candidate = []
    percent_votes_per_candidate = []
    total_votes = 0

#create loop
    for row in csvreader:
     total_votes += 1 
     if row[2] not in candidates:
        candidates.append(row[2])
        index = candidates.index(row[2])
        votes_per_candidate.append(1)
     else:
        index = candidates.index(row[2])
        votes_per_candidate[index] += 1
    
    for votes in votes_per_candidate:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes_per_candidate.append(percentage)
    
    # find the winner
    winner = max(votes_per_candidate)
    index = votes_per_candidate.index(winner)
    winning_candidate = candidates[index]
    
#print text

print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes_per_candidate[i])} ({str(votes_per_candidate[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

#output path to file
outputPath = os.path.join("PyPoll", "Analysis", "PyPoll-output.txt")
with open(outputPath, 'w') as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("--------------------------")
    txt_file.write(f"Total Votes: {str(total_votes)}")
    txt_file.write("--------------------------")
    for i in range(len(candidates)):
        txt_file.write(f"{candidates[i]}: {str(percent_votes_per_candidate[i])} ({str(votes_per_candidate[i])})")
    txt_file.write("--------------------------")
    txt_file.write(f"Winner: {winning_candidate}")
    txt_file.write("--------------------------")

    
    
    