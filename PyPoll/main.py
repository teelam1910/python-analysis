#Columns  "Voter ID", "County", and "Candidate"
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote


import csv
data = csv.DictReader(open('Resources/election_data.csv')) #header update from reader; use DictReader (this makes header a pare of every record)
my_report = open('analysis/Election_Report.txt','w')


# variables
# Store the number of total votes and store the votes each candidate received individually
total_votes = 0
can_list = {}
win_votes = 0

for row in data:    #loop through data, looking through every row in data
    total_votes += 1      #votes = votes + 1
    candidate = row["Candidate"]

    if candidate not in can_list.keys():
        can_list[candidate] = 0
    
    can_list[candidate] += 1

#template
output = f'''
Election Results
-------------------------
Total Votes: {total_votes:,}
-------------------------
'''

for candidate in can_list.keys():
    votes = can_list[candidate]
    if votes > win_votes:
        win_votes = votes
        winner = candidate
       
    output += f'{candidate}: {votes/total_votes*100: .3f}% ({votes:,})\n'

output += f'-------------------------\nWinner: {winner}\n-------------------------'

print(output)
my_report.write(output)