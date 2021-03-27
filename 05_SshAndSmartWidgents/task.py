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

        self.Color = tk.Label(self, text="Color")
        self.Width = tk.Label(self, text="Width")
        self.Outline = tk.Label(self, text="Outline")
        self.Shape = tk.Label(self, text="Shape")


        self.optionColor = ('black', 'white', 'red', 'yellow', 'blue', 'green')
        self.varColor = tk.StringVar()
        self.varColor.set(self.optionColor[0])
        self.optionColor = tk.OptionMenu(self, self.varColor, *self.optionColor)

        self.optionOutline = ('black', 'white', 'red', 'yellow', 'blue', 'green')
        self.varOutline = tk.StringVar()
        self.varOutline.set(self.optionOutline[2])
        self.optionOutline = tk.OptionMenu(self, self.varOutline, *self.optionOutline)

        self.optionWidth = ('1', '2', '3', '4', '5', '6')
        self.varWidth = tk.StringVar()
        self.varWidth.set(self.optionWidth[2])
        self.optionWidth = tk.OptionMenu(self, self.varWidth, *self.optionWidth)

        self.optionShape = ('oval', 'rectangle', 'arc')
        self.varShape = tk.StringVar()
        self.varShape.set(self.optionShape[0])
        self.optionShape = tk.OptionMenu(self, self.varShape, *self.optionShape)


        self.figureLog = []
        self.figureLogShape = []        
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
        
        self.optionColor.grid(row=1, column=1, sticky="NEWS")
        self.optionWidth.grid(row=1, column=2, sticky="NEWS")
        self.optionOutline.grid(row=1, column=3, sticky="NEWS")
        self.optionShape.grid(row=1, column=4, sticky="NEWS")
        self.Color.grid(row=0, column=1, sticky="NEWS")
        self.Width.grid(row=0, column=2, sticky="NEWS")
        self.Outline.grid(row=0, column=3, sticky="NEWS")
        self.Shape.grid(row=0, column=4, sticky="NEWS")
        self.text.grid(row=2, column=0, sticky="NEWS")
        self.canvas.grid(row=2, column=1, columnspan=4, sticky="NEWS")
        self.draw.grid(row=3, column=0, sticky="NEWS")
        self.Q.grid(row=3, column=1, columnspan=4, sticky="NEWS")

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
                if self.varShape.get() == 'oval':
                    self.cur_fig = self.canvas.create_oval(*self.oval_coord, fill=self.varColor.get(), outline=self.varOutline.get(), width=self.varWidth.get())
                elif self.varShape.get() == 'arc':
                    self.cur_fig = self.canvas.create_arc(*self.oval_coord, fill=self.varColor.get(), outline=self.varOutline.get(), width=self.varWidth.get())
                elif self.varShape.get() == 'rectangle':
                    self.cur_fig = self.canvas.create_rectangle(*self.oval_coord, fill=self.varColor.get(), outline=self.varOutline.get(), width=self.varWidth.get())
                self.mode = 1 #Draw-mode
            self.init_state = 1
        elif self.mode:
            self.canvas.delete(self.cur_fig)
            self.oval_coord[2] = event.x
            self.oval_coord[3] = event.y
            if self.varShape.get() == 'oval':
                self.cur_fig = self.canvas.create_oval(*self.oval_coord, fill=self.varColor.get(), outline=self.varOutline.get(), width=self.varWidth.get())
            elif self.varShape.get() == 'arc':
                self.cur_fig = self.canvas.create_arc(*self.oval_coord, fill=self.varColor.get(), outline=self.varOutline.get(), width=self.varWidth.get())
            elif self.varShape.get() == 'rectangle':
                self.cur_fig = self.canvas.create_rectangle(*self.oval_coord, fill=self.varColor.get(), outline=self.varOutline.get(), width=self.varWidth.get())
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
                if self.varShape.get() == 'oval':
                    self.cur_fig = self.canvas.create_oval(*self.oval_coord, fill=self.varColor.get(), outline=self.varOutline.get(), width=self.varWidth.get())
                    self.text.insert(tk.END, f"oval <{self.canvas.coords(self.cur_fig)[0]} {self.canvas.coords(self.cur_fig)[1]} {self.canvas.coords(self.cur_fig)[2]} {self.canvas.coords(self.cur_fig)[3]}> width={self.canvas.itemconfigure(self.cur_fig)['width'][-1]} outline={self.canvas.itemconfigure(self.cur_fig)['outline'][-1]} fill={self.canvas.itemconfigure(self.cur_fig)['fill'][-1]}\n")
                elif self.varShape.get() == 'arc':
                    self.cur_fig = self.canvas.create_arc(*self.oval_coord, fill=self.varColor.get(), outline=self.varOutline.get(), width=self.varWidth.get())
                    self.text.insert(tk.END, f"arc <{self.canvas.coords(self.cur_fig)[0]} {self.canvas.coords(self.cur_fig)[1]} {self.canvas.coords(self.cur_fig)[2]} {self.canvas.coords(self.cur_fig)[3]}> width={self.canvas.itemconfigure(self.cur_fig)['width'][-1]} outline={self.canvas.itemconfigure(self.cur_fig)['outline'][-1]} fill={self.canvas.itemconfigure(self.cur_fig)['fill'][-1]}\n")
                elif self.varShape.get() == 'rectangle':
                    self.cur_fig = self.canvas.create_rectangle(*self.oval_coord, fill=self.varColor.get(), outline=self.varOutline.get(), width=self.varWidth.get())
                    self.text.insert(tk.END, f"rectangle <{self.canvas.coords(self.cur_fig)[0]} {self.canvas.coords(self.cur_fig)[1]} {self.canvas.coords(self.cur_fig)[2]} {self.canvas.coords(self.cur_fig)[3]}> width={self.canvas.itemconfigure(self.cur_fig)['width'][-1]} outline={self.canvas.itemconfigure(self.cur_fig)['outline'][-1]} fill={self.canvas.itemconfigure(self.cur_fig)['fill'][-1]}\n")
                
                self.figureLog.append(self.cur_fig)
                self.figureLogShape.append(self.varShape.get())
                
                
            else: 
                self.canvas.move(self.cur_fig, event.x - self.oval_coord[0], event.y - self.oval_coord[1])
                self.text.delete(str(self.figureLog.index(self.cur_fig) + 1) + '.0', str(self.figureLog.index(self.cur_fig) + 1) + '.end')
                if self.figureLogShape[self.figureLog.index(self.cur_fig)] == 'oval':
                    self.text.insert(str(self.figureLog.index(self.cur_fig) + 1) + '.0', f"oval <{self.canvas.coords(self.cur_fig)[0]} {self.canvas.coords(self.cur_fig)[1]} {self.canvas.coords(self.cur_fig)[2]} {self.canvas.coords(self.cur_fig)[3]}> width={self.canvas.itemconfigure(self.cur_fig)['width'][-1]} outline={self.canvas.itemconfigure(self.cur_fig)['outline'][-1]} fill={self.canvas.itemconfigure(self.cur_fig)['fill'][-1]}")
                elif self.figureLogShape[self.figureLog.index(self.cur_fig)] == 'arc':
                    self.text.insert(str(self.figureLog.index(self.cur_fig) + 1) + '.0', f"arc <{self.canvas.coords(self.cur_fig)[0]} {self.canvas.coords(self.cur_fig)[1]} {self.canvas.coords(self.cur_fig)[2]} {self.canvas.coords(self.cur_fig)[3]}> width={self.canvas.itemconfigure(self.cur_fig)['width'][-1]} outline={self.canvas.itemconfigure(self.cur_fig)['outline'][-1]} fill={self.canvas.itemconfigure(self.cur_fig)['fill'][-1]}")
                elif self.figureLogShape[self.figureLog.index(self.cur_fig)] == 'rectangle':
                    self.text.insert(str(self.figureLog.index(self.cur_fig) + 1) + '.0', f"rectangle <{self.canvas.coords(self.cur_fig)[0]} {self.canvas.coords(self.cur_fig)[1]} {self.canvas.coords(self.cur_fig)[2]} {self.canvas.coords(self.cur_fig)[3]}> width={self.canvas.itemconfigure(self.cur_fig)['width'][-1]} outline={self.canvas.itemconfigure(self.cur_fig)['outline'][-1]} fill={self.canvas.itemconfigure(self.cur_fig)['fill'][-1]}")
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
                    shape, coords, width, outline, fill = re.findall(r"(.*) <(.*)> width=(.*) outline=(.*) fill=(.*)", figure)[0]
                    if shape == 'oval':
                        curFig = self.canvas.create_oval(coords.split('\n'), fill=fill, outline=outline, width=width)
                    elif shape == 'arc':
                        curFig = self.canvas.create_arc(coords.split('\n'), fill=fill, outline=outline, width=width)
                    elif shape == 'rectangle':
                        curFig = self.canvas.create_rectangle(coords.split('\n'), fill=fill, outline=outline, width=width)
                    
                except:
                    self.figureLog.append(0)
                    self.figureLogShape.append("0")
                    
                    self.text.tag_remove('correct', str(len(self.figureLog)) + '.0', str(len(self.figureLog)) + '.end')
                    self.text.tag_add('incorrect', str(len(self.figureLog)) + '.0', str(len(self.figureLog)) + '.end') 
                else:
                    self.figureLog.append(curFig)
                    self.figureLogShape.append(shape)
                    self.text.tag_remove('incorrect', str(len(self.figureLog)) + '.0', str(len(self.figureLog)) + '.end')
                    self.text.tag_add('correct', str(len(self.figureLog)) + '.0', str(len(self.figureLog)) + '.end')

app = App(title="Graph Editor")
app.mainloop()