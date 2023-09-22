import mysql.connector
import tkinter as tk


def establish_connection():
    return mysql.connector.connect(
        host="MacBook-Pro-von-Oliver.local",
        user="root",
        password="huhky8-jarbun-noxxeH",
        database="recipes_db"
    )


def execute_query(query):
    mydb = establish_connection()
    cursor = mydb.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    mydb.commit()
    mydb.close()
    return rows


def print_recipes():
    query = "SELECT id, name FROM recipes"
    rows = execute_query(query)
    for row in rows:
        recipe_id, recipe_name = row
        print("Recipe ID:", recipe_id)
        print("Recipe Name:", recipe_name)


def create_recipe(recipe_name, recipe_instructions):
    query = f"INSERT INTO recipes (name, instructions) VALUES ('{recipe_name}', '{recipe_instructions}')"
    execute_query(query)
    last_insert_id_query = "SELECT LAST_INSERT_ID()"
    last_insert_id = execute_query(last_insert_id_query)[0][0]
    print("Recipe created successfully!")


# Create a new Tkinter window


window = tk.Tk()
window.geometry("800x600")  # Set the window size
window.title("Recipicity")

# Create and pack a label widget with text
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

textbox = tk.Text(window)
textbox.pack()
# Start the Tkinter event loop
window.mainloop()

