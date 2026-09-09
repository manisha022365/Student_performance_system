import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="manisha@22",
        database="student_performance",
        use_pure=True
    )