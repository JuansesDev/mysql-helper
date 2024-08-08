from colorama import Fore, Style

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
    "add_field": f"{Fore.GREEN}Agregar campos a la tabla existente{Style.RESET_ALL}",
    "delete_field": f"{Fore.RED}Eliminar campo de la tabla{Style.RESET_ALL}",
    "delete_table": f"{Fore.RED}Eliminar tabla{Style.RESET_ALL}"
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
    "add_field": f"{Fore.GREEN}Add fields to the existing table{Style.RESET_ALL}",
    "delete_field": f"{Fore.RED}Delete field from the table{Style.RESET_ALL}",
    "delete_table": f"{Fore.RED}Delete table{Style.RESET_ALL}"
}

def get_messages(language):
    if language == 1:
        return messages_es
    elif language == 2:
        return messages_en
    else:
        print(f"{Fore.RED}Opción inválida. {Style.RESET_ALL}")
        exit()
