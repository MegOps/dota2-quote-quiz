import csv
import random #inclusive

def main():
    values = get_csv_file('data.csv') 
    triviaQuestion=get_trivia_questions(values)
    print(triviaQuestion)


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

def get_trivia_questions(dict):
    key = random.choice(list(dict.keys()))  # randomly select a key
    return key, dict[key] 


main()