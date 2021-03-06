import os
import csv
import collections


# Path to collect data from the Resources folder
dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, "Resources", "election_data.csv")

# Define blank list for Poll Result
list_poll = []

# Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    # Read third column of data after the header and put them into "list_poll"
    for row in csvreader:
        list_poll.append(row[2])

# Summarize the result in dictionary named "results"
results = collections.Counter(list_poll)

# Calculate total votes
total = int(sum(results.values()))

print("")
print("Election Results")
print("-------------------------")
print("Total Votes: "+str(total))
print("-------------------------")

# Output Results for each Candidates
for k, v in results.items():

    # Calculate Percentage & round off to 3 decimal places
    percent = round(100*v/total, 3)
    
    print(k+":", str(percent)+"%", "("+str(v)+")")

print("-------------------------")

# Output Winner
winner = max(results, key=results.get)
print("Winner: " + winner)

print("-------------------------")
print("")

# Output Results to text file

# Create New Folder
folder_path = os.path.join(dirname, "Analysis")
os.mkdir(folder_path)

# Create text file & output there
file_path = folder_path = os.path.join(dirname, "Analysis", "election_results.txt")
f = open(file_path, "w")

f.write("Election Results\n")
f.write("-------------------------\n")
f.write(f"Total Votes: {str(total)}\n")
f.write("-------------------------\n")

for k, v in results.items():
    percent = round(100*v/total, 3)
    
    f.write(f"{k}:{str(percent)}%, ({str(v)})\n")

f.write("-------------------------\n")
winner = max(results, key=results.get)
f.write(f"Winner: {winner}\n")
f.write("-------------------------\n")
f.close