# MySQL Helper Tool

## Description

The MySQL Helper Tool is a comprehensive command-line utility for managing MySQL databases. It provides robust options to create and manage databases, tables, and table fields with advanced validation and safety features. Users can interact with the tool in Spanish, English, or French with a user-friendly interface.

## Features

- **Multi-language Support**: Interface available in Spanish, English, and French
- **Database Management**: Create new databases and connect to existing ones
- **Table Management**: Create, view, and delete tables with proper validation
- **Field Management**: 
  - Add new fields to tables with full type specification
  - Edit existing field properties (name, type, length, null constraints, default values)
  - Delete fields from tables
  - View detailed table structure
- **SQL Safety**: Built-in SQL injection protection with identifier validation
- **Error Handling**: Comprehensive error handling with colored output
- **Type Validation**: Support for all MySQL data types with proper length validation

## Requirements

Ensure you have Python 3.6 or higher installed. The tool requires the following Python libraries:

- `mysql-connector-python` - For MySQL database connectivity
- `python-dotenv` - For environment variable management
- `colorama` - For colored terminal output
- `tabulate` - For formatted table display

## Installation

1. **Clone the repository**:
   
   ```bash
   git clone https://github.com/JuansesDev/mysql-helper
   cd mysql-helper
   ```

2. **Create a virtual environment** (optional but recommended):
   
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   
   - On Windows:
     
     ```bash
     venv\Scripts\activate
     ```
   
   - On macOS/Linux:
     
     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies**:
   
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure environment variables**:
   
    Copy the example file `.env.example` to a new file named `.env` and configure the variables with your database settings:
   
   ```bash
   cp .env.example .env
   ```
   
    Edit the `.env` file with your database credentials:
   
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=1234
   ```

## Usage

1. **Run the script**:
   
   ```bash
   python main.py
   ```

2. **Select the language**:
   
    When running the script, you'll be prompted to select the language for the interface. Enter `1` for Spanish, `2` for English, or `3` for French.

3. **Manage databases**:
   
   - **Create a new database**: Choose the option to create a new database and enter its name with automatic validation
   - **Use an existing database**: List available databases and select the one you wish to use

4. **Manage tables**:
   
   - **Create a new table**: Specify the table name and define its fields with proper data types, lengths, null constraints, and default values
   - **Use an existing table**: List existing tables and select one to view its structure and manage its fields

5. **Manage table fields**:
   
   - **View table structure**: See all fields with their properties in a formatted table
   - **Edit field properties**: Modify field names, data types, lengths, null constraints, and default values
   - **Add new fields**: Define new fields with full type specification
   - **Delete fields**: Remove fields from tables with confirmation

6. **Exit**:
   
    Select the exit option to terminate the program safely.

## Supported Data Types

The tool supports all standard MySQL data types including:

- **Numeric**: INTEGER, REAL, DECIMAL, FLOAT, DOUBLE, BIGINT, SMALLINT, TINYINT
- **String**: VARCHAR, CHAR, TEXT, LONGTEXT, MEDIUMTEXT, TINYTEXT
- **Date/Time**: DATE, TIME, DATETIME, TIMESTAMP, YEAR
- **Binary**: BLOB, LONGBLOB, MEDIUMBLOB, TINYBLOB, BINARY, VARBINARY
- **Other**: BOOLEAN, JSON, ENUM, SET

## Security Features

- **SQL Injection Protection**: All identifiers are properly escaped and validated
- **Input Validation**: Comprehensive validation for database, table, and field names
- **Safe Query Building**: Parameterized queries and identifier escaping
- **Error Handling**: Graceful error handling with informative messages

## Example `.env` File

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=1234
```

## Project Structure

```
mysql-helper/
├── main.py              # Main application entry point
├── config.py            # Configuration and environment variables
├── db_connection.py     # Database connection management
├── ui.py               # User interface and multilingual support
├── sql_utils.py        # SQL query building and validation utilities
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── readme.md          # This file
└── CHANGELOG.md       # Version history and changes
```

## Future Improvements

This tool continues to evolve with planned features including:

- **Data Management**: Insert, update, and delete table records
- **Import/Export**: Support for SQL file import/export
- **Backup/Restore**: Database backup and restoration utilities
- **Advanced Queries**: Query builder for complex SELECT statements
- **Graphical Interface**: Optional GUI version
- **Performance Tools**: Query optimization and performance monitoring

## Contributing

Contributions are welcome! Please feel free to submit pull requests, report bugs, or suggest new features through the GitHub repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or issues, please open an issue on the [GitHub repository](https://github.com/JuansesDev/mysql-helper).

## Changelog

For a detailed list of changes and version history, see [CHANGELOG.md](CHANGELOG.md).