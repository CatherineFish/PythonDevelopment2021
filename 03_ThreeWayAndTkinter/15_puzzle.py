import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()

    def createWidgets(self):
        top = self.winfo_toplevel()                
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.newButton = tk.Button(self, text='New', command=self.new)
        self.exitButton = tk.Button(self, text='Exit', command=self.exit)


        self.newButton.grid(row=0, column=0, sticky="NEWS")
        self.exitButton.grid(row=0, column=1, sticky="NEWS")
        
    def new(self):
        """Handler for the new button"""
        pass

    def exit(self):
        """Handler for the exit button that closes the application window"""
        pass
   

        
app = Application()
app.master.title('15 PUZZLE')
app.mainloop()
