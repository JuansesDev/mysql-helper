import re
from mysql.connector import Error
from colorama import Fore, Style


class SQLIdentifierValidator:
    """Validates SQL identifiers (database, table, column names)"""
    
    @staticmethod
    def is_valid_identifier(name):
        """Validate if a name is a valid MySQL identifier"""
        if not name or len(name) > 64:
            return False
        # MySQL identifier pattern: starts with letter/underscore, contains alphanumeric/underscore
        pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
        return bool(re.match(pattern, name))
    
    @staticmethod
    def escape_identifier(name):
        """Escape identifier with backticks for safe SQL usage"""
        if not SQLIdentifierValidator.is_valid_identifier(name):
            raise ValueError(f"Invalid identifier: {name}")
        return f"`{name}`"


class ColumnDefinition:
    """Handles MySQL column definition creation"""
    
    TYPES_WITHOUT_LENGTH = {'REAL', 'INTEGER', 'BOOLEAN', 'DATE', 'TEXT', 'BLOB'}
    
    def __init__(self, name, data_type, length=None, nullable=True, default=None):
        self.name = name
        self.data_type = data_type.upper()
        self.length = length
        self.nullable = nullable
        self.default = default
    
    def build_definition(self, include_name=True):
        """Build the complete column definition"""
        definition_parts = []
        
        if include_name:
            definition_parts.append(SQLIdentifierValidator.escape_identifier(self.name))
        
        # Data type with optional length
        if self.length and self.data_type not in self.TYPES_WITHOUT_LENGTH:
            definition_parts.append(f"{self.data_type}({self.length})")
        else:
            definition_parts.append(self.data_type)
        
        # NULL constraint
        definition_parts.append("NULL" if self.nullable else "NOT NULL")
        
        # Default value
        if self.default:
            if self.data_type in {'VARCHAR', 'CHAR', 'TEXT'}:
                definition_parts.append(f"DEFAULT '{self.default}'")
            else:
                definition_parts.append(f"DEFAULT {self.default}")
        
        return " ".join(definition_parts)
    
    @staticmethod
    def parse_mysql_type(type_string):
        """Parse MySQL type string like 'varchar(50)' into type and length"""
        match = re.match(r'^(\w+)(?:\((\d+)\))?', type_string.lower())
        if match:
            data_type = match.group(1).upper()
            length = match.group(2) if match.group(2) else None
            return data_type, length
        return type_string.upper(), None


class SQLQueryBuilder:
    """Builds safe SQL queries with proper identifier escaping"""
    
    @staticmethod
    def create_database(db_name):
        """Build CREATE DATABASE query"""
        return f"CREATE DATABASE {SQLIdentifierValidator.escape_identifier(db_name)}"
    
    @staticmethod
    def create_table(table_name, columns):
        """Build CREATE TABLE query"""
        escaped_table = SQLIdentifierValidator.escape_identifier(table_name)
        column_defs = [col.build_definition() for col in columns]
        all_columns = f"`id` INTEGER PRIMARY KEY AUTO_INCREMENT, {', '.join(column_defs)}"
        return f"CREATE TABLE {escaped_table} ({all_columns})"
    
    @staticmethod
    def add_column(table_name, column):
        """Build ALTER TABLE ADD COLUMN query"""
        escaped_table = SQLIdentifierValidator.escape_identifier(table_name)
        return f"ALTER TABLE {escaped_table} ADD COLUMN {column.build_definition()}"
    
    @staticmethod
    def drop_column(table_name, column_name):
        """Build ALTER TABLE DROP COLUMN query"""
        escaped_table = SQLIdentifierValidator.escape_identifier(table_name)
        escaped_column = SQLIdentifierValidator.escape_identifier(column_name)
        return f"ALTER TABLE {escaped_table} DROP COLUMN {escaped_column}"
    
    @staticmethod
    def change_column(table_name, old_name, new_column):
        """Build ALTER TABLE CHANGE COLUMN query"""
        escaped_table = SQLIdentifierValidator.escape_identifier(table_name)
        escaped_old_name = SQLIdentifierValidator.escape_identifier(old_name)
        return f"ALTER TABLE {escaped_table} CHANGE COLUMN {escaped_old_name} {new_column.build_definition()}"
    
    @staticmethod
    def drop_table(table_name):
        """Build DROP TABLE query"""
        escaped_table = SQLIdentifierValidator.escape_identifier(table_name)
        return f"DROP TABLE {escaped_table}"
