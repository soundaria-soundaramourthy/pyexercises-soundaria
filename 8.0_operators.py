"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In: two strings, "Python" and "python" (same word, different capital P).
# 2. Process: I compare them with ==, !=, <, >, <=, >= and then combine
#    some results with and, or, not.
# 3. Out: a table printed in the terminal, one line per comparison,
#    showing the comparison and True or False.
# 4. My two values: "Python" and "python".
#    The result that surprised me: "Python" < "python" is True, because Python
#    compares character codes and capital P (80) comes before small p (112).
# Your code below
# The two values I want to compare
a = "Python"
b = "python"

# Every comparison, plus some logical combinations, as (description, result) pairs
results = [
    ("a == b", a == b),
    ("a != b", a != b),
    ("a < b", a < b),
    ("a > b", a > b),
    ("a <= b", a <= b),
    ("a >= b", a >= b),
    ("(a != b) and (a < b)", (a != b) and (a < b)),
    ("(a == b) or (a > b)", (a == b) or (a > b)),
    ("not (a == b)", not (a == b)),
]

# Print a readable table: the description in a column 25 wide, then the result
print(f"a = {a!r}, b = {b!r}")
print(f"{'Comparison':<25}Result")
print("-" * 32)
for description, result in results:
    print(f"{description:<25}{result}")

# CHECK IT YOURSELF (result):
# Before running, I predicted a == b is False and a < b is False.
# I got 1 out of 2 right: a < b is actually True (capital letters come first).
