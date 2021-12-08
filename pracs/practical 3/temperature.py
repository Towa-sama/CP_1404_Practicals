MENU = """C - Convert Celsius to Fahrenheit
  F - Convert Fahrenheit to Celsius
  Q - Quit"""


def main():
    print(MENU)


def convert_to_fahrenheit(celcius):
    celcius * 9.0 / 5 + 32
    return celsius


def convert_to_celcius(fahrenheit):
    5 / 9 * (fahrenheit - 32)
    return fahrenheit


choice = input(">>> ").upper()

while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = convert_to_fahrenheit(celsius)
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = convert_to_celcius(fahrenheit)
        print("Result: {:.2f} C".format(celsius))
        pass
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.") #sdsdsdsdsdsdssd

main()
