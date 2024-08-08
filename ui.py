from colorama import Fore, Style, init
from tabulate import tabulate
from messages import get_messages

init()

class UserInterface:
    def __init__(self):
        self.language = None
        self.messages = None

    def select_language(self):
        welcome_message = f"""
{Fore.CYAN}
 _   _  ___ _   ___ __  __ __ ___   _____ __    __ ____   __ __   __  _     _  _ ___ _   ___ ___ ___  
| | | || __| | / _//__\|  V  | __| |_   _/__\  |  V  \ `v' /' _/ /__\| |   | || | __| | | _,\ __| _ \ 
| 'V' || _|| || \_| \/ | \_/ | _|    | || \/ | | \_/ |`. .'`._`.| \/ | |_  | >< | _|| |_| v_/ _|| v / 
!_/ \_!|___|___\__/\__/|_| |_|___|   |_| \__/  |_| |_| !_! |___/ \_V_\___| |_||_|___|___|_| |___|_|_\ 

Development for Juanses03
{Style.RESET_ALL}
"""
        print(welcome_message)
        print("1. Español")
        print("2. English")
        try:
            self.language = int(input("Select language: "))
            self.messages = get_messages(self.language)
        except ValueError:
            print(f"{Fore.RED}Invalid option. {Style.RESET_ALL}")
            exit()

    def display_menu(self, options):
        for key, value in options.items():
            print(f"{key}. {value}")

    def get_input(self, prompt):
        return input(prompt)

    def show_table(self, table_name, table_description):
        headers = [i[0] for i in table_description]
        print(tabulate(table_description, headers=headers, tablefmt='grid'))

    def show_message(self, message):
        print(message)
