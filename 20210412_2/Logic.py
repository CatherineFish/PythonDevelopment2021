"""
Logic.py
~~~~~~~~

Skeleton application module.

Provides base class for application build.

:copyright: (c) 2021 by Ekaterina Chekhonina
:license: MIT, see COPYING for more details.
"""
import tkinter as tk


class Application(tk.Frame):
    """
    Sample tkinter application class.

    :param master: master window (tkinter root if None)
    :param title: application window title
    """

    def __init__(self, master=None, title="<application>", **kwargs):
        """Create root window with frame, tune weight and resize."""
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
        """Create all the widgets."""
