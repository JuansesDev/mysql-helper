from config import db_host, db_user, db_password
from db_connection import DatabaseConnection
from ui import UserInterface
from colorama import Fore, Style


class DatabaseManager:
    def __init__(self, ui, db):
        self.ui = ui
        self.db = db
        self.conn, self.cursor = self.db.connect()

    def create_database(self):
        # Create a new database
        db_name = self.ui.get_input(self.ui.messages["db_name"])
        try:
            self.cursor.execute(f"CREATE DATABASE {db_name}")
            self.conn.database = db_name
            self.cursor = self.conn.cursor()
        except Exception as e:
            self.ui.show_message(
                f"{Fore.RED}Error creating the database: {e}{Style.RESET_ALL}"
            )

    def select_database(self):
        # List existing databases and select one to use
        self.cursor.execute("SHOW DATABASES")
        databases = self.cursor.fetchall()
        self.ui.show_message(self.ui.messages["list_dbs"])
        for i, database in enumerate(databases):
            self.ui.show_message(
                f"{Fore.YELLOW}{i + 1}. {database[0]}{Style.RESET_ALL}"
            )
        try:
            db_index = int(self.ui.get_input(self.ui.messages["option"])) - 1
            if 0 <= db_index < len(databases):
                db_name = databases[db_index][0]
                self.conn.database = db_name
                self.cursor = self.conn.cursor()
            else:
                self.ui.show_message(
                    f"{Fore.RED}Invalid database index.{Style.RESET_ALL}"
                )
        except (ValueError, IndexError):
            self.ui.show_message(f"{Fore.RED}Invalid option.{Style.RESET_ALL}")

    def create_table(self):
        # Create a new table with specified fields
        table_name = self.ui.get_input(self.ui.messages["table_name"])
        fields = []
        while True:
            field = self.ui.get_input(self.ui.messages["field"])
            if field.lower() in ["fin", "done"]:
                break
            data_type = self.ui.get_input(self.ui.messages["data_type"])
            length = self.ui.get_input(self.ui.messages["length"])
            is_null = self.ui.get_input(self.ui.messages["is_null"]).lower() == "yes"
            default = self.ui.get_input(self.ui.messages["default_value"])

            fields.append((field, data_type, length, is_null, default))

        try:
            field_definitions = ", ".join(
                [
                    f"{field[0]} {field[1]}{f'({field[2]})' if field[2] and field[1].upper() not in ['REAL', 'INTEGER', 'BOOLEAN', 'DATE', 'TEXT', 'BLOB'] else ''}"
                    f"{' NULL' if field[3] else ' NOT NULL'}"
                    f"{f' DEFAULT {field[4]}' if field[4] else ''}"
                    for field in fields
                ]
            )
            self.cursor.execute(
                f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY AUTO_INCREMENT, {field_definitions})"
            )
            self.cursor.execute(f"DESCRIBE {table_name}")
            table_description = self.cursor.fetchall()
            self.ui.show_table(table_name, table_description)
        except Exception as e:
            self.ui.show_message(
                f"{Fore.RED}Error creating the table: {e}{Style.RESET_ALL}"
            )

    def use_table(self):
        # List existing tables and select one to use
        self.cursor.execute("SHOW TABLES")
        tables = self.cursor.fetchall()
        if tables:
            self.ui.show_message(self.ui.messages["list_tables"])
            for i, table in enumerate(tables):
                self.ui.show_message(
                    f"{Fore.YELLOW}{i + 1}. {table[0]}{Style.RESET_ALL}"
                )
            try:
                table_index = int(self.ui.get_input(self.ui.messages["option"])) - 1
                if 0 <= table_index < len(tables):
                    table_name = tables[table_index][0]
                    self.cursor.execute(f"DESCRIBE {table_name}")
                    table_description = self.cursor.fetchall()
                    self.ui.show_table(table_name, table_description)
                    self.manage_table(table_name)
                else:
                    self.ui.show_message(
                        f"{Fore.RED}Invalid table index.{Style.RESET_ALL}"
                    )
            except (ValueError, IndexError):
                self.ui.show_message(f"{Fore.RED}Invalid option.{Style.RESET_ALL}")
        else:
            self.ui.show_message(f"{Fore.RED}No tables available.{Style.RESET_ALL}")

    def manage_table(self, table_name):
        # Show table management options
        self.ui.display_menu(
            {
                "1": self.ui.messages["add_field"],
                "2": self.ui.messages["delete_field"],
                "3": self.ui.messages["edit_field"],  # New option
                "4": self.ui.messages["delete_table"],
                "5": self.ui.messages["exit"],
            }
        )
        option = self.ui.get_input(self.ui.messages["option"])

        if option == "1":
            self.add_field(table_name)
        elif option == "2":
            self.delete_field(table_name)
        elif option == "3":  # New option
            self.edit_field(table_name)
        elif option == "4":
            self.delete_table(table_name)

    def add_field(self, table_name):
        # Add a new field to the specified table
        while True:
            field = self.ui.get_input(self.ui.messages["field"])
            if field.lower() in ["fin", "done"]:
                break
            data_type = self.ui.get_input(self.ui.messages["data_type"])
            length = self.ui.get_input(self.ui.messages["length"])
            is_null = self.ui.get_input(self.ui.messages["is_null"]).lower() == "yes"
            default = self.ui.get_input(self.ui.messages["default_value"])
            try:
                definition = (
                    f"{field} {data_type}"
                    f"{f'({length})' if length and data_type.upper() not in ['REAL', 'INTEGER', 'BOOLEAN', 'DATE', 'TEXT', 'BLOB'] else ''}"
                    f"{' NULL' if is_null else ' NOT NULL'}"
                    f"{f' DEFAULT {default}' if default else ''}"
                )
                self.cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {definition}")
                self.cursor.execute(f"DESCRIBE {table_name}")
                table_description = self.cursor.fetchall()
                self.ui.show_table(table_name, table_description)
            except Exception as e:
                self.ui.show_message(
                    f"{Fore.RED}Error adding the field: {e}{Style.RESET_ALL}"
                )

    def delete_field(self, table_name):
        # Delete a field from the specified table
        while True:
            field = self.ui.get_input(self.ui.messages["field"])
            if field.lower() in ["fin", "done"]:
                break
            try:
                self.cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN {field}")
                self.cursor.execute(f"DESCRIBE {table_name}")
                table_description = self.cursor.fetchall()
                self.ui.show_table(table_name, table_description)
            except Exception as e:
                self.ui.show_message(
                    f"{Fore.RED}Error deleting the field: {e}{Style.RESET_ALL}"
                )

    def edit_field(self, table_name):
        # Edit an existing field in the specified table
        self.cursor.execute(f"DESCRIBE {table_name}")
        fields = self.cursor.fetchall()

        self.ui.show_message(self.ui.messages["list_fields"])
        for i, field in enumerate(fields):
            self.ui.show_message(f"{Fore.YELLOW}{i + 1}. {field[0]}{Style.RESET_ALL}")

        try:
            field_index = int(self.ui.get_input(self.ui.messages["option"])) - 1
            if 0 <= field_index < len(fields):
                old_field_name = fields[field_index][0]
                new_field_name = self.ui.get_input(
                    self.ui.messages["field_name_change"].format(
                        old_field_name=old_field_name
                    )
                )
                if not new_field_name:
                    new_field_name = old_field_name
                new_data_type = self.ui.get_input(
                    self.ui.messages["data_type_change"].format(
                        current_type=fields[field_index][1]
                    )
                )
                new_length = self.ui.get_input(
                    self.ui.messages["length_change"].format(
                        current_length=fields[field_index][1]
                    )
                )
                new_is_null = (
                    self.ui.get_input(
                        self.ui.messages["is_null_change"].format(
                            current_null=fields[field_index][2]
                        )
                    ).lower()
                    == "yes"
                )
                new_default = self.ui.get_input(
                    self.ui.messages["default_value_change"].format(
                        current_default=fields[field_index][4]
                    )
                )

                # Build the ALTER statement
                alter_statement = f"ALTER TABLE {table_name} CHANGE COLUMN {old_field_name} {new_field_name} {new_data_type}"
                if new_length and new_data_type.upper() not in [
                    "REAL",
                    "INTEGER",
                    "BOOLEAN",
                    "DATE",
                    "TEXT",
                    "BLOB",
                ]:
                    alter_statement += f"({new_length})"
                alter_statement += f"{' NULL' if new_is_null else ' NOT NULL'}"
                if new_default:
                    alter_statement += f" DEFAULT {new_default}"

                self.cursor.execute(alter_statement)
                self.cursor.execute(f"DESCRIBE {table_name}")
                table_description = self.cursor.fetchall()
                self.ui.show_table(table_name, table_description)
            else:
                self.ui.show_message(f"{Fore.RED}Invalid field index.{Style.RESET_ALL}")
        except (ValueError, IndexError) as e:
            self.ui.show_message(
                f"{Fore.RED}Invalid option or error occurred: {e}{Style.RESET_ALL}"
            )
        except Exception as e:
            self.ui.show_message(
                f"{Fore.RED}Error editing the field: {e}{Style.RESET_ALL}"
            )

    def delete_table(self, table_name):
        # Delete the specified table
        try:
            self.cursor.execute(f"DROP TABLE {table_name}")
            self.ui.show_message(
                f"{Fore.GREEN}Table {table_name} deleted successfully.{Style.RESET_ALL}"
            )
        except Exception as e:
            self.ui.show_message(
                f"{Fore.RED}Error deleting the table: {e}{Style.RESET_ALL}"
            )

    def close(self):
        # Close the database connection
        self.db.close()


def main():
    # Main function to run the application
    ui = UserInterface()
    ui.select_language()
    messages = ui.messages

    db = DatabaseConnection(db_host, db_user, db_password)
    manager = DatabaseManager(ui, db)

    if manager.conn is None:
        return

    try:
        while True:
            ui.display_menu(
                {
                    "1": messages["create_db"],
                    "2": messages["use_db"],
                    "3": messages["exit"],
                }
            )
            option = ui.get_input(messages["option"])

            if option == "1":
                manager.create_database()
            elif option == "2":
                manager.select_database()
                while True:
                    ui.display_menu(
                        {
                            "1": messages["create_table"],
                            "2": messages["use_table"],
                            "3": messages["exit"],
                        }
                    )
                    option = ui.get_input(messages["option"])
                    if option == "1":
                        manager.create_table()
                    elif option == "2":
                        manager.use_table()
                    elif option == "3":
                        break
            elif option == "3":
                break

    finally:
        manager.close()


if __name__ == "__main__":
    main()
