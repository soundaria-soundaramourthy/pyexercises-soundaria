# read_campaigns: opens the CSV file and returns every row as a dictionary
import csv

def read_campaigns(filename):
    with open(filename, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

rows = read_campaigns("practice.csv")
print(len(rows), rows[0])

# to_number: turns text like "1200,50" into the number 1200.50
def to_number(text):
   return float(text.replace(",", "."))

print(to_number("1200,50"))
print(to_number("800,00") + 1)

# get_ctr: returns clicks divided by impressions, or None if impressions is empty
def get_ctr(row):
   if row["impressions"].strip() == "": 
       return None
   return float(row["clicks"]) / float(row["impressions"])

print(get_ctr(rows[0]))
print(get_ctr(rows[2]))

# get_cpa: returns cost divided by conversions, or None if there are no conversions
def get_cpa(row):
   if float(row["conversions"]) == 0:
        return None
   return to_number(row["cost"]) / float(row["conversions"])

print(get_cpa(rows[0]))
print(get_cpa(rows[1]))

# get_roas: returns revenue divided by cost
def get_roas(row):
    return to_number(row["revenue"]) / to_number(row["cost"])

print(get_roas(rows[0]))

# build_campaigns: goes through every row, skips rows with empty impressions, and keeps the name, channel, conversions and the three indicators
def build_campaigns(rows):
    campaigns = []
    for row in rows:
        ctr = get_ctr(row)
        if ctr is None:
            continue
        campaigns.append({"name": row["name"], "channel": row["channel"], "conversions": float(row["conversions"]), "ctr": ctr, "cpa": get_cpa(row), "roas": get_roas(row)})
    return campaigns
campaigns = build_campaigns(rows)
print(len(campaigns))
for c in campaigns: print(c["name"], c["cpa"])

# best_ctr: returns the name of the campaign with the highest CTR
def best_ctr(campaigns):
    return max(campaigns, key=lambda c: c["ctr"])["name"]

print(best_ctr(campaigns))

# highest_cpa: returns the name of the campaign with the highest CPA, ignoring campaigns that have no CPA
def highest_cpa(campaigns):
    with_cpa = [c for c in campaigns if c["cpa"] is not None]
    return max(with_cpa, key=lambda c: c["cpa"])["name"]

print(highest_cpa(campaigns))

# count_high_roas: counts the campaigns whose ROAS is above 3
def count_high_roas(campaigns):
    return len([c for c in campaigns if c["roas"] > 3])

print(count_high_roas(campaigns))

# best_channel: adds up the conversions of each channel and returns the channel with the most
def best_channel(campaigns):
    totals = {}
    for c in campaigns:
        totals[c["channel"]] = totals.get(c["channel"], 0) + c["conversions"]
    return max(totals, key=totals.get)

print(best_channel(campaigns))

# average_ctr: returns the average CTR of all the campaigns, rounded to two decimals
def average_ctr(campaigns):
    return round(sum(c["ctr"] for c in campaigns) / len(campaigns), 2)

print(average_ctr(campaigns))

# ask_question: asks one question, compares the answer with the correct one, and returns 1 for right or 0 for wrong
def ask_question(question, correct_answer):
    answer = input(question + " ")
if answer.strip().lower() == str(correct_answer).strip().lower():
    print("Correct!")
else:
    print("Wrong! The correct answer is:", correct_answer)
    return 0

# run_quiz: asks the five questions one by one, using the computed answers, and returns the total score
def run_quiz(campaigns):
    score = 0
    score = score + ask_question("1. Which campaign has the best CTR?", best_ctr(campaigns))
    score = score + ask_question("2. Which campaign has the highest CPA?", highest_cpa(campaigns))
    score = score + ask_question("3. How many campaigns have a ROAS above 3?", count_high_roas(campaigns))
    score = score + ask_question("4. Which channel generated the most conversions?", best_channel(campaigns))
    score = score + ask_question("5. What is the average CTR across all campaigns (2 decimals)?", average_ctr(campaigns))
    return score

# save_result: writes the player name, the score and today's date into result.csv.
def save_result(name, score):
    with open("result.csv", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([name, score, date.today()])

# main: runs the whole program in order: read, clean, ask the player, show the score, save the result
def main():
    rows = read_campaigns("practice.csv")
    campaigns = build_campaigns(rows)
    name = input("Player name: ")
    score = run_quiz(campaigns)
    print("Final score:", score, "/ 5")
    save_result(name, score)

main()


    


