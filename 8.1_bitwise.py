"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In: four permissions for a class assignment on Teams, each stored as one bit:
#    VIEW = 1 (0001), SUBMIT = 2 (0010), GRADE = 4 (0100), PUBLISH = 8 (1000).
# 2. Process: I combine VIEW and SUBMIT with | to make a student's permissions.
#    I test if GRADE is present with &. Then the student becomes a teaching
#    assistant: I add GRADE with | and remove SUBMIT with & and ~.
# 3. Out: the permission value printed in binary after each step.
# 4. My permissions are about who may view, submit, grade, and publish the
#    grades of a class assignment.
# Your code below
# Each permission is one bit
VIEW = 1      # 0001
SUBMIT = 2    # 0010
GRADE = 4     # 0100
PUBLISH = 8   # 1000

# A student can view and submit: combine the two bits with |
student = VIEW | SUBMIT
print("Student:              ", format(student, "04b"))

# Test if GRADE is present: & keeps only the GRADE bit, 0 means it is absent
print("Can grade?            ", (student & GRADE) != 0)

# The student becomes a teaching assistant: add GRADE with |
assistant = student | GRADE
print("After adding GRADE:   ", format(assistant, "04b"))

# A teaching assistant does not hand in work: remove SUBMIT with & and ~
assistant = assistant & ~SUBMIT
print("After removing SUBMIT:", format(assistant, "04b"))

# CHECK IT YOURSELF (result):
# Reading the bits right to left (VIEW, SUBMIT, GRADE, PUBLISH):
# Student = 0011: VIEW and SUBMIT on. Can grade? False, the GRADE bit is 0.
# After adding GRADE = 0111: GRADE turned on.
# After removing SUBMIT = 0101: SUBMIT turned off, VIEW and GRADE stay on.
# PUBLISH stays 0 the whole time: only the teacher can publish grades.
