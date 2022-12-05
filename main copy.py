from optparse import AmbiguousOptionError
import random
import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='/Users/zay/Downloads/python-project-v2-841b5a84b10d.json')


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

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['John', 'Steve', 'Sarah']

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('PY to Gsheet Test')

#select the first sheet 
wks = sh[0]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(df,(1,1))

        # updated the message to alert the user that the new password has been generated.
        