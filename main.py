import os
import mysql.connector
import tkinter as tk


def establish_connection():
    return mysql.connector.connect(
        host="MacBook-Pro-von-Oliver.local",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="recipes_db"
    )


class RecipeApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("800x600")  # Set the window size
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

    def open_recipe_window(self, recipe_id):
        recipe_name, recipe_instructions = self.get_recipe_by_id(recipe_id)

        # Clear the window
        for widget in self.window.winfo_children():
            widget.destroy()

        # Update the window title
        self.window.title(recipe_name)

        # Add a back button to return to the recipe list
        back_button = tk.Button(self.window, text="Back", command=self.display_recipes)
        back_button.pack(anchor="nw")

        # Create and pack new widgets
        recipe_name_label = tk.Label(self.window, text=f"Recipe Name: {recipe_name}")
        recipe_name_label.pack()

        instructions_label = tk.Label(self.window, text=f"Instructions:\n{recipe_instructions}")
        instructions_label.pack()

    def display_recipes(self):
        # Clear the window
        for widget in self.window.winfo_children():
            widget.destroy()

        # Update the window title
        self.window.title("Recipicity")

        # Create and pack a label widget with text
        label = tk.Label(self.window, text="All Recipes")
        label.pack()

        # Retrieve and display all recipes
        recipe_list = self.get_all_recipes()
        for recipe_item in recipe_list:
            recipe_id, recipe_name = recipe_item
            recipe_button = tk.Button(self.window, text=f"Recipe ID: {recipe_id}, Recipe Name: {recipe_name}",
                                      command=lambda id_=recipe_id: self.open_recipe_window(id_))
            recipe_button.pack(pady=10)

    def run(self):
        self.display_recipes()
        self.window.mainloop()


if __name__ == "__main__":
    app = RecipeApp()
    app.run()
