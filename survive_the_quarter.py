# Name: Soundaria Soundaramourthy - Group A
# # I built this step by step with help from Claude (AI). The full chat is in CONVERSATION.md
#
# 1. What goes in? scenarios_A.csv. Separator: comma. 14 columns: ID, Scenario,
#    OptionA/B/C, BudgetA/B/C, ReputationA/B/C, FeedbackA/B/C.
#    Numbers are plain integers, losses have a minus sign (-5), no "+" or "EUR".
#    Texts with commas inside are between quotes.
# 2. What happens in one day?
#    - show the day number, budget and reputation
#    - show the situation and options A, B, C
#    - ask A, B or C until the answer is valid
#    - change budget and reputation, show the feedback
#    - stop the game if budget or reputation is 0 or less
# 3. What comes out? "Fired" (and why) or my final score and title, plus my best
#    and worst move. One line in results.csv: name,budget,reputation,title,date
# 4. What could go wrong?
#    - The player types a wrong letter: I ask again until it is A, B or C.
#    - Reputation goes above 100: I set it back to 100.
#    - A gauge goes to 0 or below: the game stops at once.
#
# Feature chosen: d) Difficulty (easy 15,000 EUR or hard 6,000 EUR),
# because it lets the player choose how hard the game is.

# Tools I need: csv to read/write files, random to shuffle, date for today's date
import csv
import random
from datetime import date


# Reads my scenario file and returns a list of scenarios.
# Each scenario is a tuple (situation, options).
# Each option is a tuple (text, budget_change, reputation_change, feedback).
def load_scenarios(filename):
    scenarios = []
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            options = []
            for letter in ["A", "B", "C"]:
                option = (row["Option" + letter], int(row["Budget" + letter]),
                          int(row["Reputation" + letter]), row["Feedback" + letter])
                options.append(option)
            scenarios.append((row["Scenario"], options))
    return scenarios


# Asks the player for A, B or C, and asks again until the answer is valid.
# Returns the position of the chosen option: 0 for A, 1 for B, 2 for C.
def ask_choice():
    answer = input("Your choice (A, B or C): ").strip().upper()
    while answer not in ["A", "B", "C"]:
        answer = input("Please type A, B or C: ").strip().upper()
    return "ABC".index(answer)


# Applies the chosen option to the two gauges.
# Returns a tuple (new_budget, new_reputation). Reputation can never go above 100.
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(reputation + reputation_change, 100)
    return budget, reputation


# Works out the final score of a player who survived, and the matching title.
# Returns a tuple (score, title).
def get_title(budget, reputation):
    score = reputation + budget // 200
    if score >= 140:
        title = "Viral Legend"
    elif score >= 120:
        title = "CMO Material"
    elif score >= 95:
        title = "Growth Hacker"
    else:
        title = "Eternal Intern"
    return score, title


# Adds one line for this game at the end of results.csv:
# name, budget, reputation, title, date
def save_result(name, budget, reputation, title):
    with open("results.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, budget, reputation, title, date.today()])


# My feature (d): asks the player for easy or hard, and returns the starting budget.
def choose_difficulty():
    level = input("Difficulty, easy or hard? ").strip().lower()
    while level not in ["easy", "hard"]:
        level = input("Please type easy or hard: ").strip().lower()
    if level == "easy":
        return 15000
    return 6000


# Plays up to 10 days. Returns a tuple (budget, reputation, history).
# history has one tuple per day: (reputation_change, day, option_text)
def play_days(scenarios, budget, reputation):
    history = []
    for day in range(1, 11):
        situation, options = scenarios[day - 1]
        print(f"\n--- Day {day} ---")
        print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
        print(situation)
        for letter, option in zip("ABC", options):
            print(f" {letter}: {option[0]}")
        option = options[ask_choice()]
        budget, reputation = apply_choice(budget, reputation, option)
        print(option[3])
        print(f"Budget {option[1]:+} EUR, Reputation {option[2]:+}")
        history.append((option[2], day, option[0]))
        if budget <= 0 or reputation <= 0:
            break
    return budget, reputation, history


# Main program: set up the game, play it, show the result, save it
name = input("Your name: ").strip()
budget = choose_difficulty()
reputation = 50
scenarios = load_scenarios("scenarios_A.csv")
random.shuffle(scenarios)
budget, reputation, history = play_days(scenarios, budget, reputation)
print("=" * 30)
if budget <= 0 or reputation <= 0:
    reason = "budget" if budget <= 0 else "reputation"
    title = "Fired"
    print(f"You are fired! Your {reason} hit zero.")
else:
    score, title = get_title(budget, reputation)
    print(f"Quarter survived! Budget left: {budget} EUR, reputation: {reputation}/100")
    print(f"Final score: {score}")
    print(f"{name}, your title: {title}")
# Best and worst move: tuples compare the first element first (reputation change)
best = max(history)
worst = min(history)
print(f'Best move: day {best[1]}, "{best[2]}" ({best[0]:+})')
print(f'Worst move: day {worst[1]}, "{worst[2]}" ({worst[0]:+})')
save_result(name, budget, reputation, title)
print("Saved in results.csv")