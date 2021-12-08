"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = int(input("Enter your sales: "))
bonus = 0
while sales >= 0:
    if sales >= 1000:
        bonus = sales / 100 * 15
        print("Your sale bonus is: {}".format(bonus))
    elif sales < 1000:
        bonus = sales / 100 * 10
        print("Your sale bonus is: {}".format(bonus))
    else:
        print("Invalid option")
    sales = int(input("Enter your sales: "))
print("Thank you")
