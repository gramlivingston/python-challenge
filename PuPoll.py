import os
import csv

csvpath = os.path.join("election_data.csv")

with open(csvpath) as csvfile:

    csv_reader = csv.DictReader(csvfile, delimiter=',')
    csv_header = list(csv_reader.fieldnames)
    
    print(csv_header)
