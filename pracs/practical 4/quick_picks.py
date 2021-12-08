import random

numbers_in_line = 6
maximum = 45
minimum = 1


def main():
    """Main program"""
    quick_picks_number = int(input("How many quick picks?: "))
    while quick_picks_number < 0:
        print("Invalid number")
        quick_picks_number = int(input("How many quick picks?: "))

    for i in range(quick_picks_number):
        quick_pick = []
        for j in range(numbers_in_line):
            number = random.randint(minimum, maximum)
            while number in quick_pick:
                number = random.randint(minimum, maximum)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))
        # I didn't quite understand how to print the answer so I copied it from solutions
        # Can you explain to me what "join" is?


main()
