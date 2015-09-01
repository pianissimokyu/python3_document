__author__ = 'raven'

import tkinter as tk

class Example(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Centered window")
        self.pack(fill=tk.BOTH, expand=1)

        self.centerWindow()

    def centerWindow(self):
        w = 290
        h = 150

        # screen 크기를 구함
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

def main():

    root = tk.Tk()
    ex = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()