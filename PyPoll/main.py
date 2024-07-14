import os
import csv

# Imported election csv file and stored data in a list.
data_path = os.path.join("Resources","election_data.csv")
with open(data_path,"r") as data_file:
    data_reader=csv.reader(data_file,delimiter=",")
    header = next(data_reader)
    data= list(data_reader)

# Calculted total votes.
total_votes=len(data)

# Organized candidates and their votes in a dictionary.
candidate_votes={}
for row in data:
    candidate=row[2]

    if (candidate in candidate_votes) == False:
        candidate_votes[candidate] = 1
    else:
        candidate_votes[candidate] = candidate_votes[candidate] + 1

# Display result and store in file.
out_path = os.path.join("analysis","results.txt")
with open(out_path,"w") as txt_file:
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")

    # Calculated winner and percentage.
    winner=""
    highest_votes=0
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        vote_percent=(votes/total_votes)*100

        print(f"{candidate}: {vote_percent:0.3f}% ({votes})")
        txt_file.write(f"{candidate}: {vote_percent:0.3f}% ({votes})\n")

        if votes>highest_votes:
            highest_votes=votes
            winner=candidate

    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")