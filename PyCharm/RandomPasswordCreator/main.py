import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$"

password = "".join(random.choices(characters, k=9))

print(f"Your password is: {password}")