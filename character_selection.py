import tkinter as tk
from PIL import ImageTk, Image
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
            image = Image_object(split[0], split[1])
            self.image_list.append(image)
class Character_Selection(tk.Frame):

    def __init__(self, image_list, master):
        super().__init__(master)

        self.image_list = image_list

        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        row = 2
        image_row = 1
        column = 0
        self.image_file = tk.StringVar()
        self.image_file.set(None)

        for i in self.image_list:
            
            tk.Radiobutton(self, text= i.name, font = 'ComicSansMS 14', fg = 'Purple', variable = self.image_file, value = i.file
            ).grid(row = row, column = column, sticky = tk.W)

            imageSmall = Image.open(i.file)
            imageSmall.resize((100,100), Image.ANTIALIAS)
            w= tk.Label (self,
                        image = imageSmall, 
                         )
            
            w.photo = imageSmall 
            w.grid (row = image_row, column = column)

            column += 1
            if column == 4:
                row += 1
                image_row += 1
                column = 0

        

