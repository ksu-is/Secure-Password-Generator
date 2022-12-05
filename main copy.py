from optparse import AmbiguousOptionError
import random
pip install https://github.com/nithinmurali/pygsheets/archive/staging.zip


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
    length_password = int(input("Hello, please enter the required password length : "))
    # updated the message that the user sees when attempting to use the password generator.
    password = "".join(random.sample(all, length_password))
    print(f"Your password is : {password}")
    
# updated to a while loop to give users the option to generate another password. 

    new_password=input("Would you like to create another password? Please type yes or no:")

    if new_password == 'yes':
            length_password = int(input("Please enter the required password length : "))
            password = "".join(random.sample(all, length_password))
            print(f"Your new password is : {password}")
            print('Thanks for using Secure Password Generator!')
            

    else:
        print(f'Thanks for using Secure Password Generator!\nYour password is:')
        break
print((password))


        # updated the message to alert the user that the new password has been generated.
        