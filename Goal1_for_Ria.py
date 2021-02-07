#This is the file where we will create the maze for the game. 

import random 
import arcade
import timeit
import os

local_sprite = 130
sprite_scale = 0.25
sprite_size = local_sprite * sprite_scale

screen_width = 1000
screen_height = 700
screen_title = "Maze Game"

player_speed = 5

empty_tile = 0
crate_tile = 1

maze_height = 901
maze_width = 501

viewport_margin = 300

def creating_the_grid(width, height):
    grid = []
    for row in range(height):
        grid.append([])
        for column in range(width):
            if column % 2 == 0 and row % 2 == 0:
                grid[row].append(empty_tile)
            elif column == 0 or row == 0 or column == width - 1 or row == height - 1:
                grid[row].append(crate_tile)
            else:
                grid[row].append(crate_tile)
        return grid

def make_maze_depth_first(maze_width, maze_height):
    maze = creating_the_grid(maze_width, maze_height)
    width_for_maze = (len(maze[0]) - 1) // 2
    height_for_maze = (len(maze) - 1) // 2
    vis = [[0] * w + [1] for _ in range(height_for_maze)] + [[1] * (w+1)]

    def walk (x: int, y: int):
        vis[y][x] = 1

        depth_for_maze = [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]
        random.shuffle(depth_for_maze)
        for (xx, yy) in depth_for_maze:
            if vis[xx][yy]:
                continue
            if xx = x:
                maze[max(y, yy) * 2][x*2+1] = empty_tile
            if yy = y:
                maze[y*2+1][max(x,xx)*2] = empty_tile
            
            walk(xx, yy)

        
    walk(random.randrange(w), random.randrange(h))
    return maze
class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.player_list = None
        self.wall_list = None

        self.score = 0
        self.player_sprite = None

        self.physics_engine = None

        self.view_bottom = 0
        self.view_left = 0

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.score = 0

        maze = make_maze_depth_first(maze_width, maze_height)

        if not merge_sprites:
            for row in range(maze_height):
                for column in range(maze_width):
                    if maze[row][column] == 1:
                        wall = arcade.Sprite ##TODO for later
                        wall.center_x = column * sprite_size + sprite_size / 2
                        wall.center_y = row * sprite_size + sprite_size / 2
                        self.wall_list.append(wall)
        
        else:
            for row in range(maze_height):
                column = 0
                while column < len(maze):
                    while column < len(maze) and maze[row][column] == 0:
                        column += 1
                    start_column = column
                    while column < len(maze) and maze[row][column] == 1:
                        column += 1
                    end column = column - 1
                    column_count = end_column - start_column + 1
                    column_mid = (start_column + end_column) / 2
                    wall = arcade.Sprite##TODO for later
                    wall.center_x = column_mid * sprite_size + sprite_size / 2
                    wall.center_y = row * sprite_size + sprite_size / 2
                    wall.width = sprite_size  * column_count
                    self.wall_list.append(wall)

        self.player_sprite = arcade.Sprite(":resources:images/animatedcharacters/bluegumdrop/blue.png", sprite_scale)
        self.player_list.append(self.player_sprite)

        placed = False
        while not placed:

            self.player_sprite.center_x = random.randrange(maze_width * sprite_size)
            self.player_sprite.center_y = random.randrange(maze_height * sprite_size)

            walls_hit = arcade.check_for_collision_with_list(self.player_sprite, self.wall_list)
            if len(walls_hit) == 0:
                placed True

            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

            arcade.set_background_color(arcade.color.AZURE_MIST)

            self.view_left = 0
            self.view_bottom = 0
            print(f"Total number of wall blocks: {len(self.wall_list)}")

    def on_draw(self):
        arcade.start_render()

        self.wall_list.draw()
        self.player_list.draw()

        sprite.count = len(self.wall_list)

        output = f"Sprite Count: {sprite_count}"
        arcade.draw_text(output, self.view_left + 20, screen_height - 20 + self.view_bottom, arcade.color.DARK_BLUE, 16)
        

    def on_update(self):

        self.physics_engine.update()

        changed = False

        left_bndry = self.view_left + viewport_margin
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            changed = True

        right_bndry = self.view_left + screen_width - viewport_margin
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            changed = True

        top_bndry = self.view_bottom + screen_width - viewport_margin
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            changed = True

        bottom_bndry = self.view_bottom + viewport_margin
        if self.player_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player_sprite.bottom
            changed = True

        if changed:
            aracde.set_viewport(self.view_left, screen_width + self.view_left, self.view_bottom, screen_height + self.view_bottom)

    def main():
        window = MyGame(screen_width, screen_height, screen_title)
        window.setup()
        arcade.run()

    if __name__ == "__main__":
        main()
    