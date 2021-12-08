"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_quantity = int(input("How many months? "))

    for month in range(1, month_quantity + 1):
        str(month)
        income = float(input("Enter income for month {}:  ".format(month)))
        incomes.append(income)
    print_report(incomes)


def print_report(incomes):
    # This function will print report
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month + 1, income, total))


main()
