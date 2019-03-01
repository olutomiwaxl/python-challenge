#import libraries
import os
import csv 

#read csv
csvpath = os.path.join("..", "Resources", "employee_data.csv")

#define empty lists
Emp_ID = []
Name = []
DOB = []
SSN_new = []
State = []
First_name = []
Last_name = []
date_formatted = []
#use state libraries
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
#read csv document and append to lists 
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        Emp_ID.append(row[0])
        Name.append(row[1])
        date = row[2]
        date_split = date.split("-")
        #use new date format
        date_formatted.append(f"{date_split[1]}/{date_split[2]}/{date_split[0]}")
        ssn = row[3]
        #star out the first 5 characters of SSN
        ssn_split = ssn.split("-")
        SSN_new.append(f"***-**-{ssn_split[2]}")
        State.append(us_state_abbrev[row[4]])  
#split the name into two lists
    for i in Name:
        First_name.append(i.split(" ")[0])
        Last_name.append(i.split(" ")[1])
    
#zip all lists together
roster = zip(Emp_ID, First_name, Last_name, date_formatted, SSN_new, State)

output_file = os.path.join("output.csv")
#write output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    writer.writerows(roster)