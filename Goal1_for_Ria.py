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

        