import csv
import random #inclusive

def main():
    values = get_csv_file('data.csv')
    total_score = 0
    max_num = 5
    used_keys = set()

    print("Welcome to Dota CL Triva!")
    for _ in range(max_num):
        trivia_question = get_trivia_question(values, used_keys)
        if trivia_question:  # Check if we can still get a trivia question
            total_score += play_game(trivia_question)
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

def get_trivia_question(dic,used_keys):
    available_keys = [key for key in dic.keys() if key not in used_keys]
    if not available_keys:
        return None  # If no more questions are available, return None
    key = random.choice(available_keys)
    used_keys.add(key)
    return key, dic[key]

def play_game(triviaQuestion):
    hero = input(f"Who said this dota2 quote: \"{triviaQuestion[1]}\"? ") 

    score = 0
    if hero.lower().strip() == triviaQuestion[0].lower().strip():  # Compare ignoring case and leading/trailing spaces
        score += 1
        print("Outcome: Correct")
    else:
        print(f"Outcome: Wrong")
        print(f"Answer is {triviaQuestion[0]}")
    
    return score
main()