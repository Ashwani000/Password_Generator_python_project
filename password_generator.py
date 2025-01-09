import random
print("*" *50)
print("Here is you password Generator Application")
print("*" *50)

chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM,.;!@#$%^&*()?123456789"

number=input("Enter the number of passwords you want to generate:")
number =  int(number)
length=input("Enter the length of password:")
length=int(length)

for pwd in range(number):
    passwords=""
    for c in range(length):
        passwords +=random.choice(chars)

    print(passwords)




