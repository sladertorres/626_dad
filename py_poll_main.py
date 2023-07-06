'''Your task is to create a Python script that analyzes the votes and calculates each of the following:
The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.
As an example, your analysis should look similar to the one below: 

Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------

In addition, your final script should both print the analysis 
to the terminal and export a text file with the results'''





# Import Libraries
import os
import csv

# Set File Path for Input and Output
csvpath = os.path.join("C:\\Users\\joannegibson\\Desktop\\Resources\\election_data.csv")
file_to_output = "election_results.txt"

# Declaring the Variables 
total_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winner = ""




# Open the File
with open('election_data.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
 
    #loop through to find the total votes
    for row in csvreader:

        # Find the total vote count
        total_votes += 1

        candidate = row["Candidate"]
        # if statement to run on first occurence of candidate name
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        
        candidate_votes[candidate] = candidate_votes[candidate] + 1
#by the time this loop is done we should have a list of unique candidates
# as well as a dictionary with candidate names and corresponding votes


#another with statement to create output
#we are also finding winning candidate
with open(file_to_output, 'w') as txt_file:
    #create header
    election_header = (
        f"Election Results\n"
        f"---------------\n")
    txt_file.write(election_header)

    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)
        
    winning_summary = (
        f"Winner: {winner}"
    )
    print(winning_summary)
    txt_file.write(winning_summary)
