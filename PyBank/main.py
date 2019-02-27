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
    changes = list(changes)
    average = (sum(changes) / len(changes))
    average_r = round(average,2)
    max_change = max(changes)
    min_change = min(changes)
    a = changes.index(max_change)
    b = date[a + 1]
    c = changes.index(min_change)
    d = date[c + 1]
    
print("Financial Analysis")
print("----------------------------------------------")
print("Total months: " + str(len(date)))
print("Total: " + "$" + str(sum(int_profit)))
print("Average Change: " + "$" +  str(average_r))
print("Greatest Increase in profits: " + str(b) + " " + "(" + "$" + str(max_change) + ")")
print("Greatest decrease in profits: " + str(d) + " " + "(" + "$" + str(min_change) + ")")


f = open("output.txt","w+")  
f.write("Financial Analysis\n")
f.write("----------------------------------------------\n")  
f.write("Total months: " + str(len(date)) + " \n")     
f.write("Total: " + "$" + str(sum(int_profit)) + " \n")
f.write("Average Change: " + "$" +  str(average_r) + " \n")
f.write("Greatest Increase in profits: " + str(b) + " " + "(" + "$" + str(max_change) + ")\n")
f.write("Greatest decrease in profits: " + str(d) + " " + "(" + "$" + str(min_change) + ")\n")
f.close()