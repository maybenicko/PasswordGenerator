import random
import string


def gen_password(length):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    characters = letters + numbers + symbols

    password = ''.join(random.choice(characters) for i in range(length))

    return password


length = int(input("Input password length: "))
psw = gen_password(length)
print(psw)
