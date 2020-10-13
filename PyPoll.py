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

#open election results and read file
with open(file_to_load) as election_data:
    #read and analyze
    file_reader = csv.reader(election_data)

    #print headers
    headers = next(file_reader)
    print(headers)