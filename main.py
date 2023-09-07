class Recipe:
    def __init__(self, name, instructions_file, ingredients):
        self.name = name
        self.instructions_file = instructions_file
        self.ingredients = ingredients

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
        self.instructions[new_ingredient] = new_amount

