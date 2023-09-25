import os
import mysql.connector


def establish_connection():
    return mysql.connector.connect(
        host="MacBook-Pro-von-Oliver.local",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="recipes_db"
    )


class DatabaseManager:
    def __init__(self):
        self.mydb = establish_connection()

    def execute_query(self, query):
        cursor = self.mydb.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        self.mydb.commit()
        return rows

    def get_all_recipes(self):
        query = "SELECT id, name FROM recipes"
        return self.execute_query(query)

    def get_recipe_by_id(self, get_id):
        query = f"SELECT name, instructions FROM recipes WHERE id = {get_id}"
        return self.execute_query(query)[0]

