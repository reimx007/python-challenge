# import modules
import os, csv
from collections import Counter

# open the csv data file
poll_path = os.path.join("election_data.csv")


candidates = []
numVote = 0
with open(poll_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # find header, skip header
    header = next(csvreader)
    print(header)
    for row in csvreader:
        candidates.append(row[2])
numVotes = len(candidates)
set = set(candidates)
uniqueCandidates = (list(set))
resultsDict = Counter(candidates)

print(f'Election results')
print(f'<><><><><><><><><><><><><><><>')
print(f'Total votes: {numVotes}')
print(f'<><><><><><><><><><><><><><><>')
#print(uniqueCandidates)
for x in uniqueCandidates:
    print(x)
print(resultsDict)
keys = list(resultsDict)
lenKeys = len(keys)
votes = []
votesPCT = []
for y in range(lenKeys):
    votes.append(resultsDict[keys[y]])
    votesPCT.append(round(float(resultsDict[keys[y]]/numVotes)*100,2))
    print(f'Candidate: {keys[y]} | Votes: {votes[y]} | Percentage: {votesPCT[y]}') #float(resultsDict[keys[y]])
maxVotesPos = votes.index(max(votes))

print(f'The winner is {keys[maxVotesPos]} with {votesPCT[maxVotesPos]} percent of the votes')
# print(votes)
# print(maxVotesPos)
# print(votesPCT)
