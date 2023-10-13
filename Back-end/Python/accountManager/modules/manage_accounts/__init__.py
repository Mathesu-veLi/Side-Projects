import os
import json


def save_account(account_folder_path: str, website_name: str, registred_email: str, registred_password: str):
    """Saves the account data in a json file with the name of the website where the account was registered

    Args:
        account_folder_path (str): Name of the folder in which the account is saved
        website_name (str): name of the website where the account was created
        registred_email (str): email address registered on the site
        registred_password (str): password registered on the site
    """

    data_registered_on_the_website = {
        'name': website_name,
        'email': registred_email,
        'password': registred_password
    }

    try:
        os.mkdir(account_folder_path)
    except FileExistsError:
        pass
    finally:
        with open(f'{account_folder_path}/{website_name}.json', '+w', encoding='utf-8') as file:
            json.dump(data_registered_on_the_website, file)


def read_accounts(account_folder_path: str):
    """Reads existing json files in the given path

    Args:
        account_folder_path (str): Path to search for account files
    """

    if not os.listdir(account_folder_path):
        print('Register an account to view registered accounts')

    for file_name in os.listdir(account_folder_path):
        with open(f'{account_folder_path}/{file_name}', 'r', encoding='utf-8') as file:
            data = json.load(file)

            print('\n', data['name'].center(55))
            print(data['email'].ljust(35), end='')
            print(data['password'].rjust(20))
