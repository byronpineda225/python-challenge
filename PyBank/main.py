#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   
# Author: Byron Pineda
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

months_counter = 0
net_total = 0
prior_months_total = 0
current_months_total = 0
net_changes = []
monthly_changes = []
average_changes = 0.00
net_delta = 0

# Method 2: Improved Reading using CSV module

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
        prior_months_total = int(row[1])
        net_changes.append(net_delta)
        monthly_changes.append(row[0])

# average_changes 
average_changes = round(sum(net_changes)/months_counter,2)     

# Date and time format used mm/dd//YYYY H:M:S
date_time_string = now.strftime("%m/%d/%Y %H:%M:%S")
print("Date/Time", date_time_string)	
print("")          
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {months_counter}')
print(f'Total: {net_total}')
print(f'Average Change: {average_changes}')

# Zip lists together
cleaned_csv = zip(net_changes, monthly_changes) 

# Get the maximum net changes and its associated da
xmax =  cleaned_csv

xmax = list(max(xmax))
print(f'Greatest Increase in Profits: {xmax[1]} (${xmax[0]})') 

cleaned_csv = zip(net_changes, monthly_changes) 

xmin = cleaned_csv

xmin = list(min(xmin))
print(f'Greatest Decrease in Profits: {xmin[1]} (${xmin[0]})') 

cleaned_csv = zip(net_changes, monthly_changes) 

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
    datafile.write(f'Greatest Increase in Profits: {xmax[1]} (${xmax[0]})\n')  
    datafile.write(f'Greatest Decrease in Profits: {xmin[1]} (${xmin[0]})\n') 







