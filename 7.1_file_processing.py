"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# -Lines 3 and 9 are empty. They are not names, so I must skip them
# -Lines 4 and 7 have spaces at the start, so I must remove them
# -The capital letters are mixed up (ada LOVELACE, grace hopper, GUIDO van rossum)
#  I must make every name look the same, like Ada Lovelace
# - Line 8 (GUIDO van rossum) has 3 words, not 2, so I need a rule for
#   which part is the last name

# 1. In: the file names.txt (10 lines: 8 names and 2 empty lines)
# 2. Process, problem by problem:
# - Empty lines: I skip any line that is empty after removing spaces
# - Spaces at the start: I use strip() on every line to remove them
# - Mixed capitals: I use title() so every name looks like "Ada Lovelace"
# - 3-word name: I take everything after the first word as the last name
# Then I sort the names by last name, ignoring capital letters
# 3. Out:a new file called names_clean.txt, one name per line, sorted
#    by last name. names.txt is only read, never changed
# 4. How I decide which word is the last name:the first word is the first
#    name, and everything after it is the last name. So "Guido van Rossum"
#    has the last name "van Rossum" (his real surname), and he sorts under V


# Your code below
# Open names.txt in read mode and put every line into a list
with open("names.txt", "r") as f:
    lines = f.readlines()

print("Lines read:", len(lines))

# Go through each line: remove spaces, skip empty lines, fix the capitals
clean_names = []
for line in lines:
    name = line.strip()
    if name == "":
        continue
    clean_names.append(name.title())

print("Clean names:", len(clean_names))
print(clean_names)

# Sort by last name: everything after the first word, in lowercase
def last_name(full_name):
    return full_name.split(" ", 1)[1].lower()

clean_names.sort(key=last_name)
print("Sorted:", clean_names)

# Write the sorted names to a new file, one per line (names.txt is not touched)
with open("names_clean.txt", "w") as f:
    for name in clean_names:
        f.write(name + "\n")

print("Saved to names_clean.txt")

# CHECK IT YOURSELF (result):
# wc -l says names.txt has 10 lines and names_clean.txt has 8 lines.
# The difference is 2 because my program skipped the 2 empty lines (3 and 9).
# All 8 real names are in the output.
# First name in the sorted list: Margaret Hamilton (H, earliest last name).
# Last name in the sorted list: Guido Van Rossum (V, because "van rossum"
# is his last name with my rule). I checked both by hand.
# Known limit: title() writes "Van" with a capital V, his real name uses "van".