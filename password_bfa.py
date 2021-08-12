import random
import string

password = str(input("Enter your password:"))

def get_random(num):
    while not None:
        rom_onetime = [random.choice(string.ascii_letters + string.digits) for i in range(num)]
        onetime = "".join(rom_onetime)
        print(onetime)
        if password == onetime:
            print("Found your password:{}".format(onetime))
            break

get_random(6)

