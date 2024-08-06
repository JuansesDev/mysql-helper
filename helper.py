import os
import mysql.connector
from dotenv import load_dotenv
from colorama import Fore, Style, init
from tabulate import tabulate

# Initialize colorama
init()

# Load environment variables from .env file
load_dotenv()

# Connect to the database
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

# Messages in Spanish and English
messages_es = {
    "option": f"{Fore.YELLOW}Ingrese la opción: {Style.RESET_ALL}",
    "create_db": f"{Fore.GREEN}Crear una nueva base de datos{Style.RESET_ALL}",
    "use_db": f"{Fore.GREEN}Utilizar una base de datos existente{Style.RESET_ALL}",
    "db_name": f"{Fore.CYAN}Ingrese el nombre de la nueva base de datos: {Style.RESET_ALL}",
    "list_dbs": f"{Fore.CYAN}Bases de datos existentes:{Style.RESET_ALL}",
    "create_table": f"{Fore.GREEN}Crear una nueva tabla{Style.RESET_ALL}",
    "use_table": f"{Fore.GREEN}Utilizar una tabla existente{Style.RESET_ALL}",
    "table_name": f"{Fore.CYAN}Ingrese el nombre de la nueva tabla: {Style.RESET_ALL}",
    "field": f"{Fore.CYAN}Ingrese el nombre del campo (o 'fin' para terminar): {Style.RESET_ALL}",
    "data_type": f"{Fore.CYAN}Ingrese el tipo de dato (TEXT, INTEGER, REAL): {Style.RESET_ALL}",
    "length": f"{Fore.CYAN}Ingrese la longitud del campo (opcional): {Style.RESET_ALL}",
    "list_tables": f"{Fore.CYAN}Tablas existentes:{Style.RESET_ALL}",
    "exit": f"{Fore.RED}Salir{Style.RESET_ALL}",
    "add_field": f"{Fore.GREEN}Agregar campos a la tabla existente{Style.RESET_ALL}"
}

messages_en = {
    "option": f"{Fore.YELLOW}Enter the option: {Style.RESET_ALL}",
    "create_db": f"{Fore.GREEN}Create a new database{Style.RESET_ALL}",
    "use_db": f"{Fore.GREEN}Use an existing database{Style.RESET_ALL}",
    "db_name": f"{Fore.CYAN}Enter the name of the new database: {Style.RESET_ALL}",
    "list_dbs": f"{Fore.CYAN}Existing databases:{Style.RESET_ALL}",
    "create_table": f"{Fore.GREEN}Create a new table{Style.RESET_ALL}",
    "use_table": f"{Fore.GREEN}Use an existing table{Style.RESET_ALL}",
    "table_name": f"{Fore.CYAN}Enter the name of the new table: {Style.RESET_ALL}",
    "field": f"{Fore.CYAN}Enter the field name (or 'done' to finish): {Style.RESET_ALL}",
    "data_type": f"{Fore.CYAN}Enter the data type (TEXT, INTEGER, REAL): {Style.RESET_ALL}",
    "length": f"{Fore.CYAN}Enter the field length (optional): {Style.RESET_ALL}",
    "list_tables": f"{Fore.CYAN}Existing tables:{Style.RESET_ALL}",
    "exit": f"{Fore.RED}Exit{Style.RESET_ALL}",
    "add_field": f"{Fore.GREEN}Add fields to the existing table{Style.RESET_ALL}"
}

# ASCII Art Presentation
welcome_message = f"""
{Fore.CYAN}
 _   _  ___ _   ___ __  __ __ ___   _____ __    __ ____   __ __   __  _     _  _ ___ _   ___ ___ ___  
| | | || __| | / _//__\|  V  | __| |_   _/__\  |  V  \ `v' /' _/ /__\| |   | || | __| | | _,\ __| _ \ 
| 'V' || _|| || \_| \/ | \_/ | _|    | || \/ | | \_/ |`. .'`._`.| \/ | |_  | >< | _|| |_| v_/ _|| v / 
!_/ \_!|___|___\__/\__/|_| |_|___|   |_| \__/  |_| |_| !_! |___/ \_V_\___| |_||_|___|___|_| |___|_|_\ 

Development for Juanses03
{Style.RESET_ALL}
"""

# Select language
print(welcome_message)
print("1. Español")
print("2. English")
try:
    language = int(input(messages_es["option"]))
except ValueError:
    print(f"{Fore.RED}Opción inválida. {Style.RESET_ALL}")
    exit()

if language == 1:
    messages = messages_es
elif language == 2:
    messages = messages_en
else:
    print(f"{Fore.RED}Opción inválida. {Style.RESET_ALL}")
    exit()

