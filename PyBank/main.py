#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
# Author: Byron Pineda  Date: 6/21/2021
#   
#   A Python script was created for analyzing the financial records of a company.
#   The budget data was analyzed for records to calculate some key metrics: 
#       - The total number of months included in the dataset "budget_data.csv".
#       - The net total amount of "Profit/Losses" over the entire period.
#       - Calculate the changes in "Pfofit/Losses" over the entire period. Then
#         calculate the average of those changes.    
#       - The greatest increase in profits (date/amount) over the entire period.
#       - The greatest decrease in profits (date/amount) over the entire period.
#
#   The script prints the analysis to the terminal and exports a text file with
#   the results.
#
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Module for Operating Systems
import os

# Module for reading CSV files
import csv

# Module for getting date/time
from datetime import datetime
now = datetime.now()

# Define the path and data file to be used.
csvpath = os.path.join("Resources","budget_data.csv")

# Define the variables and lists. Initialize them as needed.

# Contains the net total amount of "Profit/Losses" over the entire period
net_total = 0

# This contains the Profit/Losses difference between current 
# and prior month.
net_delta = 0

# This is used to hold the Profit/Losses from the prior month.
#prior_months_total = 0
prior_months_total = 0

# The next 2 lists hold the net changes and corresponding dates
# over the entire period.

net_changes = []
monthly_changes = []

# Holds the number of months in the data file used for analysis.
months_counter = 0

# Hold the average changes over the entire period.
average_changes = 0.00

# Improved Reading using CSV module

with open(csvpath) as csvfile:
     
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    next(csvreader)

    for row in csvreader:
       
        # Total months counter
        months_counter += 1

        # The net total amount of "Profit/Losses" over the entire period
        net_total += int(row[1]) 
  
        # Calculate the average change in Profits/Losses over the entire period

        net_delta = int(row[1]) - prior_months_total
        net_changes.append(net_delta)
        monthly_changes.append(row[0])
        prior_months_total =int(row[1])
        
# average changes over the entire period.
average_changes = round(sum(net_changes)/months_counter,2)     

# Obtain the maximum net changes in list, get its index, 
# and use it to find the corresponding date in the date list.
max_delta =  max(net_changes)
idx_max = net_changes.index(max_delta)
max_month = monthly_changes[idx_max]

# Obtain the minimum net changes in list, get its index, 
# and use it to find the corresponding date in the date list.
min_delta =  min(net_changes)
idx_min = net_changes.index(min_delta)
min_month = monthly_changes[idx_min]

# Print out key budget itmes to the terminal 
# Set the Date and time format used mm/dd//YYYY H:M:S 
# when the script was executed.

date_time_string = now.strftime("%m/%d/%Y %H:%M:%S")
print("Date/Time", date_time_string)	
print("")          
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {months_counter}')
print(f'Total: {net_total}')
print(f'Average Change: {average_changes}')
print(f'Greatest Increase in Profits: {max_month} (${max_delta})') 
print(f'Greatest Decrease in Profits: {min_month} (${min_delta})') 

# Set variable for output file
output_file = os.path.join("analysis","budget_final_analysis.txt")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

# Write the results of the analysis to the text file "budget_final_analysis.txt"

    datafile.write(f'Date/Time {date_time_string}\n')	
    datafile.write("\n")    
    datafile.write("Financial Anaylsis\n") 
    datafile.write("----------------------------\n")
    datafile.write(f'Total Months: {months_counter}\n')
    datafile.write(f'Total: {net_total}\n')
    datafile.write(f'Average Change: {average_changes}\n')
    datafile.write(f'Greatest Increase in Profits: {max_month} (${max_delta})\n')  
    datafile.write(f'Greatest Decrease in Profits: {min_month} (${min_delta})\n') 