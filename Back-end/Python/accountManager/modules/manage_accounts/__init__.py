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

