import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("임덕규")
        self.pack(fill=tk.BOTH, expand=1)


def main():
    root = tk.Tk() # 메인윈도우
    root.geometry("250x150+300+300")  # 윈도우 크기위치 변경
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()



