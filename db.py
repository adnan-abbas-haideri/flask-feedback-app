import mysql.connector
import os
import time

def get_connection():

    while True:
        try:
            connection = mysql.connector.connect(
                host=os.getenv("MYSQL_HOST", "db"),
                port=int(os.getenv("MYSQL_PORT", "3306")),
                user=os.getenv("MYSQL_USER", "root"),
                password=os.getenv("MYSQL_PASSWORD", "root"),
                database=os.getenv("MYSQL_DATABASE", "devops")
            )

            return connection

        except Exception:
            print("Waiting for MySQL...")
            time.sleep(5)
