import os
from modules import utils, manage_accounts


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

            manage_accounts.save_account(
                accountFolderPath,
                website_name,
                registred_email,
                registred_password)

            print('Account registered successfully')
        case 2:
            print('Saved accounts: ')
            
            try:
                files_count = -1
                for iterator, file_name in enumerate(os.listdir(accountFolderPath)):
                    print(f'{iterator}: {file_name.replace('.json', '')}')
                    files_count += 1

                while True:
                    print()
                    website_number = utils.validate_number(
                        'Enter the number of the site you want to see your account details for: ')
                    
                    if website_number <= files_count and website_number >= 0:
                        break
                    
                    print('Enter a valid number!')

                manage_accounts.read_accounts(accountFolderPath, website_number)
            except FileNotFoundError:
                print('Register an account to view registered accounts', '\n')
        case 4:
            break

print('\n', 'Come back often!')
