import tkinter as tk
import functools

recipe_button_size = 10


class RecipeGUI:
    def __init__(self, db):
        self.root = tk.Tk()
        self.root.geometry("800x600")  # Set the window size
        self.db = db

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_back_button(self, command):
        back_button = tk.Button(self.root, text="Back", command=command)
        back_button.grid()

    def create_label(self, text):
        label = tk.Label(self.root, text=text)
        label.grid()

    def create_entry(self, default_text):
        entry = tk.Entry(self.root)
        entry.grid()
        entry.insert(0, default_text)
        entry.focus()
        return entry

    def create_text(self, default_text):
        text = tk.Text(self.root)
        text.grid()
        text.insert("1.0", default_text)
        return text

    def open_recipe_window(self, recipe_id):
        recipe_name, recipe_instructions = self.db.get_recipe_by_id(recipe_id)
        self.clear_window()
        self.root.title(recipe_name)
        self.create_back_button(self.open_recipe_list_window)

        self.create_label(recipe_name)
        self.create_label(recipe_instructions)

        # create an edit button
        edit_button = tk.Button(self.root,
                                text="edit",
                                command=functools.partial(self.open_recipe_edit_window, recipe_id))
        edit_button.grid()

    def open_recipe_edit_window(self, recipe_id):
        recipe_name, recipe_instructions = self.db.get_recipe_by_id(recipe_id)
        self.clear_window()
        self.create_back_button(functools.partial(self.open_recipe_window, recipe_id))
        self.root.title("edit " + recipe_name)

        self.create_label("Name")
        name_entry = self.create_entry(recipe_name)

        self.create_label("Instructions")
        instructions_text = self.create_text(recipe_instructions)

        # save button
        def save_button_command(id_to_change):
            new_name = name_entry.get()
            new_instructions = instructions_text.get("1.0", 'end-1c')

            query = "UPDATE recipes SET name = %s, instructions = %s WHERE id = %s"
            params = (new_name, new_instructions, id_to_change)

            self.db.execute_query(query, params)

            self.open_recipe_window(id_to_change)

        save_button = tk.Button(self.root, text="save", command=lambda: save_button_command(recipe_id))
        save_button.grid()

    def open_recipe_list_window(self):
        print("Opening recipe list window...")
        try:
            self.clear_window()
            self.root.title("Recipicity")

            self.root.columnconfigure(0, weight=1)
            self.root.columnconfigure(1, weight=1)
            self.root.columnconfigure(2, weight=1)
            self.root.columnconfigure(3, weight=1)

            # Retrieve and display all recipes
            recipe_list = self.db.get_all_recipes()
            row = 0
            column = 0
            for recipe_item in recipe_list:
                recipe_id, recipe_name = recipe_item
                recipe_button = tk.Button(self.root,
                                          text=recipe_name,
                                          command=functools.partial(self.open_recipe_window, recipe_id))
                recipe_button.grid(row=row, column=column, padx=5, pady=20, sticky="nsew")
                column += 1
                if column > 3:
                    column = 0
                    row += 1
        except Exception as e:
            print(f"An error occurred in open_recipe_list_window: {e}")
        print("Recipe list window opened successfully.")

    def run(self):
        print(self.db.execute_query("SELECT* FROM recipes"))
        print("Running the GUI...")
        try:
            self.open_recipe_list_window()
            self.root.mainloop()
        except Exception as e:
            print(f"An error occurred: {e}")
