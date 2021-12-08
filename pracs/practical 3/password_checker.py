minimum_length = 3


def main():
    password = get_password(minimum_length)
    convert_to_asterisks(password)


def get_password(min_length):
    password = input("Enter your password (At least {} characters): ".format(min_length))
    while len(password) < min_length:
        print("This password is too short!")
        password = input("Enter your password (At least {} characters): ".format(min_length))
    return password


def convert_to_asterisks(output):
    print("*" * len(output))



main()
