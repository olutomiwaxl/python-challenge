#import libraries
import os
import csv
# set path to resource file
csvpath = os.path.join("..", "Resources", "election_data.csv")
# define empty list
voter_id = []
county = []
candidate = []
list_candidate = []
khan_list = []
correy_list = []
li_list = []
tooley_list = []

#open the csv file and read values into the empty list
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        #check winner row and append the corresponding Voter ID
        if row[2] == "Khan":
            khan_list.append(row[0])
        if row[2] == "Correy":
            correy_list.append(row[0])
        if row[2] == "Li":
            li_list.append(row[0])
        if row[2] == "O'Tooley":
            tooley_list.append(row[0])
    # append unique candidate to the candidate list
    for i in candidate:
        if i not in list_candidate:
            list_candidate.append(i)
# define variables for total votes and votes for each candidate    
total = len(voter_id) 
correy_t = len(correy_list)
khan_t = len(khan_list)
li_t = len(li_list)
tooley_t = len(tooley_list)

# calculate percentages
kp = round(((khan_t / total) * 100),4)
cp = round(((correy_t / total) * 100),4)
lp = round(((li_t / total) * 100),4)
tp = round(((tooley_t / total) * 100),4)

# print output
print("Election Results")
print("------------------------------------")
print("Total Votes: " + str(total))
print("------------------------------------")
print("Khan:  " + str(kp) + "% " + "(" + str(khan_t) + ")")
print("Correy:  " + str(cp) + "% " + "(" + str(correy_t) + ")")
print("Li:  " + str(lp) + "% " + "(" + str(li_t) + ")")
print("O'Tooley:  " + str(tp) + "% " + "(" + str(tooley_t) + ")")
print("------------------------------------")
print("Winner: Khan ")

# write output into  a text file 
f = open("output.txt","w+")  
f.write("Election Results\n")
f.write("------------------------------------\n")
f.write("Total Votes: " + str(total) + " \n")
f.write("------------------------------------\n")
f.write("Khan:  " + str(kp) + "% " + "(" + str(khan_t) + ")\n")
f.write("Correy:  " + str(cp) + "% " + "(" + str(correy_t) + ")\n")
f.write("Li:  " + str(lp) + "% " + "(" + str(li_t) + ")\n")
f.write("O'Tooley:  " + str(tp) + "% " + "(" + str(tooley_t) + ")\n")
f.write("------------------------------------\n")
f.write("Winner: Khan  \n")
f.write("------------------------------------\n")  
f.close()