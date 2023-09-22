import os, mysql.connector

def establish_connection():
    return mysql.connector.connect(
        host="MacBook-Pro-von-Oliver.local",
        user="root",
        password="huhky8-jarbun-noxxeH",
        database="recipes_db")
def print_recipes():
    mydb = establish_connection()
    # Create a cursor object to execute SQL queries
    cursor = mydb.cursor()
    # Execute the SELECT query
    cursor.execute("SELECT id, name FROM recipes")
    # Fetch all rows from the result set
    rows = cursor.fetchall()
    # Print the recipe names and IDs
    for row in rows:
        recipe_id, recipe_name = row
        print("Recipe ID:", recipe_id)
        print("Recipe Name:", recipe_name)
        print()
    # Close the cursor and connection
    cursor.close()
    mydb.close()

#____________________________________________________________

print_recipes()