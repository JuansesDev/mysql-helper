import mysql.connector
from mysql.connector import Error

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
                password=self.password
            )
            self.cursor = self.conn.cursor()
            return self.conn, self.cursor
        except Error as e:
            print(f"Error connecting to the database: {e}")
            return None, None

    def close(self):
        if self.conn.is_connected():
            self.conn.close()
            print("Connection closed.")
