import os
from modules import utils


print('Welcome to the account manager!', '\n')

while True:
    print('Type 1 to save or update an account')
    print('Type 2 to view saved accounts')
    print('Type 3 to delete an account')
    print('Type 4 to exit the program', '\n')

    option = utils.validate_number('Type an option: ')
    while option > 4 or option < 1:
        print('Type a number from 1 to 3')
        option = utils.validate_number('Type an option: ')

    accountFolderPath = os.path.join('./', 'accounts')

    match(option):
        case 1:
            website_name = str(input('Enter the name of the website where you registered your account: '))
            registred_email = str(input('Enter the email address you registered on this website: '))
            registred_password = str(input('Enter the password you entered: '))

            print('Account registered successfully')
        case 4:
            break

print('Come back often!')
