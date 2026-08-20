import mysql.connector
import time

def get_connection():

    while True:
        try:
            connection = mysql.connector.connect(
                host="db",
                user="root",
                password="root",
                database="devops"
            )

            return connection

        except Exception:
            print("Waiting for MySQL...")
            time.sleep(5)
