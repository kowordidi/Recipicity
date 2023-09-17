import os
class Recipe:
    def __init__(self, name, instructions, ingredients=None):
        self.name = name
        self.ingredients = ingredients if ingredients else {}
        self.instructions = f'dat/{name}.txt'  # Create the file path

        # Create the instructions file and write the instructions to it
        if not os.path.exists(self.instructions):
            with open(self.instructions, 'w') as file:
                file.write(instructions)

    def get_instructions(self):
        try:
            with open(self.instructions, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Instructions not found"

    def set_instructions(self, new_instructions):
        self.instructions = new_instructions

    def get_ingredients(self):
        return self.ingredients

    def add_ingredient(self, new_ingredient, new_amount="1 unit"):
        self.ingredients[new_ingredient] = new_amount

    def __str__(self):
        return (f"Name: {self.name} \n"
                f"Instructions: {self.get_instructions()}\n")


#____________________________________________________________

recipe1 = Recipe("Spaghetti", "Boil spaghetti in water.")
recipe2 = Recipe("Salad", "Chop vegetables and mix with dressing.")

print(recipe1)  # This will print: Recipe: Spaghetti
print(recipe2)  # This will print: Recipe: Salad