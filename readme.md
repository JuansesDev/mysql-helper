# MySQL Helper Tool

## Description

The MySQL Helper Tool is a command-line utility for managing MySQL databases. It provides options to create new databases and tables, use existing databases and tables, and add fields to tables. Users can interact with the tool in either Spanish or English.

## Requirements

Ensure you have Python 3.6 or higher installed. The tool also requires the following Python libraries, which can be installed via the `requirements.txt` file.

## Installation

1. **Clone the repository**:
   
   ```bash
   git clone https://github.com/Juanses03/mysql-helper
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
   python helper.py
   ```

2. **Select the language**:
   
    When running the script, you'll be prompted to select the language for the interface. Enter `1` for Spanish or `2` for English.

3. **Manage the database**:
   
   - **Create a new database**: Choose the option to create a new database and enter its name.
   - **Use an existing database**: List available databases and select the one you wish to use.
   - **Create a new table**: Specify the table name and define its fields.
   - **Use an existing table**: List existing tables and select one. You can also add new fields to the selected table.

4. **Exit**:
   
    Select the exit option to terminate the program.

## Example `.env` File

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=1234
```

## Future Improvements

This tool is a work in progress and will continue to be improved with additional features, such as:

- Enhanced error handling and validation
- Support for more complex data types and constraints
- User-friendly features for managing table records
- Graphical interface options

Contributions and feature suggestions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or issues, please open an issue on the [GitHub repository](https://github.com/Juanses03/mysql-helper).

## Notes

Feel free to customize any section to better fit your needs or add any additional details that may be relevant.

License
This project is licensed under the MIT License. See the LICENSE file for details.