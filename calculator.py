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
        def create_widgets(self):
        """
        Method for the creation/placement of buttons/labels.
        """

        # "LCD" screen
        self.display = tkinter.Label(self.frame, textvariable=self.text_value, bg='gray')
        self.display.grid(row=0, column=0, columnspan=5, sticky=NSEW)

        # One button
        self.one = tkinter.Button(self.frame, text='1', command=self.one)
        self.one.grid(row=1, column=0, sticky=NSEW)

        # Two button
        self.two = tkinter.Button(self.frame, text='2', command=self.two)
        self.two.grid(row=1, column=1, sticky=NSEW)

        # Three button
        self.three = tkinter.Button(self.frame, text='3', command=self.three)
        self.three.grid(row=1, column=2, sticky=NSEW)

        # Four button
        self.four = tkinter.Button(self.frame, text='4', command=self.four)
        self.four.grid(row=2, column=0, sticky=NSEW)

        # Five button
        self.five = tkinter.Button(self.frame, text='5', command=self.five)
        self.five.grid(row=2, column=1, sticky=NSEW)

        # Six button
        self.six = tkinter.Button(self.frame, text='6', command=self.six)
        self.six.grid(row=2, column=2, sticky=NSEW)

        # Seven button
        self.seven = tkinter.Button(self.frame, text='7', command=self.seven)
        self.seven.grid(row=3, column=0, sticky=NSEW)

        # Eight button
        self.eight = tkinter.Button(self.frame, text='8', command=self.eight)
        self.eight.grid(row=3, column=1, sticky=NSEW)

        # Nine button
        self.nine = tkinter.Button(self.frame, text='9', command=self.nine)
        self.nine.grid(row=3, column=2, sticky=NSEW)

        # Zero button
        self.zero = tkinter.Button(self.frame, text='0', command=self.zero)
        self.zero.grid(row=4, column=1, sticky=NSEW)

        # Clear button
        self.clear = tkinter.Button(self.frame, text='Clear', command=self.clear)
        self.clear.grid(row=4, column=0, sticky=NSEW)

        # Plus button
        self.add = tkinter.Button(self.frame, text='+', command=self.add)
        self.add.grid(row=1, column=3, sticky=NSEW)

        # Minus button
        self.subtract = tkinter.Button(self.frame, text='-', command=self.subtract)
        self.subtract.grid(row=2, column=3, sticky=NSEW)

        # Multiply button
        self.multiply = tkinter.Button(self.frame, text='*', command=self.multiply)
        self.multiply.grid(row=3, column=3, sticky=NSEW)

        # Divide button
        self.divide = tkinter.Button(self.frame, text='/', command=self.divide)
        self.divide.grid(row=4, column=3, sticky=NSEW)

        # Equals button
        self.equals = tkinter.Button(self.frame, text='=', command=self.equals)
        self.equals.grid(row=4, column=2, sticky=NSEW)

        # Make widgets spread out to fill screen when window is resized.
        # This is accomplished by configuring the rows and columns of a widget's
        # parent.
        self.root.rowconfigure(0, weight=1)

        self.root.columnconfigure(0, weight=1)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)

        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)
