class Recipe:
    def __init__(self, name, instructions, ingredients=None):
        self.name = name
        self.ingredients = ingredients if ingredients else {}
        self.instructions = f'dat/{name}.txt'  # Create the file path

        # Create the instructions file and write the instructions to it
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

#____________________________________________________________





