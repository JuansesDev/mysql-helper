import mysql.connector
from mysql.connector import Error, ProgrammingError, IntegrityError, DatabaseError
from colorama import Fore, Style


class DatabaseConnection:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                autocommit=True  # Enable autocommit for DDL operations
            )
            self.cursor = self.conn.cursor()
            return self.conn, self.cursor
        except Error as e:
            print(f"{Fore.RED}Error connecting to the database: {e}{Style.RESET_ALL}")
            return None, None
    
    def execute_query(self, query, params=None):
        """Execute query with proper error handling"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return True
        except ProgrammingError as e:
            print(f"{Fore.RED}SQL Programming Error: {e}{Style.RESET_ALL}")
            return False
        except IntegrityError as e:
            print(f"{Fore.RED}Integrity Error: {e}{Style.RESET_ALL}")
            return False
        except DatabaseError as e:
            print(f"{Fore.RED}Database Error: {e}{Style.RESET_ALL}")
            return False
        except Error as e:
            print(f"{Fore.RED}MySQL Error: {e}{Style.RESET_ALL}")
            return False
    
    def fetchall(self):
        """Safely fetch all results"""
        try:
            return self.cursor.fetchall()
        except Error as e:
            print(f"{Fore.RED}Error fetching results: {e}{Style.RESET_ALL}")
            return []

    def close(self):
        if self.conn and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print(f"{Fore.GREEN}Connection closed.{Style.RESET_ALL}")
