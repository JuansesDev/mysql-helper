from config import db_host, db_user, db_password
from db_connection import DatabaseConnection
from ui import UserInterface
from colorama import Fore, Style

def main():
    ui = UserInterface()
    ui.select_language()
    messages = ui.messages

    db = DatabaseConnection(db_host, db_user, db_password)
    conn, cursor = db.connect()

    if conn is None:
        return

    try:
        while True:
            ui.display_menu({
                "1": messages["create_db"],
                "2": messages["use_db"]
            })
            option = ui.get_input(messages["option"])

            if option == '1':
                db_name = ui.get_input(messages["db_name"])
                try:
                    cursor.execute(f"CREATE DATABASE {db_name}")
                    conn.database = db_name
                    cursor = conn.cursor()
                except Exception as e:
                    ui.show_message(f"{Fore.RED}Error creating the database: {e}{Style.RESET_ALL}")

            elif option == '2':
                cursor.execute("SHOW DATABASES")
                databases = cursor.fetchall()
                ui.show_message(messages["list_dbs"])
                for i, database in enumerate(databases):
                    ui.show_message(f"{Fore.YELLOW}{i+1}. {database[0]}{Style.RESET_ALL}")
                try:
                    db_index = int(ui.get_input(messages["option"])) - 1
                    if 0 <= db_index < len(databases):
                        db_name = databases[db_index][0]
                        conn.database = db_name
                        cursor = conn.cursor()
                    else:
                        ui.show_message(f"{Fore.RED}Invalid database index.{Style.RESET_ALL}")
                        continue
                except (ValueError, IndexError):
                    ui.show_message(f"{Fore.RED}Invalid option. {Style.RESET_ALL}")
                    continue

            while True:
                ui.display_menu({
                    "1": messages["create_table"],
                    "2": messages["use_table"],
                    "3": messages["exit"]
                })
                option = ui.get_input(messages["option"])

                if option == '1':
                    table_name = ui.get_input(messages["table_name"])
                    fields = []
                    while True:
                        field = ui.get_input(messages["field"])
                        if field.lower() in ['fin', 'done']:
                            break
                        data_type = ui.get_input(messages["data_type"])
                        length = ui.get_input(messages["length"])
                        fields.append((field, data_type, length))

                    try:
                        field_definitions = ", ".join([f"{field[0]} {field[1]}({field[2]})" if field[2] else f"{field[0]} {field[1]}" for field in fields])
                        cursor.execute(f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTO_INCREMENT, {field_definitions})")
                        cursor.execute(f"DESCRIBE {table_name}")
                        table_description = cursor.fetchall()
                        ui.show_table(table_name, table_description)
                    except Exception as e:
                        ui.show_message(f"{Fore.RED}Error creating the table: {e}{Style.RESET_ALL}")

                elif option == '2':
                    cursor.execute("SHOW TABLES")
                    tables = cursor.fetchall()
                    if tables:
                        ui.show_message(messages["list_tables"])
                        for i, table in enumerate(tables):
                            ui.show_message(f"{Fore.YELLOW}{i+1}. {table[0]}{Style.RESET_ALL}")
                        try:
                            table_index = int(ui.get_input(messages["option"])) - 1
                            if 0 <= table_index < len(tables):
                                table_name = tables[table_index][0]
                                cursor.execute(f"DESCRIBE {table_name}")
                                table_description = cursor.fetchall()
                                ui.show_table(table_name, table_description)

                                ui.display_menu({
                                    "1": messages["add_field"],
                                    "2": messages["delete_field"],
                                    "3": messages["delete_table"],
                                    "4": messages["exit"]
                                })
                                edit_option = ui.get_input(messages["option"])

                                if edit_option == '1':
                                    while True:
                                        field = ui.get_input(messages["field"])
                                        if field.lower() in ['fin', 'done']:
                                            break
                                        data_type = ui.get_input(messages["data_type"])
                                        length = ui.get_input(messages["length"])
                                        try:
                                            if length:
                                                cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {field} {data_type}({length})")
                                            else:
                                                cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {field} {data_type}")
                                            cursor.execute(f"DESCRIBE {table_name}")
                                            table_description = cursor.fetchall()
                                            ui.show_table(table_name, table_description)
                                        except Exception as e:
                                            ui.show_message(f"{Fore.RED}Error adding the field: {e}{Style.RESET_ALL}")

                                elif edit_option == '2':
                                    while True:
                                        field = ui.get_input(messages["field"])
                                        if field.lower() in ['fin', 'done']:
                                            break
                                        try:
                                            cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN {field}")
                                            cursor.execute(f"DESCRIBE {table_name}")
                                            table_description = cursor.fetchall()
                                            ui.show_table(table_name, table_description)
                                        except Exception as e:
                                            ui.show_message(f"{Fore.RED}Error deleting the field: {e}{Style.RESET_ALL}")

                                elif edit_option == '3':
                                    try:
                                        cursor.execute(f"DROP TABLE {table_name}")
                                        ui.show_message(f"{Fore.GREEN}Table {table_name} deleted successfully.{Style.RESET_ALL}")
                                        break
                                    except Exception as e:
                                        ui.show_message(f"{Fore.RED}Error deleting the table: {e}{Style.RESET_ALL}")

                            else:
                                ui.show_message(f"{Fore.RED}Invalid table index.{Style.RESET_ALL}")
                        except (ValueError, IndexError):
                            ui.show_message(f"{Fore.RED}Invalid option. {Style.RESET_ALL}")
                    else:
                        ui.show_message(f"{Fore.RED}No tables available.{Style.RESET_ALL}")

                elif option == '3':
                    break

            ui.display_menu({
                "1": messages["create_db"],
                "2": messages["exit"]
            })
            option = ui.get_input(messages["option"])

            if option == '2':
                break

    finally:
        db.close()

if __name__ == "__main__":
    main()
