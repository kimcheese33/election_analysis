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
file_to_save = os.path.join("analysis", "election_analysis.txt")

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

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:        

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = (float(votes) / float(total_votes)) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #write results to text file
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
            
        

        
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

