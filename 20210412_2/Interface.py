"""
Homework application interface.

- Functions and classes have few parameters
"""
import tkinter as tk
from Logic import Application


class App(Application):
    """Main application class."""

    def create_widgets(self):
        """All widgets of this application."""
        super().create_widgets()
        validHandler = self.register(self.validHandler)
        self.S = tk.StringVar()
        self.inputEntry = tk.Entry(self, textvariable=self.S, validate='all',
                                   validatecommand=(validHandler, '%P'))

        self.optionList = ('One', 'Two', 'Three')
        self.variable = tk.StringVar()
        self.variable.set(self.optionList[0])
        self.optionMenu = tk.OptionMenu(self, self.variable, *self.optionList)

        self.insert = tk.Button(self, text="Insert", command=self.insert)

        self.labelStr = tk.StringVar()
        self.labelStr.set("Default")
        self.label = tk.Label(self, textvariable=self.labelStr)
        self.label.bind('<Enter>', self.enterEvent)
        self.label.bind('<Leave>', self.leaveEvent)

        self.show = tk.Button(self, text="Show", command=self.show)

        self.inputEntry.grid(row=0, columnspan=3, sticky="NEWS")
        self.optionMenu.grid(row=1, column=0, sticky="NEWS")
        self.insert.grid(row=1, column=1, sticky="NEWS")
        self.show.grid(row=1, column=2, sticky="NEWS")
        self.label.grid(row=2, columnspan=3, sticky="NEWS")

    def validHandler(self, result):
        """
        Entry handler.

        Does not allow more than 10 characters

        :param result: gets the string that will be obtained when a new character is entered
        """
        return len(result) <= 10

    def insert(self):
        """Insert button handler."""
        self.S.set((self.S.get() + self.variable.get())[:10])

    def enterEvent(self, event):
        """
        Enter Event reaction.

        Reacts to the appearance of a mouse on the label

        :param event: the appearance of the mouse
        """
        self.labelStr.set("Hi Mouse")

    def leaveEvent(self, event):
        """
        Leave Event reaction.

        Reacts to the disappearance of the mouse from the label

        :param event: the disappearance of the mouse
        """
        self.labelStr.set("Bye Mouse")

    def show(self):
        """
        Show button handler.

        Transfers text from entry to label
        """
        self.labelStr.set(self.S.get())


def main():
    """Call main application ."""
    app = App(title="Sample application")
    app.mainloop()


if __name__ == "__main__":
    main()
