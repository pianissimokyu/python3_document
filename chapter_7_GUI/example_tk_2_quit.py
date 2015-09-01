__author__ = 'raven'

import tkinter as tk

class Example(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("Quit button")

        self.pack(fill=tk.BOTH, expand=1)

        quitButton = tk.Button(self, text="Quit",
            command=self.quit)
        quitButton.place(x=50, y=50)


def main():

    root = tk.Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
