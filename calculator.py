from tkinter.constants import *
import tkinter


class Calculator():
    """A calculator program."""

    def __init__(self):
        """Sets up the calculator GUI. """

        # Memory
        self.register = [None, None]
        self.pointer = 0

        # Flags for telling calculator which operation to do
        self.flag = {'add': False,
                     'subtract': False,
                     'multiply': False,
                     'divide': False}

        # Main/Root container
        self.root = tkinter.Tk()
        self.root.title("Calculator")

        # Text variable to be displayed inside the "LCD"
        self.text_value = tkinter.StringVar()

        self.frame = tkinter.Frame(self.root, bg='red')
        self.frame.pack(fill=BOTH, expand=1)

        self.create_widgets()

        # Main loop to listen for events
        self.root.mainloop()