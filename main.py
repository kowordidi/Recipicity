from database_manager import DatabaseManager
from recipe_gui import RecipeGUI

if __name__ == "__main__":
    db = DatabaseManager()
    gui = RecipeGUI(db)
    gui.run()
