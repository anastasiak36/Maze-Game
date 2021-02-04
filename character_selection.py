import tkinter as tk
class Images(object):
    def __init__(self, file_name):
        self.image_list = []

        f = open(file_name)
        for line in f:
            self.image_list.append(line)

class Character_Selection(tk.Frame):
    def __init__(self, images_list, master):
        super().__init__(master)
        self.images_list = images_list

        self.grid()
        self.create_widgets()
    
    def create_widgets(self):
        pass