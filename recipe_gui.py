import tkinter as tk
import functools


class RecipeGUI:
    def __init__(self, db):
        self.window = tk.Tk()
        self.window.geometry("800x600")  # Set the window size
        self.db = db

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def open_recipe_window(self, recipe_id):
        recipe_name, recipe_instructions = self.db.get_recipe_by_id(recipe_id)

        self.clear_window()

        # Update the window title
        self.window.title(recipe_name)

        # Add a back button to return to the recipe list
        back_button = tk.Button(self.window, text="Back", command=self.open_recipe_list_window)
        back_button.pack(anchor="nw")

        # Create and pack new widgets
        recipe_name_label = tk.Label(self.window, text=f"Recipe Name: {recipe_name}")
        recipe_name_label.pack()

        instructions_label = tk.Label(self.window, text=f"Instructions:\n{recipe_instructions}")
        instructions_label.pack()

        # create an edit button
        edit_button = tk.Button(self.window, text="edit",
                                command=functools.partial(self.open_recipe_edit_window, recipe_id))
        edit_button.pack()

    def open_recipe_edit_window(self, recipe_id):
        recipe_name, recipe_instructions = self.db.get_recipe_by_id(recipe_id)

        self.clear_window()

        # Update the window title
        self.window.title("edit " + recipe_name)

        # back button to return to the recipe list
        back_button = tk.Button(self.window, text="Back", command=self.open_recipe_list_window)
        back_button.pack(anchor="nw")

        # Label for name edit
        recipe_name_label = tk.Label(self.window, text="Name")
        recipe_name_label.pack()

        # entry for name edit
        recipe_name_entry = tk.Entry(self.window)
        recipe_name_entry.pack()
        recipe_name_entry.insert(0, recipe_name)
        recipe_name_entry.focus()

        # Label for instructions edit
        recipe_instructions_label = tk.Label(self.window, text="Instructions")
        recipe_instructions_label.pack()

        # text for instructions edit
        recipe_instructions_text = tk.Text(self.window)
        recipe_instructions_text.pack()
        recipe_instructions_text.insert("1.0", recipe_instructions)

        # save button
        def save_button_command(id_to_change, new_name, new_instructions):
            name_query = f"UPDATE recipes SET name = '{new_name}' WHERE id = {id_to_change}"
            self.db.execute_query(name_query)
            instructions_query = f"UPDATE recipes SET instructions = '{new_instructions}' WHERE id = {id_to_change}"
            self.db.execute_query(instructions_query)
            self.open_recipe_window(id_to_change)

        save_button = tk.Button(self.window, text="save",
                                command=lambda: save_button_command(recipe_id,
                                                                    recipe_name_entry.get(),
                                                                    recipe_instructions_text.get("1.0", 'end-1c')))

        save_button.pack()

    def open_recipe_list_window(self):
        print("Opening recipe list window...")
        try:
            self.clear_window()

            # Update the window title
            self.window.title("Recipicity")

            # Create and pack a label widget with text
            label = tk.Label(self.window, text="All Recipes")
            label.pack()

            # Retrieve and display all recipes
            recipe_list = self.db.get_all_recipes()
            for recipe_item in recipe_list:
                recipe_id, recipe_name = recipe_item
                recipe_button = tk.Button(self.window, text=f"Recipe ID: {recipe_id}, Recipe Name: {recipe_name}",
                                          command=functools.partial(self.open_recipe_window, recipe_id))
                recipe_button.pack(pady=10)
        except Exception as e:
            print(f"An error occurred in open_recipe_list_window: {e}")
        print("Recipe list window opened successfully.")

    def run(self):
        print("Running the GUI...")
        try:
            self.open_recipe_list_window()
            self.window.mainloop()
        except Exception as e:
            print(f"An error occurred: {e}")