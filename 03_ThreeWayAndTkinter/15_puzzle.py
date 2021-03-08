import tkinter as tk
from random import shuffle, seed
from functools import partial
from tkinter import messagebox

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
        
        #Frame configuration
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)        
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
                
        #Frame elements
        self.newButton = tk.Button(self, text='New', command=self.new)
        self.exitButton = tk.Button(self, text='Exit', command=self.exit)
        self.listOfNumberButton = list()
        self.numbers = list()
        self.listNum = list(range(1, 1 + PUZZLE_NUM))
        
        #Blank space
        self.blank_row = 4
        self.blank_col = 3

        #Button randomization
        for i in range(PUZZLE_NUM):
            self.numbers.append(tk.StringVar())
        for i in range(PUZZLE_NUM):
            self.listOfNumberButton.append(tk.Button(self, textvariable=self.numbers[i], command=partial(self.move, i)))
        
        #Grid
        self.newButton.grid(row=0, column=0, columnspan=2,  sticky="NEWS")
        self.exitButton.grid(row=0, column=2, columnspan=2, sticky="NEWS")   
        self.new()
        

    def new(self):
        """Handler for the new button that changes the values of the number buttons"""
        f = True
        while f:
            shuffle(self.listNum)
            sum = 0
            for i in range(PUZZLE_NUM):
                for j in range(i, PUZZLE_NUM):
                    if self.listNum[j] < self.listNum[i]:
                        sum += 1
            if not(sum % 2):
                f = False
        for i in range(PUZZLE_NUM):
            self.numbers[i].set(self.listNum[i])
            self.listOfNumberButton[i].grid(row=1 + int(i / 4), column=int(i % 4), sticky="NEWS")        
        
    
    def exit(self):
        """Handler for the exit button that closes the application window"""
        self.quit()


    def move(self, i):
        """Handler for the button with numbers"""

        #Move
        cur_row = self.listOfNumberButton[i].grid_info()['row']
        cur_col = self.listOfNumberButton[i].grid_info()['column']
        if (cur_row + 1) == self.blank_row and cur_col == self.blank_col:
            self.listOfNumberButton[i].grid(row=self.blank_row, column=self.blank_col, sticky="NEWS")
            self.blank_row -= 1
        elif (cur_row - 1) == self.blank_row and cur_col == self.blank_col:
            self.listOfNumberButton[i].grid(row=self.blank_row, column=self.blank_col, sticky="NEWS")
            self.blank_row += 1    
        elif cur_row == self.blank_row and (cur_col + 1) == self.blank_col:
            self.listOfNumberButton[i].grid(row=self.blank_row, column=self.blank_col, sticky="NEWS")
            self.blank_col -= 1            
        elif cur_row == self.blank_row and (cur_col - 1) == self.blank_col:
            self.listOfNumberButton[i].grid(row=self.blank_row, column=self.blank_col, sticky="NEWS")
            self.blank_col += 1    
        
        #Check
        if self.blank_row == 4 and self.blank_col == 3:
            cur_list = list()
            for i in range(PUZZLE_NUM):
                if self.grid_slaves(row=1 + int(i / 4), column=int(i % 4))[0]['text'] != i + 1:
                    break
            if i == PUZZLE_NUM - 1:
                messagebox.showinfo(message="You win!")
                self.new()

app = Application()
app.master.title('15 PUZZLE')
app.mainloop()
