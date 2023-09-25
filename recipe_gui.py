import tkinter as tk
import functools

recipe_button_size = 10
class RecipeGUI:
    def __init__(self, db):
        self.window = tk.Tk()
        self.window.geometry("800x600")  # Set the window size
        self.db = db

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def create_back_button(self, command):
        back_button = tk.Button(self.window, text="Back", command=command)
        back_button.pack(anchor="nw")

    def create_label(self, text):
        label = tk.Label(self.window, text=text)
        label.pack()

    def create_entry(self, default_text):
        entry = tk.Entry(self.window)
        entry.pack()
        entry.insert(0, default_text)
        entry.focus()
        return entry

    def create_text(self, default_text):
        text = tk.Text(self.window)
        text.pack()
        text.insert("1.0", default_text)
        return text

    def open_recipe_window(self, recipe_id):
        recipe_name, recipe_instructions = self.db.get_recipe_by_id(recipe_id)
        self.clear_window()
        self.window.title(recipe_name)
        self.create_back_button(self.open_recipe_list_window)

        self.create_label(recipe_name)
        self.create_label(recipe_instructions)

        # create an edit button
        edit_button = tk.Button(self.window,
                                text="edit",
                                command=functools.partial(self.open_recipe_edit_window, recipe_id))
        edit_button.pack()

    def open_recipe_edit_window(self, recipe_id):
        recipe_name, recipe_instructions = self.db.get_recipe_by_id(recipe_id)
        self.clear_window()
        self.create_back_button(functools.partial(self.open_recipe_window, recipe_id))
        self.window.title("edit " + recipe_name)

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

        save_button = tk.Button(self.window, text="save", command=lambda: save_button_command(recipe_id))
        save_button.pack()

    def open_recipe_list_window(self):
        print("Opening recipe list window...")
        try:
            self.clear_window()
            self.window.title("Recipicity")
            self.create_label("All recipes")

            # Retrieve and display all recipes
            recipe_list = self.db.get_all_recipes()
            for recipe_item in recipe_list:
                recipe_id, recipe_name = recipe_item
                recipe_button = tk.Button(self.window,
                                          text=recipe_name,
                                          height=recipe_button_size,
                                          width=recipe_button_size,
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
