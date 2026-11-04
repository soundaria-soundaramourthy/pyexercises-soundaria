"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In: the subject I studied and how many minutes, typed by the user.
#    The date is taken automatically from today's date.
# 2. Process: check the input. If the subject is empty, or the minutes are not
#    a whole number above 0, I print an error and ask again.
#    If study_log.csv does not exist yet, I write the header line first.
#    Then I add the new row at the end of the file (append mode, so old rows stay).
# 3. Out: the file study_log.csv with the columns: date, subject, minutes
# 4. Why these columns, and what this file is for: I want to track my studying.
#    With 200 rows I could add up the minutes per subject to see which subjects
#    I study the most and which ones I neglect, and see how much I study each week.


# Your code below
import csv
import os
from datetime import date

# Ask for the subject, and ask again if the user types nothing
subject = input("Subject: ").strip()
while subject == "":
    print("The subject cannot be empty.")
    subject = input("Subject: ").strip()

# Ask for the minutes, and ask again until it is a whole number above 0
minutes = input("Minutes: ").strip()
while not minutes.isdigit() or int(minutes) == 0:
    print("Please type a whole number above 0, like 45.")
    minutes = input("Minutes: ").strip()
minutes = int(minutes)
# Check if the file exists yet: if not, I must write the header line first
file_name = "study_log.csv"
is_new_file = not os.path.exists(file_name)

# Open in append mode ("a") so old rows are kept, then add the new row
with open(file_name, "a", newline="") as f:
    writer = csv.writer(f)
    if is_new_file:
        writer.writerow(["date", "subject", "minutes"])
    writer.writerow([date.today().isoformat(), subject, minutes])

print("Saved to", file_name)

# CHECK IT YOURSELF (result):
# I ran the program 3 times: python/45, maths/30 (0 was refused first), english/20.
# study_log.csv has 4 lines: exactly 1 header line and 3 entries.
# So the header is only written the first time, and append mode keeps old rows.
# Bad input was refused: an empty subject, "abc" and 0 for minutes.