import os
import csv
import numpy

csvpath = os.path.join("..", "Resources", "budget_data.csv")
date = []
profit = []
int_profit = []
changes = []
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        date.append(row[0])
        profit.append(row[1])
    for i in profit:
        int_profit.append(int(i))
    changes = numpy.diff(int_profit)
    average = (sum(changes) / len(changes))
    max_change = max(changes)
    min_change = min(changes)

    


print("Financial Analysis")
print("----------------------------------------------")
print("Total months: " + str(len(date)))
print("Total: " + str(sum(int_profit)))
print("Average Change: " + str(average))
print("Greatest Increase in profits: " + str(max_change))
print("Greatest decrease in profits: " + str(min_change))