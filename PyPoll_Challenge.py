#dependencies.
import csv
import os

#variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
#variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

#initialize a total vote counter.
total_votes = 0

#candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

#county list and county votes dictionary.
county_options = []
county_votes = {}

# track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# track the largest county and county voter turnout.
winning_county_count = 0
winning_county_percentage = 0
winning_county = ''


#read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    #read the header
    header = next(reader)

    #for each row in the CSV file.
    for row in reader:

        #add total vote count
        total_votes = total_votes + 1

        #get candidate name from each row.
        candidate_name = row[2]

        #extract the county name from each row.
        county_name = row[1]

        #if candidate doesn't match any existing candidate add it to candidate list
        if candidate_name not in candidate_options:

            #add candidate name to candidate list.
            candidate_options.append(candidate_name)

            #begin tracking candidate's voter count.
            candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #decision statement that checks county does not match any existing county in county list.
        if county_name not in county_options:

            #add existing county to list of counties.
            county_options.append(county_name)

            #begin tracking county's vote count.
            county_votes[county_name] = 0

        # add a vote to that county's vote count.
        county_votes[county_name] += 1


#save results to text file.
with open(file_to_save, "w") as txt_file:

    #print the final vote count
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    #write a repetition statement to get the county from county dictionary.
    for county_name in county_votes:
        #retrieve county vote count.
        vote = county_votes[county_name]
        #calculate percent of total votes for county.
        county_percentage = float(vote) / float(total_votes) * 100

         #print county results to terminal.
        county_results = (f"{county_name}: {county_percentage:.1f}% ({vote:,})\n")
        print(county_results)
         #save county votes to text file.
        txt_file.write(county_results)
         #write decision statement to determine winning county and get vote count.
        if (vote > winning_county_count) and (county_percentage > winning_county_percentage):
            winning_county_count = vote
            winning_county_percentage = county_percentage
            winning_county = county_name

    #print county with largest turnout to terminal.
    winning_county_summary = (
    f"\n-------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"-------------------------\n")
    print(winning_county_summary)

    #save county with largest turnout to text file.
    txt_file.write(winning_county_summary)

    #save final candidate vote count to text file.
    for candidate_name in candidate_votes:

        #retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #print each candidate's voter count and percentage to terminal.
        print(candidate_results)
        #save candidate results to text file.
        txt_file.write(candidate_results)

        #determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    #print winning candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    #save winning candidate's name to text file
    txt_file.write(winning_candidate_summary)
