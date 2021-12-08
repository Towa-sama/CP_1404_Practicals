total = 0
item_number = int(input("Enter the amount of items: "))
while item_number < 0:
    print("Invalid input: ")
    item_number = int(input("Enter the amount of items: "))
for i in range(item_number):
    item_price = float(input("Price of item: "))
    total += item_price
if total > 100:
    total = total / 100 * 10
print("Total price for {} items is {}".format(item_number, total))
