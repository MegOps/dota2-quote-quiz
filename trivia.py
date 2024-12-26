import csv

def main():
    values = get_csv_file('data.csv') 
    print(values)


#populate dictionary with data.csv file
def get_csv_file(csvfile):
    with open(csvfile, newline='') as csvfile:
        reader = csv.reader(csvfile)
        Values = {}
        for row in reader:
            key = row[0]
            value = row[1]
            Values[key] = value
    return Values

main()