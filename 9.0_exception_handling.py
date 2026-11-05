"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: the number of conversions of a campaign, typed by the user.
# 2. Process: I divide the campaign budget (1200) by the conversions to get
#    the cost per conversion. If the input is bad, I explain why and ask again.
#    The user gets 3 attempts. After 3 bad attempts the program stops politely.
# 3. Out: the cost per conversion printed in the terminal, or a clear message.
# 4. The two failures, and whether they deserve the same message:
#    - ValueError: the user typed something that is not a whole number ("abc",
#      or an empty line). Message: please type a whole number.
#    - ZeroDivisionError: the user typed 0, so the division is impossible.
#      Message: zero conversions means the cost cannot be calculated.
#    They need different messages because the user must fix different things.

# Your code below
# The budget I divide, and how many tries the user gets
budget = 1200
max_attempts = 3

# Why I catch each error separately instead of all errors at once:
# a bare "except" would also hide real bugs in my own code (like a typo in a
# variable name), and the user would get the same vague message for every
# problem. Catching each error separately lets me give the right message.

# Ask until the input works, or until the user runs out of attempts
attempt = 1
while attempt <= max_attempts:
    text = input(f"Number of conversions (attempt {attempt} of {max_attempts}): ")
    try:
        conversions = int(text)
        cost = budget / conversions
    except ValueError:
        print("Please type a whole number, like 40.")
    except ZeroDivisionError:
        print("Zero conversions: the cost per conversion cannot be calculated.")
    else:
        print(f"Cost per conversion: {cost:.2f}")
        break
    attempt += 1

# The while loop's "else" runs only if we never reached "break"
else:
    print("Too many invalid attempts. Stopping.")

# CHECK IT YOURSELF (result), four runs:
# 1. "40": printed "Cost per conversion: 30.00" and stopped normally.
# 2. "0": printed the zero conversions message, then asked again (attempt 2).
# 3. "abc": printed "Please type a whole number", then asked again.
# 4. Empty line, 3 times: the whole number message each time, then
#    "Too many invalid attempts. Stopping." The program never crashed.