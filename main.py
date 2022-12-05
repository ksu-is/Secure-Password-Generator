from optparse import AmbiguousOptionError
import random
import pygsheets



uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = ",./;'[]{}()*&%$#@!\\?-+_ "

upper, lower, nums, syms = True, True, True, True

all = ""

if upper: 
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms: 
    all += symbols

amount = 10

for x in range(amount):
    length_password = int(input("Please enter the required password length : "))
    # updated the message that the user sees when attempting to use the password generator.
    password = "".join(random.sample(all, length_password))
    print(f"Your password is : {password}")
    input("Would you like to create another password? Please type yes or no: ")
    break

yes = True
if True:
    for x in range(amount):
        length_password = int(input("Please enter the required password length : "))
        # updated the message that the user sees when attempting to use the password generator.
        password = "".join(random.sample(all, length_password))
        print(f"Your new password is : {password}") 
        #notifying the user that the new password has been generated
        input("Would you like to create another password? Please type yes or no: ")
        break
else:       
        break