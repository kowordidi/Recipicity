import os
import mysql.connector


def establish_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="recipicity_db"
        )
    except mysql.connector.Error as error:
        print(f"Error establishing database connection: {error}")
        return None


class DatabaseManager:
    def __init__(self):
        self.connection = establish_connection()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def execute_query(self, query, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            rows = cursor.fetchall()
            self.connection.commit()
            return rows

    def get_all_recipes(self):
        query = "SELECT id, name FROM recipes"
        return self.execute_query(query)

    def get_recipe_by_id(self, recipe_id):
        query = "SELECT name, instructions FROM recipes WHERE id = %s"
        params = (recipe_id,)
        result = self.execute_query(query, params)
        if result:
            return result[0]
        else:
            raise ValueError(f"No recipe found with ID {recipe_id}")
