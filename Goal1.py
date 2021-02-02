import arcade

screen_width = 1000
screen_height = 700
screen_title = "Maze Game"
class MyGame(arcade.Window):
    
    def __init__(self):
        
        super().__init__(screen_width, screen_height, screen_title)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        # create the list to keep the character in
        self.player_list = None

        # create separate variable that will hold the sprite
        self.player_sprite
    
    def setup(self):
        # make grid for maze
        pass

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()