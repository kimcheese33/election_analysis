# Election Audit

## Overview of Project

The purpose of this project was to analyze election data from a CSV file to come up with the candidate and county that won. In order to accomplish this goal, we used Python. Through this project we learned how to read data from a CSV file, analyze the data to get the desired result, and finally write that result to a text file.

## Results
- How many votes were cast in this congressional election?

There were 369,711 votes cast.

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

Jefferson county received 38,855 votes, which is 10.5% of the total vote. Denver received 306,055 votes, which is 82.8% of the total vote. Finally, Arapahoe received 24,801 votes, which is 6.7% of the total votes.

- Which county had the largest number of votes?

Denver had the largest number of votes.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

Charles Casper Stockham received 85,213 votes, which is 23% of the total votes. Diana DeGette received 272,892 votes, which was 73.8% of the total votes. Finally, Raymon Anthony Doane received 11,606 votes, which was 3.1% of the total votes.

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

Diana DeGette won the election with 272,892 votes, which was 73.8% of the total vote.

### Results at a glance:

<img src="https://github.com/kimcheese33/election_analysis/blob/main/Resources/election_results.png" width="300" height="400" />

## Summary
In summary, Python is a powerful tool that can produce quick, accurate election results. Furthermore, this script can be adapted for future elections. For example, this script could be easily modified for a national election. If the CSV file contained state instead of county data, all we would have to do is modify some variable names and the output text. Alternatively, if the CSV file contained an additional state column, we could just add another state variable in the file read section like so: state_name = row[<state column number>]. Then we would just mimick how we calculated the county results to produce state results. Another example of how this script can be used differently is if we wanted to also find out what percentage of voters voted by party, such as Republican or Democrat. IF the CSV contained the candidate's party affiliation we could extract that column in the file read section, store the party name in a list, then in the write section perform similar calculations to find total votes and percentages. It is my recommendation that we move forward with using a Python script to calculate future election results.
