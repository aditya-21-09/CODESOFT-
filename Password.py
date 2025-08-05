import random
chars="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#$%^&*()"
length = int(input("Enter length : "))
password = ""
for i in range(length):
    password +=random.choice(chars)
print(f"your password is {password}")
