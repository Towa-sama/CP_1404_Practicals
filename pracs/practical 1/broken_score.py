"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


score = float(input("Enter score: "))
if score > 100 or score < 1:
    print("Invalid score")
elif score > 50:
    print("Passable")
elif score > 90:
    print("Excellent")
elif score < 50:
    print("Bad")

