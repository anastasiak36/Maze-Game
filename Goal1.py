import arcade

#constant variables
screen_width = 1000
screen_height = 700
screen_title = "Maze Game"
character_scale = 0.25
class MyGame(arcade.Window):
    
    def __init__(self):
        
        super().__init__(screen_width, screen_height, screen_title)

        arcade.set_background_color(arcade.color.AZURE_MIST)
        # create the list to keep the character in
        self.player_list = arcade.SpriteList()

        # create separate variable that will hold the sprite
        self.player_sprite = None
    
    def setup(self):
        # create player sprite and store it in the variables
        self.player_sprite = arcade.Sprite("Maze-Game/images/blue.png", character_scale)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        # make grid for maze
        
    def on_draw(self):
        arcade.start_render()

        #draw the sprites 
        self.player_list.draw()

def main():
    window = MyGame()
    window.setup()
    window.on_draw()
    arcade.run()

if __name__ == "__main__":
    main()