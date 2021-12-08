def main():
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    if score > 100 or score < 1:
        print("Invalid score")
    elif score > 50:
        print("Passable")
    elif score > 90:
        print("Excellent")
    elif score < 50:
        print("Bad")


main()
