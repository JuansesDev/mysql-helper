from config import db_host, db_user, db_password
from db_connection import DatabaseConnection
from ui import UserInterface
from sql_utils import SQLQueryBuilder, ColumnDefinition, SQLIdentifierValidator
from colorama import Fore, Style


class DatabaseManager:
    def __init__(self, ui, db):
        self.ui = ui
        self.db = db
        self.conn, self.cursor = self.db.connect()

    def create_database(self):
        """Create a new database with proper validation"""
        db_name = self.ui.get_valid_identifier(self.ui.messages["db_name"])
        try:
            query = SQLQueryBuilder.create_database(db_name)
            if self.db.execute_query(query):
                self.conn.database = db_name
                self.cursor = self.conn.cursor()
                self.ui.show_message(f"{Fore.GREEN}Database '{db_name}' created successfully.{Style.RESET_ALL}")
        except Exception as e:
            self.ui.show_message(f"{Fore.RED}Error creating the database: {e}{Style.RESET_ALL}")

    def select_database(self):
        """List existing databases and select one to use"""
        if not self.db.execute_query("SHOW DATABASES"):
            return False
        
        databases = self.db.fetchall()
        self.ui.show_message(self.ui.messages["list_dbs"])
        for i, database in enumerate(databases):
            self.ui.show_message(f"{Fore.YELLOW}{i + 1}. {database[0]}{Style.RESET_ALL}")
        
        try:
            db_index = int(self.ui.get_input(self.ui.messages["option"])) - 1
            if 0 <= db_index < len(databases):
                db_name = databases[db_index][0]
                self.conn.database = db_name
                self.cursor = self.conn.cursor()
                return True
            else:
                self.ui.show_message(f"{Fore.RED}Invalid database index.{Style.RESET_ALL}")
                return False
        except (ValueError, IndexError):
            self.ui.show_message(f"{Fore.RED}Invalid option.{Style.RESET_ALL}")
            return False

    def create_table(self):
        """Create a new table with specified fields"""
        table_name = self.ui.get_valid_identifier(self.ui.messages["table_name"])
        columns = []
        
        while True:
            field = self.ui.get_input(self.ui.messages["field"])
            if field.lower() in ["fin", "done"]:
                break
            
            if not SQLIdentifierValidator.is_valid_identifier(field):
                self.ui.show_message(f"{Fore.RED}Invalid field name: {field}{Style.RESET_ALL}")
                continue
            
            data_type = self.ui.get_input(self.ui.messages["data_type"]).upper()
            length = self.ui.get_input(self.ui.messages["length"])
            is_null = self.ui.get_input(self.ui.messages["is_null"]).lower() == "yes"
            default = self.ui.get_input(self.ui.messages["default_value"])
            
            try:
                column = ColumnDefinition(field, data_type, length, is_null, default)
                columns.append(column)
            except ValueError as e:
                self.ui.show_message(f"{Fore.RED}Error in column definition: {e}{Style.RESET_ALL}")

        if columns:
            try:
                query = SQLQueryBuilder.create_table(table_name, columns)
                if self.db.execute_query(query):
                    self.ui.show_message(f"{Fore.GREEN}Table '{table_name}' created successfully.{Style.RESET_ALL}")
            except Exception as e:
                self.ui.show_message(f"{Fore.RED}Error creating table: {e}{Style.RESET_ALL}")

    def use_table(self):
        """Select and work with an existing table"""
        if not self.db.execute_query("SHOW TABLES"):
            return False
        
        tables = self.db.fetchall()
        if not tables:
            self.ui.show_message(f"{Fore.YELLOW}No tables found in the database.{Style.RESET_ALL}")
            return False
        
        self.ui.show_message("Available tables:")
        for i, table in enumerate(tables):
            self.ui.show_message(f"{Fore.YELLOW}{i + 1}. {table[0]}{Style.RESET_ALL}")
        
        try:
            table_index = int(self.ui.get_input(self.ui.messages["option"])) - 1
            if 0 <= table_index < len(tables):
                table_name = tables[table_index][0]
                self._show_table_description(table_name)
                
                # Show fields and modify field option
                fields = self.db.fetchall()
                self.ui.show_message(self.ui.messages["list_fields"])
                for i, field in enumerate(fields):
                    self.ui.show_message(f"{Fore.YELLOW}{i + 1}. {field[0]} - {field[1]}{Style.RESET_ALL}")

                try:
                    field_index = int(self.ui.get_input(self.ui.messages["option"])) - 1
                    if 0 <= field_index < len(fields):
                        old_field = fields[field_index]
                        old_field_name = old_field[0]
                        current_type, current_length = ColumnDefinition.parse_mysql_type(old_field[1])
                        current_null = "YES" if old_field[2] == "YES" else "NO"
                        current_default = old_field[4] if old_field[4] else "NULL"
                        
                        # Get new values
                        new_field_name = self.ui.get_input(
                            self.ui.messages["field_name_change"].format(old_field_name=old_field_name)
                        )
                        if not new_field_name:
                            new_field_name = old_field_name
                        
                        new_data_type = self.ui.get_input(
                            self.ui.messages["data_type_change"].format(current_type=current_type)
                        )
                        if not new_data_type:
                            new_data_type = current_type
                        
                        new_length = self.ui.get_input(
                            self.ui.messages["length_change"].format(current_length=current_length or "N/A")
                        )
                        if not new_length:
                            new_length = current_length
                        
                        new_is_null_input = self.ui.get_input(
                            self.ui.messages["is_null_change"].format(current_null=current_null)
                        )
                        new_is_null = new_is_null_input.lower() == "yes" if new_is_null_input else (current_null == "YES")
                        
                        new_default = self.ui.get_input(
                            self.ui.messages["default_value_change"].format(current_default=current_default)
                        )
                        if not new_default and current_default != "NULL":
                            new_default = current_default if current_default != "NULL" else None

                        # Create new column definition
                        new_column = ColumnDefinition(new_field_name, new_data_type, new_length, new_is_null, new_default)
                        query = SQLQueryBuilder.change_column(table_name, old_field_name, new_column)
                        
                        if self.db.execute_query(query):
                            self._show_table_description(table_name)
                    else:
                        self.ui.show_message(f"{Fore.RED}Invalid field index.{Style.RESET_ALL}")
                except (ValueError, IndexError) as e:
                    self.ui.show_message(f"{Fore.RED}Invalid option or error occurred: {e}{Style.RESET_ALL}")
                
                return True
            else:
                self.ui.show_message(f"{Fore.RED}Invalid table index.{Style.RESET_ALL}")
                return False
        except (ValueError, IndexError):
            self.ui.show_message(f"{Fore.RED}Invalid option.{Style.RESET_ALL}")
            return False

    def delete_table(self, table_name):
        """Delete the specified table with confirmation"""
        if not self.ui.get_confirmation(self.ui.messages["confirm_delete_table"]):
            self.ui.show_message(self.ui.messages["operation_cancelled"])
            return
        
        try:
            query = SQLQueryBuilder.drop_table(table_name)
            if self.db.execute_query(query):
                self.ui.show_message(self.ui.messages["table_deleted"])
        except Exception as e:
            self.ui.show_message(f"{Fore.RED}Error deleting the table: {e}{Style.RESET_ALL}")
    
    def _show_table_description(self, table_name):
        """Helper method to show table description"""
        if self.db.execute_query(f"DESCRIBE `{table_name}`"):
            table_description = self.db.fetchall()
            self.ui.show_table(table_name, table_description)

    def close(self):
        """Close the database connection"""
        self.db.close()


def main():
    ui = UserInterface()
    ui.select_language()
    messages = ui.messages

    db = DatabaseConnection(db_host, db_user, db_password)
    manager = DatabaseManager(ui, db)

    if manager.conn is None:
        return

    try:
        while True:
            ui.display_menu({
                "1": messages["create_db"],
                "2": messages["use_db"],
                "3": messages["exit"],
            })
            option = ui.get_input(messages["option"])

            if option == "1":
                manager.create_database()
            elif option == "2":
                if manager.select_database():
                    while True:
                        ui.display_menu({
                            "1": messages["create_table"],
                            "2": messages["use_table"],
                            "3": messages["exit"],
                        })
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
