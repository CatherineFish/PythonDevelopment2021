'''
Tkinter skeleton app
'''
import tkinter as tk
from itertools import product
import re

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
        self.figureLog = []
        self.text = tk.Text(self, undo=True, wrap=tk.WORD, font="fixed")
        self.text.tag_config('correct', background='white')
        self.text.tag_config('incorrect', background='red')

        self.mode, self.cur_fig, self.init_state, self.oval_coord = 1, 0, 0, [0., 0., 0., 0.]
        self.canvas = tk.Canvas(self)
        self.canvas.bind("<Button-1>", self.justClickMouse)
        self.canvas.bind("<B1-Motion>", self.clickMouse)
        self.canvas.bind("<ButtonRelease-1>", self.releaseMouse)
       
        self.draw = tk.Button(self, text="Draw", command=self.draw) 
        self.Q = tk.Button(self, text="Quit", command=self.master.quit)
        
        self.text.grid(row=0, column=0, sticky="NEWS")
        self.canvas.grid(row=0, column=1, sticky="NEWS")
        self.draw.grid(row=1, column=0, sticky="NEWS")
        self.Q.grid(row=1, column=1, sticky="NEWS")

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

                self.figureLog.append(self.cur_fig)
                self.text.insert(tk.END, f"oval <{self.canvas.coords(self.cur_fig)[0]} {self.canvas.coords(self.cur_fig)[1]} {self.canvas.coords(self.cur_fig)[2]} {self.canvas.coords(self.cur_fig)[3]}> width={self.canvas.itemconfigure(self.cur_fig)['width'][-1]} outline={self.canvas.itemconfigure(self.cur_fig)['outline'][-1]} fill={self.canvas.itemconfigure(self.cur_fig)['fill'][-1]}\n")
            else: 
                self.canvas.move(self.cur_fig, event.x - self.oval_coord[0], event.y - self.oval_coord[1])
                self.text.delete(str(self.figureLog.index(self.cur_fig) + 1) + '.0', str(self.figureLog.index(self.cur_fig) + 1) + '.end')
                self.text.insert(str(self.figureLog.index(self.cur_fig) + 1) + '.0', f"oval <{self.canvas.coords(self.cur_fig)[0]} {self.canvas.coords(self.cur_fig)[1]} {self.canvas.coords(self.cur_fig)[2]} {self.canvas.coords(self.cur_fig)[3]}> width={self.canvas.itemconfigure(self.cur_fig)['width'][-1]} outline={self.canvas.itemconfigure(self.cur_fig)['outline'][-1]} fill={self.canvas.itemconfigure(self.cur_fig)['fill'][-1]}\n")
            self.init_state = 0

    def draw(self):
        '''Draw button handler'''
        for figure in self.canvas.find_all():
            self.canvas.delete(figure)
        self.figureLog.clear()
        text = self.text.get('1.0', tk.END).split("\n")
        for figure in text:
            if len(figure):
                try:    
                    coords, width, outline, fill = re.findall(r"oval <(.*)> width=(.*) outline=(.*) fill=(.*)", figure)[0]
                    curFig = self.canvas.create_oval(coords.split(' '), width=width, outline=outline, fill=fill)
                except:
                    self.figureLog.append(0)
                    self.text.tag_remove('correct', str(len(self.figureLog)) + '.0', str(len(self.figureLog)) + '.end')
                    self.text.tag_add('incorrect', str(len(self.figureLog)) + '.0', str(len(self.figureLog)) + '.end') 
                else:
                    self.figureLog.append(curFig)
                    self.text.tag_remove('incorrect', str(len(self.figureLog)) + '.0', str(len(self.figureLog)) + '.end')
                    self.text.tag_add('correct', str(len(self.figureLog)) + '.0', str(len(self.figureLog)) + '.end')
app = App(title="Sample application")
app.mainloop()