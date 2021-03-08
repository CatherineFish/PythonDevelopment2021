import tkinter as tk
from random import shuffle, seed

seed()
PUZZLE_NUM = 15

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
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)        
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
                

        self.newButton = tk.Button(self, text='New', command=self.new)
        self.exitButton = tk.Button(self, text='Exit', command=self.exit)
        self.listOfNumberButton = list()
        self.numbers = list()
        self.listNum = list(range(1, 17))

        for i in range(PUZZLE_NUM):
            self.numbers.append(tk.StringVar())
        for i in range(PUZZLE_NUM):
            self.listOfNumberButton.append(tk.Button(self, textvariable=self.numbers[i], command=self.move))
        self.new()

        self.newButton.grid(row=0, column=0, columnspan=2, sticky="NEWS")
        self.exitButton.grid(row=0, column=2, columnspan=2, sticky="NEWS")
        for i in range(PUZZLE_NUM):
            self.listOfNumberButton[i].grid(row=1 + int(i / 4), column=int(i % 4), sticky="NEWS")        


    def new(self):
        """Handler for the new button that changes the values of the number buttons"""
        shuffle(self.listNum)
        for i in range(PUZZLE_NUM):
            self.numbers[i].set(self.listNum[i])

    
    def exit(self):
        """Handler for the exit button that closes the application window"""
        self.quit()

    def move(self):
        """Handler for the button with numbers"""
        pass
    
        
app = Application()
app.master.title('15 PUZZLE')
app.mainloop()
