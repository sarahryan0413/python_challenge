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
candidate_list = []


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
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)


        # Add a vote to the candidate's count

print(candidate_list)
# Open a text file to save the output
#with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)


    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file
