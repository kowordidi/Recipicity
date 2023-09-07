class Recipe:
    def __init__(self, name, instructions_file, ingredients=None):
        self.name = name
        self.instructions_file = instructions_file
        self.ingredients = ingredients if ingredients else {}

    def get_instructions(self):
        try:
            with open(self.instructions_file, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Instructions not found"

    def set_instructions(self, new_instructions):
        self.instructions = new_instructions

    def get_ingredients(self):
        return self.ingredients

    def add_ingredient(self, new_ingredient, new_amount="1 unit"):
        self.ingredients[new_ingredient] = new_amount

#____________________________________________________________


recipe_name = 'Thunfischnudeln'
file_path = 'dat/Thunfischnudeln'

thunfischnudeln_recipe = Recipe(recipe_name, file_path)

print(thunfischnudeln_recipe.get_instructions())