"""
CP1404/CP5632 Practical
Colours' codes
"""

colour_codes = {"Absolutezero": "#0048ba", "Azure1": "#f0ffff", "Bistre": "#3d2b1f", "Blond": "#faf0be",
                "Aquamarine1": "#7fffd4", "Apricot": "#fbceb1", "Amethyst": "#9966cc", "Olivine": "#9ab973",
                "Pear": "#d1e231", "Raspberry": "#e30b5d"}

colour_name = input("Enter the color name: ").capitalize()
while colour_name != "":
    print("The code for {} is {}".format(colour_name, colour_codes.get(colour_name)))
    colour_name = input("Enter the color name: ").capitalize()
print("Thank you!")
