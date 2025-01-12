# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_names_list = []
candidate_count_dict = {}

candidate_stats = ""

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count_tracker = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets) - shows the user that the program is working and not frozen
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1  #counts each row as 1 vote count

        # Get the candidate's name from the row
        candidate_name = row[2]  #candidates name is in the 3 column

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_names_list:
            candidate_names_list.append(candidate_name)

        # Add a vote to the candidate's count
        if candidate_name in candidate_count_dict:
            candidate_count_dict[candidate_name] += 1  #add one vote to their count
        else:
            candidate_count_dict[candidate_name] = 1  #add the candidate with 1 vote

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    #print(f"Total Votes: {total_votes}")

    # Write the total vote count to the text file
    txt_file.write(f"Total Votes: {total_votes}\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name in candidate_count_dict:
    
        # Get the vote count and calculate the percentage
        vote_count = candidate_count_dict[candidate_name]
        vote_percentage = (vote_count / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if vote_count > winning_count_tracker:  #compare the vote count to what is currently stored in winning count tracker
            winning_candidate = candidate_name  #set the candidate's name as winner
            winning_count_tracker = vote_count  #update the winning count tracker for next loop

        # Save each candidate's vote count and percentage 
        candidate_stats += f"{candidate_name}: {round(vote_percentage, 3)}% ({vote_count})\n"  #add \n for a new line 

    # Generate and print the winning candidate summary
    output = f"""
    Election Results
    -------------------------
    Total Votes: {total_votes}
    -------------------------
    {candidate_stats}
    -------------------------
    Winner: {winning_candidate}
    -------------------------
    """

    print(output)

    # Save the winning candidate summary to the text file
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)