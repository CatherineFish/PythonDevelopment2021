import tkinter as tk
from itertools import product

class Application(tk.Frame):
    '''Sample tkinter application class'''

    def __init__(self, master=None, title="<application>", **kwargs):
        '''Create root window with frame, tune weight and resize'''
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.create_widgets()
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

    def create_widgets(self):
        '''Create all the widgets'''

class InputLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        self.char_size = 20
        self.char_width = 16
        self.textField = tk.StringVar()
        super().__init__(master, textvariable=self.textField, 
            takefocus=True, highlightthickness=3, highlightcolor='#000fff000', font=("Courier", self.char_size),
            anchor="w")
        self.bind('<Button-1>', self.mouse_click)
        self.bind('<KeyPress>', self.key_click)
        #focused from begining
        #self.focus()
        self.cursor = tk.Frame(self, background='#000000', width=1)
        #cursor from begining
        #self.cursor.place(x=0, y=0, height=1.5 * self.char_size)
        self.x_position = 0        

    def mouse_click(self, event):
        '''Mouse click handler'''
        self.focus()
        self.x_position = min(event.x // self.char_width, len(self.textField.get())) * self.char_width
        self.cursor.place(x=self.x_position, y=0, height=1.5 * self.char_size)

    def key_click(self, event):
        '''Key click handler'''
        if event.keysym == "Right":
            self.x_position += self.char_width
        elif event.keysym == "Left":
            self.x_position -= self.char_width
        elif event.keysym in ["KP_Home", "Home", "Up"]:
            self.x_position = 0
        elif event.keysym in ["KP_End", "End", "Down"]:
            self.x_position = len(self.textField.get()) * self.char_width
        elif event.keysym == "BackSpace":
            if len(self.textField.get()) > 1:
                self.textField.set(self.textField.get()[:self.x_position // self.char_width - 1] + self.textField.get()[self.x_position // self.char_width:])
                self.x_position -= self.char_width
            else:
                self.textField.set("")
                self.x_position = 0
        elif event.char.isprintable():
            if self.textField.get():
                self.textField.set(self.textField.get()[:self.x_position // self.char_width] + event.char + self.textField.get()[self.x_position // self.char_width:])
            else:
                self.textField.set(self.textField.get() + event.char)
            self.x_position += self.char_width
        self.cursor.place(x=self.x_position, y=0)
        

class App(Application):
    def create_widgets(self):
        super().create_widgets()
        self.L = InputLabel(self)
        self.Q = tk.Button(self, text="Quit", command=self.master.quit)
        self.Q.grid(row=1, sticky="NES")
        self.L.grid(row=0, sticky="NEWS")
        
app = App(title="LabelEdit application")
app.mainloop()