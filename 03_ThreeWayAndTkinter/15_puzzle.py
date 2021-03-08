import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.newButton = tk.Button(self, text='New', command=self.new)
        self.exitButton = tk.Button(self, text='Exit', command=self.exit)

        self.newButton.grid()
        self.exitButton.grid()
        
    def new(self):
        """Handler for the new button"""
        pass

    def exit(self):
        """Handler for the exit button that closes the application window"""
        pass
   

        
app = Application()
app.master.title('15 PUZZLE')
app.mainloop()
