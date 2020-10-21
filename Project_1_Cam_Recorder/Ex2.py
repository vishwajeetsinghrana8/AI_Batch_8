from tkinter import *

class MyButtons:

    def __init__(self, window):
        frame = Frame(window)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMess)
        self.printButton.pack()

        self.quit = Button(frame, text="QUIT", command=win.destroy)
        self.quit.pack()

    def printMess(self):
        print("This is my first GUI in Python.")

win = Tk()

b = MyButtons(win)

win.mainloop()