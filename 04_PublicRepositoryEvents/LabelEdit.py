import tkinter as tk
from itertools import product

class Application(tk.Frame):
    '''Sample tkinter application class'''

    def __init__(self, master=None, title="<application>", **kwargs):
        '''Create root window with frame, tune weight and resize'''
        super().__init__(master, **kwargs)
        self.master.title(title)
        #self.master.columnconfigure(0, weight=1)
        #self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.create_widgets()
        #for column in range(self.grid_size()[0]):
        #    self.columnconfigure(column, weight=1)
        #for row in range(self.grid_size()[1]):
        #    self.rowconfigure(row, weight=1)

    def create_widgets(self):
        '''Create all the widgets'''

class InputLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        self.textField = tk.StringVar()
        self.textField.set("My Label")
        super().__init__(master, text="Label", takefocus=True, highlightthickness=2)

class App(Application):
    def create_widgets(self):
        super().create_widgets()
        self.L = InputLabel(self)
        self.Q = tk.Button(self, text="Quit", command=self.master.quit)
        self.Q.grid(row=1, sticky="ES")
        self.L.grid(row=0)
        
app = App(title="LabelEdit application")
app.mainloop()