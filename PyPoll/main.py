#PyPoll Challenge
import os
import csv

election_csv = "Resources/election_data.csv"

#Lists
candidatesList = []
candidateVotes = []

#Variables
currCounty = ""
currCandidate = ""
currVoter = ""
winner = ""
totalVotes = 0
winVotes = 0
i = 0

#Add all candidates to Candidates List & tally total votes
with open(election_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader:
        totalVotes += 1
        currCandidate = row[2]

        if currCandidate not in candidatesList:
            candidatesList.append(currCandidate)


#Loop through Candidates List to tally toal votes for each candidates
while i < len(candidatesList):
    votesCounter = 0

    #Loop through csv file
    with open(election_csv, 'r') as csvfile:

        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
    
        for row in csvreader:
            currVoter = row[0]
            currCandidate = row[2]

            #Tally votes for selected candidate
            if currCandidate == candidatesList[i]:
                votesCounter += 1
    
    #Keep track of winning candidate and their votes
    if winVotes < votesCounter:
        winVotes = votesCounter
        winner = candidatesList[i]

    candidateVotes.append(votesCounter)    
    i += 1

      
#Print Analysis
print('Election Results')
print('-------------------------')
print(f'Total Votes: {totalVotes}')
print('-------------------------')
i = 0  
while i < len(candidatesList):
    print(f'{candidatesList[i]}: {round(candidateVotes[i]/totalVotes * 100, 3)}% ({candidateVotes[i]})')
    i += 1
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

#Export to existing txt file 
#switch 'w' to 'x' to create new txt file
election_txt = open('election_data.txt','w')

#Overwite to print following text
election_txt.write('Election Results\n')
election_txt.write('-------------------------\n')
election_txt.write(f'Total Votes: {totalVotes}\n')
election_txt.write('-------------------------\n')
i = 0  
while i < len(candidatesList):
    election_txt.write(f'{candidatesList[i]}: {round(candidateVotes[i]/totalVotes * 100, 3)}% ({candidateVotes[i]})\n')
    i += 1
election_txt.write('-------------------------\n')
election_txt.write(f'Winner: {winner}\n')
election_txt.write('-------------------------\n')