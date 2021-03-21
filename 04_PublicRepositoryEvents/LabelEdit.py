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
        self.textField = tk.StringVar()
        #self.textField.set("My Label")
        super().__init__(master, textvariable=self.textField, 
            takefocus=True, highlightthickness=3, highlightcolor='#000fff000')
        self.bind('<Button-1>', self.mouse_click)
        self.bind('<KeyPress>', self.key_click)
        self.cursor = tk.Frame(self, background='#000000', width=3)
        self.cursor.place(x=0, y=0, height=20)        

    def mouse_click(self, event):
        '''Mouse click handler'''
        self.focus()

    def key_click(self, event):
        '''Key click handler'''
        self.textField.set(self.textField.get() + event.char)

class App(Application):
    def create_widgets(self):
        super().create_widgets()
        self.L = InputLabel(self)
        self.Q = tk.Button(self, text="Quit", command=self.master.quit)
        self.Q.grid(row=1, sticky="ES")
        self.L.grid(row=0)
        
app = App(title="LabelEdit application")
app.mainloop()