try:
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password
    )
    cursor = conn.cursor()
    
    while True:
        # Ask user if they want to create a new database or use an existing one
        print(f"\n1. {messages['create_db']}")
        print(f"2. {messages['use_db']}")
        option = input(messages["option"])
        
        if option == '1':
            # Get the name of the new database
            db_name = input(messages["db_name"])
            try:
                cursor.execute(f"CREATE DATABASE {db_name}")
                conn.database = db_name
                cursor = conn.cursor()
            except mysql.connector.Error as e:
                print(f"{Fore.RED}Error al crear la base de datos: {e}{Style.RESET_ALL}")
        elif option == '2':
            # List existing databases
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            print(messages["list_dbs"])
            for i, database in enumerate(databases):
                print(f"{Fore.YELLOW}{i+1}. {database[0]}{Style.RESET_ALL}")
            try:
                db_index = int(input(messages["option"])) - 1
                if 0 <= db_index < len(databases):
                    db_name = databases[db_index][0]
                    conn.database = db_name
                    cursor = conn.cursor()
                else:
                    print(f"{Fore.RED}Índice de base de datos inválido.{Style.RESET_ALL}")
                    continue
            except (ValueError, IndexError):
                print(f"{Fore.RED}Opción inválida. {Style.RESET_ALL}")
                continue
        
        while True:
            # Ask user if they want to create a new table, use an existing one, or exit
            print(f"\n1. {messages['create_table']}")
            print(f"2. {messages['use_table']}")
            print(f"3. {messages['exit']}")
            option = input(messages["option"])
            
            if option == '1':
                # Get the name of the new table
                table_name = input(messages["table_name"])
                fields = []
                while True:
                    field = input(messages["field"])
                    if field.lower() == 'fin' or field.lower() == 'done':
                        break
                    data_type = input(messages["data_type"])
                    length = input(messages["length"])
                    fields.append((field, data_type, length))
                
                # Create the table
                try:
                    field_definitions = ", ".join([f"{field[0]} {field[1]}({field[2]})" if field[2] else f"{field[0]} {field[1]}" for field in fields])
                    cursor.execute(f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTO_INCREMENT, {field_definitions})")
                    
                    # Show the structure of the created table
                    print(f"\nTable structure for '{table_name}':")
                    cursor.execute(f"DESCRIBE {table_name}")
                    table_description = cursor.fetchall()
                    headers = [i[0] for i in cursor.description]
                    print(tabulate(table_description, headers=headers, tablefmt='grid'))
                except mysql.connector.Error as e:
                    print(f"{Fore.RED}Error al crear la tabla: {e}{Style.RESET_ALL}")
                
            elif option == '2':
                # List existing tables
                cursor.execute("SHOW TABLES")
                tables = cursor.fetchall()
                if tables:
                    print(messages["list_tables"])
                    for i, table in enumerate(tables):
                        print(f"{Fore.YELLOW}{i+1}. {table[0]}{Style.RESET_ALL}")
                    try:
                        table_index = int(input(messages["option"])) - 1
                        if 0 <= table_index < len(tables):
                            table_name = tables[table_index][0]
                            
                            # Show the structure of the selected table
                            print(f"\nTable structure for '{table_name}':")
                            cursor.execute(f"DESCRIBE {table_name}")
                            table_description = cursor.fetchall()
                            headers = [i[0] for i in cursor.description]
                            print(tabulate(table_description, headers=headers, tablefmt='grid'))
                            
                            # Option to add fields to the selected table
                            print(f"\n1. {messages['add_field']}")
                            print(f"2. {messages['exit']}")
                            edit_option = input(messages["option"])
                            
                            if edit_option == '1':
                                while True:
                                    field = input(messages["field"])
                                    if field.lower() == 'fin' or field.lower() == 'done':
                                        break
                                    data_type = input(messages["data_type"])
                                    length = input(messages["length"])
                                    try:
                                        if length:
                                            cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {field} {data_type}({length})")
                                        else:
                                            cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {field} {data_type}")
                                        
                                        # Show the updated structure of the table after each field added
                                        print(f"\nUpdated structure of the table '{table_name}':")
                                        cursor.execute(f"DESCRIBE {table_name}")
                                        table_description = cursor.fetchall()
                                        headers = [i[0] for i in cursor.description]
                                        print(tabulate(table_description, headers=headers, tablefmt='grid'))
                                    except mysql.connector.Error as e:
                                        print(f"{Fore.RED}Error al agregar el campo: {e}{Style.RESET_ALL}")
                        else:
                            print(f"{Fore.RED}Índice de tabla inválido.{Style.RESET_ALL}")
                    except (ValueError, IndexError):
                        print(f"{Fore.RED}Opción inválida. {Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}No hay tablas disponibles.{Style.RESET_ALL}")
                    
            elif option == '3':
                break
        
        # Ask the user if they want to create another database or exit
        print(f"\n1. {messages['create_db']}")
        print(f"2. {messages['exit']}")
        option = input(messages["option"])
        
        if option == '2':
            break
    
except mysql.connector.Error as e:
    print(f"{Fore.RED}Error connecting to the database: {e}{Style.RESET_ALL}")

finally:
    if conn.is_connected():
        conn.close()
        print(f"{Fore.GREEN}Connection closed.{Style.RESET_ALL}")
