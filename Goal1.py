import arcade
class MyGame(arcade.Window):
    
    def __init__(self):
        
        super().__init__(1000, 700, "Maze Game")

        arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)
    
    def setup(self):
        pass

def main():
    window = MyGame()
    window.setup()
    arcade.run()

main()