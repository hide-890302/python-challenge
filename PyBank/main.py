import os
import csv
import copy

# Path to collect data from the Resources folder
dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, "Resources", "budget_data.csv")


# Define blank list for month & profit
list_month = []
list_profit = []

# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Read csv file and create lists for "month" & "profit"
    for row in csvreader:
        list_month.append(row[0])
        list_profit.append(row[1])
    
# Calculate total month from csv file
total_months = len(list_month)

#Calculate total profit from csv file
list_profit_int = [int(x) for x in list_profit]
total_profit = sum(list_profit_int)
    
# Copy contents of "list_profit" to list_profit_a & b
list_profit_a = copy.copy(list_profit)
list_profit_b = copy.copy(list_profit)
    
# Delete first item in list "list_month"
list_month_delta = copy.copy(list_month)
del list_month_delta[0] #To make it Feb-2010 to Feb-2017
    
# Delete fist item in list "list_profit_a" and make values into integer
del list_profit_a[0] #To make it Feb-2010 to Feb-2017
list_profit_a_int = [int(x) for x in list_profit_a]

# Delete last item in list "list_profit_b" and make values into integer
del list_profit_b[total_months - 1] #To make it Jan-2010 to Jan-2017
list_profit_b_int = [int(x) for x in list_profit_b]

# Exclude "list_profit_b_int" from "list_profit_a_int"
# to calculate "list_profit_delta"
list_profit_delta = [x - y for (x, y) in zip(list_profit_a_int, list_profit_b_int)]
    
# Calculate average of profit delta
mean_profit_delta = round(sum(list_profit_delta) / len(list_profit_delta), 2)
    
# Create dictionary for profit delta and identify max & min
d_profit_delta = dict(zip(list_month_delta, list_profit_delta))
   
max_delta_month = max(d_profit_delta, key=d_profit_delta.get)
max_delta = max(d_profit_delta.values())

min_delta_month = min(d_profit_delta, key=d_profit_delta.get)
min_delta = min(d_profit_delta.values())

# Output Results
print("")
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${mean_profit_delta}")
print(f"Greatest Increase in Profits: {max_delta_month} (${max_delta})")
print(f"Greatest Decrease in Profits: {min_delta_month} (${min_delta})")
print("----------------------------")
print("")

# Output Results to text file

# Create New Folder
folder_path = os.path.join(dirname, "Analysis")
os.mkdir(folder_path)

# Create text file & output there
file_path = folder_path = os.path.join(dirname, "Analysis", "financial_analysis.txt")
f = open(file_path, "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write(f"Total Months: {total_months}\n")
f.write(f"Total: ${total_profit}\n")
f.write(f"Average Change: ${mean_profit_delta}\n")
f.write(f"Greatest Increase in Profits: {max_delta_month} (${max_delta})\n")
f.write(f"Greatest Decrease in Profits: {min_delta_month} (${min_delta})\n")
f.write("----------------------------\n")
f.close