import arcade

screen_width = 1000
screen_height = 700
screen_title = "Maze Game"
class MyGame(arcade.Window):
    
    def __init__(self):
        
        super().__init__(screen_width, screen_height, screen_title)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
    
    def setup(self):
        pass

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()