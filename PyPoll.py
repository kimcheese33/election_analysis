#retrieve data
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

#add dependencies
import os
import csv

#assign variable to load file from path
file_to_load = os.path.join("Resources","election_results.csv")

#assign variable to save file to path
file_to_save = os.path.join("analsis", "election_analysis.txt")

#initialize total vote counter
total_votes = 0

#initialize candidate list
candidate_options = []

#declare candidate/vote count dict
candidate_votes = {}

#winning candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open election results and read file
with open(file_to_load) as election_data:
    #read and analyze
    file_reader = csv.reader(election_data)

    #read header row
    headers = next(file_reader)
    
    #print each row in file
    for row in file_reader:

        #add to total counter
        total_votes += 1

        #get candidate name from row 3
        candidate_name = row[2]

        #if candidate not in list then add it
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #add candidate name as key in dict
            candidate_votes[candidate_name] = 0

        #add vote to candidate count
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = (float(votes) / float(total_votes)) * 100
    #print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name
        
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    
winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"-------------------------\n")
print(winning_candidate_summary)

