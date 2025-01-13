# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Define Variables for greatest increase/decrease - both amount and month
greatest_increase_amount = 0 
greatest_increase_month = ""

greatest_decrease_amount = 0
greatest_decrease_month = ""

sum_of_change = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader) 

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader) 

    #take the value in the first row, second column (profit/losses) - idenitified by first_row[1]
    prior_profit_losses = int(first_row[1]) 

    # Track the total month and net change 
    total_months += 1  #count that first row as 1 month
    total_net += prior_profit_losses  #add that first row's profit/losses to the total net

    # Process each row of data
    for row in reader:

        # Track the total months
        total_months += 1  #count that row as 1 month

        # Track the net change -- sum the next row to total_net
        next_profit_losses = int(row[1]) #create a variable for the next row
        total_net += next_profit_losses  #add the next profit/losses to the total net

        # Calculate the change month by month
        change = next_profit_losses - prior_profit_losses

        # Calculate the greatest increase in profits (month and amount)
        if change > greatest_increase_amount:  #compare the change to what is stored in greatest increase
            greatest_increase_amount = change  #if the statement above was true, swap it out with the new change
            greatest_increase_month = row[0]   #if it was true, store that month in greatest increase month

        # Calculate the greatest decrease in losses (month and amount)
        if change < greatest_decrease_amount:  #compare the change to what is stored in greatest decrease
            greatest_decrease_amount = change  #if the statement above was true, swap it out with the new change
            greatest_decrease_month = row[0]   #if it was true, store that month in greatest decrease month

        # Calculate the average net change across the months - start with adding all of the change together
        sum_of_change += change

        # Update priot to the current row so it's ready for another loop
        prior_profit_losses = next_profit_losses

# Calculate the average net change across the months - divide the average_change by the number of months
# Subtract one away from the total month due to this calculation being for the change
average_change = round(sum_of_change / (total_months - 1), 2)

# Generate the output summary - use the """ for multi-lines and cleaner formatting
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${average_change}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount})
"""

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)