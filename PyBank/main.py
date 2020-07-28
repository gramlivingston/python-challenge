import os
import csv

csvpath = os.path.join("resources/" "budget_data.csv")

with open(csvpath) as csvfile:

    csv_reader = csv.DictReader(csvfile, delimiter=',')
    csv_header = list(csv_reader.fieldnames)
    valuecol = (csv_header[1])
    monthcol = (csv_header[0])
    valueslist = []
    monthlist = []
    changelist = []

    for lines in csv_reader:
        valueslist.append(float(lines[valuecol]))
        monthlist.append(lines[monthcol])
        next
        
    numMonths = int(len(valueslist))

    for i in range(0,(numMonths-1),1):
        change = valueslist[i+1] - valueslist[i]
        changelist.append(change)
        next

    monthmax = monthlist[1+changelist.index(max(changelist))]
    monthmin = monthlist[1+changelist.index(min(changelist))]

    print(f"Total Months: {numMonths}")
    print(f"Total: {sum(valueslist)}")
    print(f"Average Change: {sum(changelist) / len(changelist)}")
    print(f"Greatest Increase in Profits: {monthmax} (${max(changelist)})")
    print(f"Greatest Decrease in Profits: {monthmin} (${min(changelist)})")

    


    

    

