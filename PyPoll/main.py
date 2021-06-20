#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
# Author: Byron Pineda
#   
#   A Python script was created tasked with helping a small, rural town modernize 
#   its vote counting process.
#   
#   The Python script analyzes the votes and calculates each of the following key metrics: 
#       - The total number of votes cast in the dataset "election_data.csv".
#       - A complete list of candidates who received votes.
#       - The percentage of votes each candidate won.  
#       - The total number of votes each candidate won.
#       - The winner of the election based on popular vote.
#
#   The script prints the analysis to the terminal and exports a text file with
#   the results.
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Module for Operating Systems
import os

# Module for reading CSV files
import csv
from typing import TYPE_CHECKING

# Define the path and data file to be used.
csvpath = os.path.join("Resources","election_data.csv")

net_votes = 0
vote_count = 0

candidates_name_list = ['Khan','Correy','Li','O\'Tooley']
candidates_votes_list = []
candidates_votes_percent = []
candidate_votes_Khan = 0
candidates_votes_Correy = 0
candidates_votes_Li = 0
candidates_votes_OTooley = 0

with open(csvpath) as csvfile:
     
    # CSV reader specifies delimiter and variable that holds contents
    poll_reader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    next(poll_reader)

    for row in poll_reader:
       
        # The net total amount of votes
        net_votes += 1 

        vote_count += 1
        if row[2] == 'Khan':
            candidate_votes_Khan += 1
        elif row[2] == 'Correy':    
            candidates_votes_Correy += 1
        elif row[2] == 'Li':
            candidates_votes_Li += 1
        else:
            row[2] == 'O\'Tooley'
            candidates_votes_OTooley += 1
        

candidates_votes_list = [candidate_votes_Khan,candidates_votes_Correy,
                        candidates_votes_Li,candidates_votes_OTooley]
candidates_votes_percent = [candidate_votes_Khan/net_votes*100, candidates_votes_Correy/net_votes*100,
                           candidates_votes_Li/net_votes*100,candidates_votes_OTooley/net_votes*100]                         

votes_for_each = candidates_name_list + candidates_votes_percent + candidates_votes_list  


# Set the winning votes tallied by default to the first 
# vote in the list and once the maximum is obtained then
# associate it with the candidates name list.  
# The defaults variables are assigned below.

the_winner_is = candidates_votes_list[0]
the_winning_candidate_is = candidates_name_list[0]

for i in candidates_votes_list:
    if i > the_winner_is:
        the_winner_is = candidates_votes_list[i]
        the_winning_candidate_is = candidates_name_list[i]
      
print("Election Results") 
print("----------------------------")
print(f'Total Votes: {net_votes}')
print("----------------------------")
print(f'{candidates_name_list[0]}: {candidates_votes_percent[0]:.3f}% ({candidates_votes_list[0]})')
print(f'{candidates_name_list[1]}: {candidates_votes_percent[1]:.3f}% ({candidates_votes_list[1]})')
print(f'{candidates_name_list[2]}: {candidates_votes_percent[2]:.3f}% ({candidates_votes_list[2]})')
print(f'{candidates_name_list[3]}: {candidates_votes_percent[3]:.3f}% ({candidates_votes_list[3]})')
print("----------------------------")
print(f'Winner: {the_winning_candidate_is}') 
print("----------------------------")

# Set variable for output file

output_file = os.path.join("analysis","election_analysis.txt")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

# Write the results of the analysis to the text file "election_analysis.txtt"

    datafile.write("Election Results\n") 
    datafile.write("----------------------------\n")
    datafile.write(f'Total Votes: {net_votes}\n')
    datafile.write("----------------------------\n")
    datafile.write(f'{candidates_name_list[0]}: {candidates_votes_percent[0]:.3f}% ({candidates_votes_list[0]})\n')
    datafile.write(f'{candidates_name_list[1]}: {candidates_votes_percent[1]:.3f}% ({candidates_votes_list[1]})\n')
    datafile.write(f'{candidates_name_list[2]}: {candidates_votes_percent[2]:.3f}% ({candidates_votes_list[2]})\n')
    datafile.write(f'{candidates_name_list[3]}: {candidates_votes_percent[3]:.3f}% ({candidates_votes_list[3]})\n')
    datafile.write("----------------------------\n")
    datafile.write(f'Winner: {the_winning_candidate_is}\n') 
    datafile.write("----------------------------\n")

