#This is the file where we will create the maze for the game. 

import random 
import arcade

local_sprite = 128
sprite_scale = 0.25
sprite_size = local_sprite * sprite_scale

screen_width = 1000
screen_height = 700
screen_title = "Maze Game"

player_speed = 3

empty_tile = 0
crate_tile = 1
chest_tile = 2 

maze_height = 31
maze_width = 31

r = 15

viewport_margin = 300



def _creating_the_grid(width, height):
    grid = []
    for row in range(height):
        grid.append([])
        for column in range(width):
            if column % 2 == 1 and row % 2 == 1:
                grid[row].append(empty_tile)
            elif column == 0 or row == 0 or column == width - 1 or row == height - 1:
                grid[row].append(crate_tile)
            else:
                grid[row].append(crate_tile)
    
    grid[r][width-1] = empty_tile
    return grid

def make_maze_depth_first(maze_width, maze_height):
    maze = _creating_the_grid(maze_width, maze_height)
    width_for_maze = (len(maze[0]) - 1) // 2
    height_for_maze = (len(maze) - 1) // 2
    vis = [[0] * width_for_maze + [1] for _ in range(height_for_maze)] + [[1] * (width_for_maze+1)]

    def walk (x: int, y: int):
        vis[y][x] = 1

        depth_for_maze = [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]
        random.shuffle(depth_for_maze)
        for (xx, yy) in depth_for_maze:
            if vis[yy][xx]:
                continue
            if xx == x:
                maze[max(y, yy) * 2][x*2+1] = empty_tile
            if yy == y:
                maze[y*2+1][max(x,xx)*2] = empty_tile
            
            walk(xx, yy)


    walk(random.randrange(width_for_maze),random.randrange(height_for_maze))
    return maze
class MyGame(arcade.Window):

    def __init__(self, sprite, callback_on_exit):
        
        super().__init__(screen_width, screen_height, screen_title)
        # create the list to keep the character in
        self.player_sprite_image = sprite

        self.player_list = None
        self.wall_list = None
        self.treasure_list = None
        self.coin_list = None
        self.exit_list = None

        self.score = 0
        self.player_sprite = None

        self.physics_engine = None

        self.coin_count = 0
        self.hit = False

        self.view_bottom = 0
        self.view_left = 0

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.treasure_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.exit_list = arcade.SpriteList()

        self.score = 0

        maze = make_maze_depth_first(maze_width, maze_height)

        for row in range(maze_height):
            for column in range(maze_width):
                if maze[row][column] == 1:
                    wall = arcade.Sprite("Maze-Game/images/brick_wall.PNG", sprite_scale) 
                    wall.center_x = column * sprite_size + sprite_size / 2
                    wall.center_y = row * sprite_size + sprite_size / 2
                    self.wall_list.append(wall)
        
    
        count = 0
        while count < 30:
            row = random.randrange(1, 30)
            column = random.randrange(1,30)
            if maze[row][column] == 0:
                coin = arcade.Sprite("Maze-Game/images/coin.gif", sprite_scale)
                coin.center_x = column * sprite_size + sprite_size / 2
                coin.center_y = row * sprite_size + sprite_size / 2
                self.coin_list.append(coin)
                count += 1

        chest = arcade.Sprite("Maze-Game/images/open_treasure_chest.PNG", sprite_scale)
        chest.center_x = 30 * sprite_size + sprite_size / 2
        chest.center_y = r * sprite_size + sprite_size / 2
        self.treasure_list.append(chest)

        self.player_sprite = arcade.Sprite(self.player_sprite_image, sprite_scale)
        self.player_list.append(self.player_sprite)


        placed = False
        while not placed:

            w = maze_width * sprite_size
            h = maze_height * sprite_size
            self.player_sprite.center_x = random.randrange(w)
            self.player_sprite.center_y = random.randrange(h)

            walls_hit = arcade.check_for_collision_with_list(self.player_sprite, self.wall_list)
            if len(walls_hit) == 0:
                placed = True

            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

            arcade.set_background_color(arcade.csscolor.MINT_CREAM)
            self.view_left = 0
            self.view_bottom = 0
            print(f"Total number of wall blocks: {len(self.wall_list)}")

    def on_draw(self):
        arcade.start_render()

        self.wall_list.draw()
        self.player_list.draw()
        self.treasure_list.draw()
        self.coin_list.draw()
        

        output = f"Coins Collected: {self.coin_count}"
        arcade.draw_text(output, self.view_left + 840, screen_height - 20 + self.view_bottom, arcade.color.DARK_BLUE, 16)

        if self.hit == True:
            output_exit = f"Congratulations! You made it! \n Please proceed to the exit!"
            arcade.draw_text(output_exit, 1250, 600 , arcade.color.DARK_BLUE, 24)
            exit_sprite = arcade.Sprite("Maze-Game/images/Exit_sign.jpg", sprite_scale)
            exit_sprite.center_x = 1500
            exit_sprite.center_y = 400 
            self.exit_list.append(exit_sprite)
            self.exit_list.draw()
        
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
    def on_update(self, delta_time):

        self.physics_engine.update()

        chest_hit = arcade.check_for_collision_with_list(self.player_sprite, self.treasure_list)
        if len(chest_hit) == 1:
            self.hit = True
            chest_hit[0].remove_from_sprite_lists()
            
        
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        if len(coin_hit_list) > 0:
            for coin in coin_hit_list:
                coin.remove_from_sprite_lists()
                self.coin_count += 1

        exit_hit = arcade.check_for_collision_with_list(self.player_sprite, self.exit_list)
        if len(exit_hit) == 1:
            self.exit_game()

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
            arcade.set_viewport(self.view_left, screen_width + self.view_left, self.view_bottom, screen_height + self.view_bottom)

    def exit_game(self):
        self.callback_on_exit()


    