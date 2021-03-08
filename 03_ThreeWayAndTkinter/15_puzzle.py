import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
app = Application()
app.master.title('15 PUZZLE')
app.mainloop()
