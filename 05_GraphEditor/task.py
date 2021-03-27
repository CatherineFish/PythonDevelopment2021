'''
Tkinter skeleton app
'''
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

class App(Application):
    def create_widgets(self):
        super().create_widgets()
        self.text = tk.Text(self, undo=True, wrap=tk.WORD, font="fixed")
        self.canvas = tk.Canvas(self)
        self.Q = tk.Button(self, text="Quit", command=self.master.quit)
        
        self.text.grid(row=0, column=0, sticky="NEWS")
        self.canvas.grid(row=0, column=1, sticky="NEWS")
        self.Q.grid(row=1, columnspan=2, sticky="NEWS")


app = App(title="Sample application")
app.mainloop()