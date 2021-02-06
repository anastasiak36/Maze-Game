from character_selection import Character_Selection, ImageList, Image_object
from Goal1_Anastasia import MyGame

class Maze_Manager(object):
    def __init__(self):
        self.root = tk.Tk()
        self.current_screen = None
        self.image_list = None
        self.player = None

    def setup_character_selection(self):
        self.root.title("Select Your Character!")
        self.image_list = ImageList("image_adress.txt")
        self.current_screen = Character_Selection(
                                                master = self.root, 
                                                image_list= self.image_list, 
                                                callback_on_selected = self.onclose_character_selection)