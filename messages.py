from colorama import Fore, Style

# Dictionaries for messages in different languages
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
    "data_type": f"{Fore.CYAN}Ingrese el tipo de dato (TEXT, INTEGER, REAL, DATE, BOOLEAN, BLOB, DECIMAL, CHAR, VARCHAR): {Style.RESET_ALL}",
    "length": f"{Fore.CYAN}Ingrese la longitud del campo (opcional): {Style.RESET_ALL}",
    "list_tables": f"{Fore.CYAN}Tablas existentes:{Style.RESET_ALL}",
    "list_fields": f"{Fore.CYAN}Campos existentes en la tabla:{Style.RESET_ALL}",
    "exit": f"{Fore.RED}Salir{Style.RESET_ALL}",
    "add_field": f"{Fore.GREEN}Agregar campos a la tabla existente{Style.RESET_ALL}",
    "delete_field": f"{Fore.RED}Eliminar campo de la tabla{Style.RESET_ALL}",
    "delete_table": f"{Fore.RED}Eliminar tabla{Style.RESET_ALL}",
    "is_null": f"{Fore.CYAN}¿El campo puede ser NULL? (yes/no): {Style.RESET_ALL}",
    "default_value": f"{Fore.CYAN}Ingrese el valor por defecto (opcional): {Style.RESET_ALL}",
    "edit_field": f"{Fore.GREEN}Editar campo de la tabla{Style.RESET_ALL}",
    "field_name_change": f"{Fore.CYAN}Ingrese el nuevo nombre del campo (actual: {{old_field_name}}): {Style.RESET_ALL}",
    "data_type_change": f"{Fore.CYAN}Ingrese el nuevo tipo de dato (actual: {{current_type}}): {Style.RESET_ALL}",
    "length_change": f"{Fore.CYAN}Ingrese la nueva longitud del campo (actual: {{current_length}}, opcional): {Style.RESET_ALL}",
    "is_null_change": f"{Fore.CYAN}¿El campo puede ser NULL? (actual: {{current_null}}): {Style.RESET_ALL}",
    "default_value_change": f"{Fore.CYAN}Ingrese el nuevo valor por defecto (actual: {{current_default}}, opcional): {Style.RESET_ALL}",
    "confirm_delete_field": "¿Está seguro que desea eliminar este campo?",
    "confirm_delete_table": "¿Está seguro que desea eliminar esta tabla?",
    "operation_cancelled": "Operación cancelada",
    "field_deleted": "Campo eliminado exitosamente",
    "table_deleted": "Tabla eliminada exitosamente",
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
    "data_type": f"{Fore.CYAN}Enter the data type (TEXT, INTEGER, REAL, DATE, BOOLEAN, BLOB, DECIMAL, CHAR, VARCHAR): {Style.RESET_ALL}",
    "length": f"{Fore.CYAN}Enter the field length (optional): {Style.RESET_ALL}",
    "list_tables": f"{Fore.CYAN}Existing tables:{Style.RESET_ALL}",
    "list_fields": f"{Fore.CYAN}Existing fields in the table:{Style.RESET_ALL}",
    "exit": f"{Fore.RED}Exit{Style.RESET_ALL}",
    "add_field": f"{Fore.GREEN}Add fields to the existing table{Style.RESET_ALL}",
    "delete_field": f"{Fore.RED}Delete field from the table{Style.RESET_ALL}",
    "delete_table": f"{Fore.RED}Delete table{Style.RESET_ALL}",
    "is_null": f"{Fore.CYAN}Can the field be NULL? (yes/no): {Style.RESET_ALL}",
    "default_value": f"{Fore.CYAN}Enter the default value (optional): {Style.RESET_ALL}",
    "edit_field": f"{Fore.GREEN}Edit table field{Style.RESET_ALL}",
    "field_name_change": f"{Fore.CYAN}Enter the new field name (current: {{old_field_name}}): {Style.RESET_ALL}",
    "data_type_change": f"{Fore.CYAN}Enter the new data type (current: {{current_type}}): {Style.RESET_ALL}",
    "length_change": f"{Fore.CYAN}Enter the new field length (current: {{current_length}}, optional): {Style.RESET_ALL}",
    "is_null_change": f"{Fore.CYAN}Can the field be NULL? (current: {{current_null}}): {Style.RESET_ALL}",
    "default_value_change": f"{Fore.CYAN}Enter the new default value (current: {{current_default}}, optional): {Style.RESET_ALL}",
    "confirm_delete_field": "Are you sure you want to delete this field?",
    "confirm_delete_table": "Are you sure you want to delete this table?",
    "operation_cancelled": "Operation cancelled",
    "field_deleted": "Field deleted successfully",
    "table_deleted": "Table deleted successfully",
}

