# import modules
import os, csv
from collections import Counter


# create various lists
candidates = []    #list of all items in candidates column
votes = []     #list of number of votes per candidate
votesPCT = [] # list of percentage of votes per candidate

# open the csv data file
poll_path = os.path.join("election_data.csv")

with open(poll_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # find header, skip header
    header = next(csvreader)
    # add all votes into list
    for row in csvreader:
        candidates.append(row[2])

# get total number of votes
numVotes = len(candidates)
# create a set of candidates and then a list of unique candidates

# use Counter to create a dictionary of canidates and number of
# times they occur in the list / votes they recieved
resultsDict = Counter(candidates)

# get a list of the keys within the dictionary, this is a list of unique Candidates
keys = list(resultsDict)
# return the length of unique candidates
lenKeys = len(keys)

# print some structure and context
print(f'Election results')
print(f'<><><><><><><><><><><><><><><>')
print(f'Total votes: {numVotes}')
print(f'<><><><><><><><><><><><><><><>')

# for each unique candidate, take the number of votes recieved and put into another list.
# then, calculate the percentage. Print the results for each candidate
for y in range(lenKeys):
    votes.append(resultsDict[keys[y]])
    votesPCT.append(round(float(resultsDict[keys[y]]/numVotes)*100,2))
    print(f'Candidate: {keys[y]} | Votes: {votes[y]} | Percentage: {votesPCT[y]}') #float(resultsDict[keys[y]])
# find the max vote value and return the candidate and percentage in the same list position
print(f'<><><><><><><><><><><><><><><>')
maxVotesPos = votes.index(max(votes))
print(f'The winner is {keys[maxVotesPos]} with {votesPCT[maxVotesPos]} percent of the votes')

# open new txt file and write the same things to it
f = open("poll_summary.txt", "w+")

f.write("Election Results\n")
f.write("<><><><><><><><><><><><><><><>\n")
f.write(f'Total votes: {numVotes}\n')
f.write(f'<><><><><><><><><><><><><><><>\n')
for y in range(lenKeys):
    votes.append(resultsDict[keys[y]])
    votesPCT.append(round(float(resultsDict[keys[y]]/numVotes)*100,2))
    f.write(f'Candidate: {keys[y]} | Votes: {votes[y]} | Percentage: {votesPCT[y]}\n')
f.write(f'<><><><><><><><><><><><><><><>\n')
f.write(f'The winner is {keys[maxVotesPos]} with {votesPCT[maxVotesPos]} percent of the votes\n')
