import tkinter as tk

class FdFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master
        self.pack(padx=20, pady=20, anchor="w")

    def create_label(self, title):
        label = tk.Label(self, text=('%s:' % title), font=("Helvetica", 16, "bold"))
        label.pack(anchor="w")

        contents = tk.StringVar()
        contents.set("undefined")

        label = tk.Label(self, textvariable=contents, font=("Helvetica", 16))
        label.pack(anchor="w")

        return contents

if __name__ == '__main__':
    class App(FdFrame):
        pass

    # create the application
    app = App()

    app.contents = app.create_label("Foo")
    app.contents.set('2018')

    app.master.title("Do-Nothing Application")
    # app.master.maxsize(1000, 600)

    # start the program
    app.mainloop()



