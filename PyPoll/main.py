# import modules
import os, csv


# open the csv data file
poll_path = os.path.join("election_data.csv")


candidates = []
#numVotes = []
with open(poll_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # find header, skip header
    header = next(csvreader)
    print(header)
    numVote = 0
    for row in csvreader:
        candidates.append(row[2])
numVotes = len(candidates)
set = set(candidates)
uniqueCandidates = (list(set))

print(f'Election results')
print(f'<><><><><><><><><><><><><><><>')
print(f'Total votes: {numVotes}')
print(f'<><><><><><><><><><><><><><><>')
print(uniqueCandidates)
for x in uniqueCandidates:
    print(x)
