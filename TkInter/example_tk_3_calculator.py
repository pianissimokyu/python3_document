__author__ = 'raven'

import tkinter as tk
import tkinter.ttk as ttk

class Example(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("Calculator")
        self.style = ttk.Style()
        self.style.theme_use("default")

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        entry = ttk.Entry(self)
        entry.grid(row=0, columnspan=4, sticky=tk.W + tk.E)
        cls = ttk.Button(self, text="Cls")
        cls.grid(row=1, column=0)
        bck = ttk.Button(self, text="Back")
        bck.grid(row=1, column=1)
        lbl = ttk.Button(self)
        lbl.grid(row=1, column=2)
        clo = ttk.Button(self, text="Close")
        clo.grid(row=1, column=3)
        pb_7 = ttk.Button(self, text="7")
        pb_7.grid(row=2, column=0)
        pb_8 = ttk.Button(self, text="8")
        pb_8.grid(row=2, column=1)
        pb_9 = ttk.Button(self, text="9")
        pb_9.grid(row=2, column=2)
        div = ttk.Button(self, text="/")
        div.grid(row=2, column=3)

        pb_4 = ttk.Button(self, text="4")
        pb_4.grid(row=3, column=0)
        pb_5 = ttk.Button(self, text="5")
        pb_5.grid(row=3, column=1)
        pb_6 = ttk.Button(self, text="6")
        pb_6.grid(row=3, column=2)
        mul = ttk.Button(self, text="*")
        mul.grid(row=3, column=3)

        pb_1 = ttk.Button(self, text="1")
        pb_1.grid(row=4, column=0)
        pb_2 = ttk.Button(self, text="2")
        pb_2.grid(row=4, column=1)
        pb_3 = ttk.Button(self, text="3")
        pb_3.grid(row=4, column=2)
        mns = ttk.Button(self, text="-")
        mns.grid(row=4, column=3)

        pb_0 = ttk.Button(self, text="0")
        pb_0.grid(row=5, column=0)
        dot = ttk.Button(self, text=".")
        dot.grid(row=5, column=1)
        equ = ttk.Button(self, text="=")
        equ.grid(row=5, column=2)
        pls = ttk.Button(self, text="+")
        pls.grid(row=5, column=3)

        self.pack()

def main():

    root = tk.Tk()
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
