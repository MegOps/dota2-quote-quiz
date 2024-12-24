import csv

# Open the file
with open('quotes.csv', newline='') as csvfile:
    # Initialize CSV reader
    reader = csv.reader(csvfile)
    
    # Iterate over each row in the CSV
    for row in reader:
        # Each row is a list of columns
        print(row)
