from colorama import Fore, Style, init
from tabulate import tabulate
from messages import get_messages

init(autoreset=True)


class UserInterface:
    def __init__(self):
        self.language = None
        self.messages = None

    def select_language(self):
        # Welcome message with language options
        welcome_message = f"""
{Fore.CYAN}
 _   _  ___ _   ___ __  __ __ ___   _____ __    __ ____   __ __   __  _     _  _ ___ _   ___ ___ ___  
| | | || __| | / _//__\|  V  | __| |_   _/__\  |  V  \ `v' /' _/ /__\| |   | || | __| | | _,\ __| _ \ 
| 'V' || _|| || \_| \/ | \_/ | _|    | || \/ | | \_/ |`. .'`._`.| \/ | |_  | >< | _|| |_| v_/ _|| v / 
!_/ \_!|___|___\__/\__/|_| |_|___|   |_| \__/  |_| |_| !_! |___/ \_V_\___| |_||_|___|___|_| |___|_|_\ 

Development by JuansesDev
{Style.RESET_ALL}
"""
        print(welcome_message)
        print(f"{Fore.MAGENTA}1. {Fore.YELLOW}Español{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}2. {Fore.YELLOW}English{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}3. {Fore.YELLOW}Français{Style.RESET_ALL}")

        while True:
            try:
                self.language = int(
                    input(f"{Fore.CYAN}Select language: {Style.RESET_ALL}")
                )
                if self.language not in [1, 2, 3]:
                    raise ValueError
                self.messages = get_messages(self.language)
                break
            except ValueError:
                print(
                    f"{Fore.RED}Invalid option. Please enter 1, 2, or 3.{Style.RESET_ALL}"
                )

    def display_menu(self, options):
        # Display menu options with styling
        print(f"\n{Fore.MAGENTA}{'=' * 40}{Style.RESET_ALL}")
        for key, value in options.items():
            print(f"{Fore.YELLOW}{key}. {Fore.CYAN}{value}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{'=' * 40}{Style.RESET_ALL}")

    def get_input(self, prompt):
        # Get user input with error handling
        try:
            return input(prompt)
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Fore.RED}Input interrupted. Exiting...{Style.RESET_ALL}")
            exit()
    
    def get_confirmation(self, message):
        """Get user confirmation for destructive operations"""
        confirmation_prompt = f"{Fore.YELLOW}{message} (yes/no): {Style.RESET_ALL}"
        while True:
            response = self.get_input(confirmation_prompt).lower().strip()
            if response in ['yes', 'y', 'si', 'sí', 'oui']:
                return True
            elif response in ['no', 'n', 'non']:
                return False
            else:
                print(f"{Fore.RED}Please enter 'yes' or 'no'{Style.RESET_ALL}")
    
    def get_valid_identifier(self, prompt):
        """Get a valid SQL identifier from user"""
        from sql_utils import SQLIdentifierValidator
        while True:
            name = self.get_input(prompt).strip()
            if not name:
                continue
            if SQLIdentifierValidator.is_valid_identifier(name):
                return name
            else:
                print(f"{Fore.RED}Invalid name. Use only letters, numbers, and underscores. Must start with letter or underscore. Max 64 characters.{Style.RESET_ALL}")

    def show_table(self, table_name, table_description):
        # Display a formatted table
        headers = [i[0] for i in table_description]
        print(f"\n{Fore.GREEN}Table: {Fore.YELLOW}{table_name}{Style.RESET_ALL}")
        print(tabulate(table_description, headers=headers, tablefmt="fancy_grid"))

    def show_message(self, message):
        # Display a styled message
        print(f"\n{Fore.BLUE}{message}{Style.RESET_ALL}")
