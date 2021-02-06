import arcade

#constant variables
screen_width = 1000
screen_height = 700
screen_title = "Maze Game"
character_scale = 0.5
player_speed = 3
class MyGame(arcade.Window):
    
    def __init__(self, sprite):
        
        super().__init__(screen_width, screen_height, screen_title)

        arcade.set_background_color(arcade.color.AZURE_MIST)
        # create the list to keep the character in
        self.player_list = arcade.SpriteList()

        # create separate variable that will hold the sprite
        self.player_sprite = None
        self.player_sprite_image = sprite
    
    def setup(self):
        # create player sprite and store it in the variables
        self.player_sprite = arcade.Sprite(self.player_sprite_image, character_scale)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        # make grid for maze
        
    def on_draw(self):
        arcade.start_render()

        #draw the sprites 
        self.player_list.draw()
    

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = player_speed
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -player_speed
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = player_speed
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -player_speed
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = 0
