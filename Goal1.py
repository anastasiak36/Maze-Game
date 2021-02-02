import arcade

screen_width = 1000
screen_height = 700
screen_title = "Maze Game"
class MyGame(arcade.Window):
    
    def __init__(self):
        
        super().__init__(screen_width, screen_height, screen_title)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        # create the list to keep the character in
        self.player_list = arcade.SpriteList()

        # create separate variable that will hold the sprite
        self.player_sprite = None
    
    def setup(self):
        # create player sprite and store it in the variables
        self.player_sprite = arcade.Sprite("blue.PNG")
        # make grid for maze
        
    def draw(self):
        arcade.start_render()

        #draw the sprites 
        self.player_list.draw()

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()