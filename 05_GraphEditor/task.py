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
        self.mode = 1
        self.cur_fig = 0
        self.init_state = 0
        self.oval_coord = [0., 0., 0., 0.]
        self.canvas = tk.Canvas(self)
        self.canvas.bind("<Button-1>", self.justClickMouse)
        self.canvas.bind("<B1-Motion>", self.clickMouse)
        self.canvas.bind("<ButtonRelease-1>", self.releaseMouse)
        self.Q = tk.Button(self, text="Quit", command=self.master.quit)
        
        self.text.grid(row=0, column=0, sticky="NEWS")
        self.canvas.grid(row=0, column=1, sticky="NEWS")
        self.Q.grid(row=1, columnspan=2, sticky="NEWS")

    def justClickMouse(self, event):
        '''Only Mouse click handler'''
        pass

    def clickMouse(self, event):
        '''Mouse click handler'''
        if not self.init_state:
            self.oval_coord[0] = event.x
            self.oval_coord[2] = event.x
            self.oval_coord[1] = event.y
            self.oval_coord[3] = event.y
            if self.canvas.find_overlapping(*self.oval_coord):
                self.cur_fig = self.canvas.find_overlapping(*self.oval_coord)[-1]
                self.mode = 0 #Move-mode
            else:
                self.cur_fig = self.canvas.create_oval(*self.oval_coord)
                self.mode = 1 #Draw-mode
            self.init_state = 1
        elif self.mode:
            self.canvas.delete(self.cur_fig)
            self.oval_coord[2] = event.x
            self.oval_coord[3] = event.y
            self.cur_fig = self.canvas.create_oval(*self.oval_coord, fill= '#FF69B4', outline='#8B008B', width=3)
        else:
            self.canvas.move(self.cur_fig, event.x - self.oval_coord[0], event.y - self.oval_coord[1])
            self.oval_coord[0] = event.x
            self.oval_coord[2] = event.x
            self.oval_coord[1] = event.y
            self.oval_coord[3] = event.y
            
    def releaseMouse(self, event):
        '''Mouse release handler'''
        if self.init_state:
            if self.mode:
                self.canvas.delete(self.cur_fig)
                self.oval_coord[2] = event.x
                self.oval_coord[3] = event.y
                self.cur_fig = self.canvas.create_oval(*self.oval_coord, fill= '#FF69B4', outline='#8B008B', width=2)


                self.text.insert(tk.END, f"oval <{self.canvas.coords(self.cur_fig)[0]} {self.canvas.coords(self.cur_fig)[1]} {self.canvas.coords(self.cur_fig)[2]} {self.canvas.coords(self.cur_fig)[3]}> width={self.canvas.itemconfigure(self.cur_fig)['width'][-1]} outline={self.canvas.itemconfigure(self.cur_fig)['outline'][-1]} fill={self.canvas.itemconfigure(self.cur_fig)['fill'][-1]}\n")
            else: 
                self.canvas.move(self.cur_fig, event.x - self.oval_coord[0], event.y - self.oval_coord[1])
            self.init_state = 0


app = App(title="Sample application")
app.mainloop()