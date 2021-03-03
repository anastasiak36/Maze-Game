import tkinter as tk
from PIL import ImageTk, Image
import pyglet, os
class Image_object(object):
    def __init__(self, name, f1le):
        self.name = name
        self.file = f1le
class ImageList(object):
    def __init__(self, file_name):
        self.image_list = []

        f = open(file_name)
        for line in f:
            split = line.split(", ")
            image = Image_object(split[0], split[1].strip())
            self.image_list.append(image)
class Character_Selection(tk.Frame):

    def __init__(self, image_list, master, callback_on_selected):
        super().__init__(master)

        self.images_list = image_list
        self.callback_on_selected = callback_on_selected
        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self, text = "Welcome to the maze game! Please Select a Character from the options below. Then, click the button at the bottom of the screen to start the game. \n Move around the maze, using the arrow keys on your keyboard, while collecting coins to reach the treasure box at the end. Try to collect all the coins!",
        font = 'Georgia 14', fg = 'Purple3'
        ).grid(row = 0, column = 0, sticky = tk.NSEW, columnspan = 8)
        
        row = 3
        image_row = 2
        column = 0
        self.image_file = tk.StringVar()
        self.image_file.set(None)

        for i in self.images_list.image_list:
            
            tk.Radiobutton(self, text= i.name, font = 'Georgia 13', fg = 'Purple3', variable = self.image_file, value = i.file
            ).grid(row = row, column = column, sticky = tk.W)

            imageSmall = tk.PhotoImage(file = i.file)
            w= tk.Label (self,
                        image = imageSmall, 
                         )
            
            w.photo = imageSmall 
            w.grid (row = image_row, column = column, sticky = tk.W)

            column += 1
            if column == 4:
                row += 2
                image_row += 2
                column = 0
        # 
        imageSmall = tk.PhotoImage(file = "Maze-Game/images/maze_snip.PNG")
        w= tk.Label (self,
                        image = imageSmall, 
                         )
            
        w.photo = imageSmall 
        w.grid (row = 2, column = 5, columnspan = 3, rowspan = 5, sticky = tk.NSEW)
        
        # create the button
        tk.Button(self, text = "Start Game!", font = "Georgia 13 bold", fg = 'White', bg = 'Brown4', command = self.selected_clicked
        ).grid(row = 7, column = 7, sticky = tk.E)
        

    def selected_clicked(self):
        self.callback_on_selected(self.image_file.get())