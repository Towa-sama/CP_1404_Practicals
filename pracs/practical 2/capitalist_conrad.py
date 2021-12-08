import random

output_file = "stock.txt"
out_file = open(output_file, 'w')

price = float(10.00)
day = 0
print("Starting price: ${}".format(price), file=out_file)
while 1000 >= price >= 0.01:
    change = 0
    day += 1
    if random.randint(1, 2) == 1:
        change = random.uniform(0, 0.1)

    else:
        change = random.uniform(-0.05, 0)

    price *= (1 + change)
    print("On day {} price is: ${:.2f}".format(day, price), file=out_file)

out_file.close()
