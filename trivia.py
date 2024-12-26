import csv
import random #inclusive

def main():
    values = get_csv_file('data.csv')
    total_score = 0
    max_num = 5
    print("Welcome to Dota CL Triva!")
    for _ in range(5):
        triviaQuestion=get_trivia_question(values)
        total_score += play_game(triviaQuestion)
    print(f"Your total score is {total_score}/{max_num}")
    print("Thanks for playing!")



#populate dictionary with data.csv file
def get_csv_file(csvfile):
    with open(csvfile, newline='') as csvfile:
        reader = csv.reader(csvfile)
        values = {}
        for row in reader:
            key = row[0].strip()  # strip whitespace from the key
            value = row[1].strip()  # strip whitespace from the value
            values[key] = value
    return values

def get_trivia_question(dict):
    key = random.choice(list(dict.keys()))  # randomly select a key
    return key, dict[key] 

def play_game(triviaQuestion):
    hero = input(f"Who said this dota2 quote: \"{triviaQuestion[1]}\"? ") 

    score = 0
    if hero.lower().strip() == triviaQuestion[0].lower().strip():  # Compare ignoring case and leading/trailing spaces
        score += 1
        print("Outcome: Correct")
    else:
        print(f"Outcome: Wrong")
        print(f"Correct answer is {triviaQuestion[0]}")
    
    return score
main()