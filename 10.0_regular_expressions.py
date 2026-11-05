"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In: three values typed by the user: a name, an Indian mobile number, an email.
# 2. Process: I check each value against its rule with a regular expression.
#    If a value breaks its rule, I say which field is wrong.
#    Only when all three pass do I save them.
# 3. Out: a message for each field (OK or wrong), and if all three are OK,
#    a new row in contacts.csv.
# 4. My three fields and their rules, in plain English:
#    - Name: only letters (A to Z, small or capital) and spaces, 2 to 30 characters.
#      Borderline case: "O'Brien" is rejected because of the apostrophe. I accept
#      that, to keep the rule simple, but it means some real names would fail.
#    - Mobile: exactly 10 digits, and the first digit is 6, 7, 8 or 9 (Indian
#      mobile numbers). "+91" in front, spaces or dashes are rejected.
#    - Email: some characters without spaces or @, then one @, then more
#      characters, then a dot, then at least 2 letters (like .com or .in).
# Your code below
import re
import csv
import os

# NAME pattern: [A-Za-z ]{2,30}
#   [A-Za-z ]   one character: a capital letter, a small letter, or a space
#   {2,30}      that character repeated between 2 and 30 times
name_pattern = r"[A-Za-z ]{2,30}"

# MOBILE pattern: [6-9][0-9]{9}
#   [6-9]       the first digit must be 6, 7, 8 or 9
#   [0-9]{9}    then exactly 9 more digits, so 10 digits in total
mobile_pattern = r"[6-9][0-9]{9}"

# EMAIL pattern: [^@\s]+@[^@\s]+\.[A-Za-z]{2,}
#   [^@\s]+     one or more characters that are NOT @ and NOT a space
#   @           exactly one @
#   [^@\s]+     again one or more characters, no @ and no space (like gmail)
#   \.          a real dot (the backslash means "a dot", not "any character")
#   [A-Za-z]{2,}  at least 2 letters at the end, like com or in
email_pattern = r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}"
# Ask the user for the three values
name = input("Name: ").strip()
mobile = input("Mobile: ").strip()
email = input("Email: ").strip()

# Check each value: fullmatch means the WHOLE value must follow the rule,
# not just a part of it
name_ok = re.fullmatch(name_pattern, name) is not None
mobile_ok = re.fullmatch(mobile_pattern, mobile) is not None
email_ok = re.fullmatch(email_pattern, email) is not None

# Tell the user which fields are OK and which are wrong
print("Name:  ", "OK" if name_ok else "wrong (letters and spaces only, 2 to 30)")
print("Mobile:", "OK" if mobile_ok else "wrong (10 digits, starting with 6 to 9)")
print("Email: ", "OK" if email_ok else "wrong (like name@example.com)")

# Save only when all three are OK, and write the header the first time
if name_ok and mobile_ok and email_ok:
    is_new_file = not os.path.exists("contacts.csv")
    with open("contacts.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if is_new_file:
            writer.writerow(["name", "mobile", "email"])
        writer.writerow([name, mobile, email])
    print("Saved to contacts.csv")
else:
    print("Not saved: fix the fields marked wrong.")

# CHECK IT YOURSELF (result), 9 values in 3 runs:
# Run 1, must pass: "Asha Rao", "9876543210", "asha@gmail.com"
#   -> all three OK, saved to contacts.csv.
# Run 2, must fail: "Asha123" (digits), "+919876543210" (has +91),
#   "asha gmail.com" (space, no @) -> all three wrong, not saved.
# Run 3, must fail: "O'Brien" (apostrophe), "1234567890" (starts with 1),
#   "asha@gmail" (no dot) -> all three wrong, not saved.
# Surprise: none of the results surprised me, but O'Brien shows that my name
# rule rejects some real names. I keep it simple on purpose.