messages_fr = {
    "option": f"{Fore.YELLOW}Entrez l'option : {Style.RESET_ALL}",
    "create_db": f"{Fore.GREEN}Créer une nouvelle base de données{Style.RESET_ALL}",
    "use_db": f"{Fore.GREEN}Utiliser une base de données existante{Style.RESET_ALL}",
    "db_name": f"{Fore.CYAN}Entrez le nom de la nouvelle base de données : {Style.RESET_ALL}",
    "list_dbs": f"{Fore.CYAN}Bases de données existantes :{Style.RESET_ALL}",
    "create_table": f"{Fore.GREEN}Créer une nouvelle table{Style.RESET_ALL}",
    "use_table": f"{Fore.GREEN}Utiliser une table existante{Style.RESET_ALL}",
    "table_name": f"{Fore.CYAN}Entrez le nom de la nouvelle table : {Style.RESET_ALL}",
    "field": f"{Fore.CYAN}Entrez le nom du champ (ou 'fin' pour terminer) : {Style.RESET_ALL}",
    "data_type": f"{Fore.CYAN}Entrez le type de données (TEXT, INTEGER, REAL, DATE, BOOLEAN, BLOB, DECIMAL, CHAR, VARCHAR) : {Style.RESET_ALL}",
    "length": f"{Fore.CYAN}Entrez la longueur du champ (optionnelle) : {Style.RESET_ALL}",
    "list_tables": f"{Fore.CYAN}Tables existantes :{Style.RESET_ALL}",
    "list_fields": f"{Fore.CYAN}Champs existants dans la table :{Style.RESET_ALL}",
    "exit": f"{Fore.RED}Quitter{Style.RESET_ALL}",
    "add_field": f"{Fore.GREEN}Ajouter des champs à la table existante{Style.RESET_ALL}",
    "delete_field": f"{Fore.RED}Supprimer le champ de la table{Style.RESET_ALL}",
    "delete_table": f"{Fore.RED}Supprimer la table{Style.RESET_ALL}",
    "is_null": f"{Fore.CYAN}Le champ peut-il être NULL ? (oui/non) : {Style.RESET_ALL}",
    "default_value": f"{Fore.CYAN}Entrez la valeur par défaut (optionnelle) : {Style.RESET_ALL}",
    "edit_field": f"{Fore.GREEN}Modifier le champ de la table{Style.RESET_ALL}",
    "field_name_change": f"{Fore.CYAN}Entrez le nouveau nom du champ (actuel : {{old_field_name}}) : {Style.RESET_ALL}",
    "data_type_change": f"{Fore.CYAN}Entrez le nouveau type de données (actuel : {{current_type}}) : {Style.RESET_ALL}",
    "length_change": f"{Fore.CYAN}Entrez la nouvelle longueur du champ (actuel : {{current_length}}, optionnelle) : {Style.RESET_ALL}",
    "is_null_change": f"{Fore.CYAN}Le champ peut-il être NULL ? (actuel : {{current_null}}) : {Style.RESET_ALL}",
    "default_value_change": f"{Fore.CYAN}Entrez la nouvelle valeur par défaut (actuelle : {{current_default}}, optionnelle) : {Style.RESET_ALL}",
    "confirm_delete_field": "Êtes-vous sûr de vouloir supprimer ce champ ?",
    "confirm_delete_table": "Êtes-vous sûr de vouloir supprimer cette table ?",
    "operation_cancelled": "Opération annulée",
    "field_deleted": "Champ supprimé avec succès",
    "table_deleted": "Table supprimée avec succès",
}

# Constants for language selection
LANGUAGE_SPANISH = 1
LANGUAGE_ENGLISH = 2
LANGUAGE_FRENCH = 3


# Function to get messages based on the selected language
def get_messages(language):
    if language == LANGUAGE_SPANISH:
        return messages_es
    elif language == LANGUAGE_ENGLISH:
        return messages_en
    elif language == LANGUAGE_FRENCH:
        return messages_fr
    else:
        print(f"{Fore.RED}Invalid option. {Style.RESET_ALL}")
        exit()


# Example usage
selected_language = LANGUAGE_FRENCH  # Or LANGUAGE_SPANISH, LANGUAGE_ENGLISH
messages = get_messages(selected_language)
print(messages["option"])
