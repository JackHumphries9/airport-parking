from tkinter import *
from functools import partial
from tkinter import messagebox
import requests
import json
from ast import literal_eval

class Dialogue:
    def __init__(self, master, col, row):
        self.root = Toplevel(master)
        self.root.lift()
        self.root.attributes("-topmost", True)
        self.root.resizable(0, 0)
        self.root.focus()
        self.root.minsize(300, 170)
        self.root.maxsize(300, 170)


        self.exited = False

        self.rowVar = StringVar()
        self.colVar = StringVar()
        self.regVar = StringVar()

        self.headerLabel = Label(self.root, text="Please enter your details")
        self.rowLabel = Label(self.root, text="Row: ")
        self.rowEntry = Entry(self.root, textvariable=self.rowVar)
        self.colLabel = Label(self.root, text="Column: ")
        self.colEntry = Entry(self.root, textvariable=self.colVar)
        self.regLabel = Label(self.root, text="Registration: ")
        self.regEntry = Entry(self.root, textvariable=self.regVar)
        self.submitButton = Button(self.root, text="Park", command=self.submit)

        if col is not None and row is not None:
            self.rowEntry.insert(0, str(row + 1))
            self.colEntry.insert(0, str(col + 1))
            self.rowEntry.config(state=DISABLED)
            self.colEntry.config(state=DISABLED)

        self.headerLabel.grid(column=1, row=0, padx=5, pady=5)
        self.rowLabel.grid(column=0, row=1, padx=5, pady=5)
        self.rowEntry.grid(column=1, row=1, padx=5, pady=5)
        self.colLabel.grid(column=0, row=2, padx=5, pady=5)
        self.colEntry.grid(column=1, row=2, padx=5, pady=5)
        self.regLabel.grid(column=0, row=3, padx=5, pady=5)
        self.regEntry.grid(column=1, row=3, padx=5, pady=5)
        self.submitButton.grid(column=1, row=4, padx=5, pady=5)

        self.root.bind("<Return>", self.submitEnter)

        self.root.mainloop()

    def submitEnter(self, e):
        self.submit()

    def submit(self):
        if len(self.rowVar.get()) == 0 or len(self.colVar.get()) == 0 or len(self.regVar.get()) == 0:
            messagebox.showerror("Error!", "Please make sure all fields are filled out!")
        else:
            self.exited = True
            self.root.destroy()
            self.root.quit()


class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title("Park Car - Airport Parking")

        self.root.minsize(800, 650)
        self.root.maxsize(800, 650)
        self.root.resizable(0, 0)

        self.controlFrameOne = Frame(self.root)
        self.controlFrameTwo = Frame(self.root)

        r = requests.get("http://localhost:5000/fetch_data").text.strip()

        self.grid = list(literal_eval(r))

        for l in range(len(self.grid)):
            self.grid[l] = list(self.grid[l])

        self.btn_grid = []

        c = 0

        for i in range(10):
            for n in range(6):
                t = partial(self.park, i, n)
                self.btn_grid.append(Button(self.controlFrameOne, text="", bg="green", command=t, height=3, width=5))
                self.btn_grid[c].grid(column=i, row=n, padx=5, pady=5)

                if self.grid[n][i] != "empty":
                    self.btn_grid[c].config(bg="red", text=self.grid[n][i])

                c += 1

        self.parkButton = Button(self.controlFrameTwo, text="Park", command=lambda: self.park(None, None))

        self.parkButton.pack(side=TOP, pady=10, padx=5)

        self.controlFrameOne.pack(padx=10, pady=10)
        self.controlFrameTwo.pack()

        self.root.mainloop()

    def park(self, col, row):
        if (col is None and row is None) or self.grid[row][col] == "empty":
            t = Dialogue(self.root, col, row)

            if t.exited is True:
                try:
                    i = int(t.colVar.get()) - 1
                    n = int(t.rowVar.get()) - 1
                    r = t.regVar.get()

                    if 0 <= i < 10 and 0 <= n < 6:

                        if self.grid[n][i] == "empty":

                            self.grid[i][n] = r

                            if requests.get("http://localhost:5000/add_data?col=" + str(i) + "&row=" + str(n) + "&content=" + r).text == "true":
                                btnN = (i * 6) + n
                                self.btn_grid[btnN].config(bg="red", text=r)
                            else:
                                messagebox.showerror("Server Error!", "There was a server error.")
                        else:
                            messagebox.showerror("Space Taken", "This parking space has been taken.")

                    else:
                        messagebox.showerror("Error!", "Please make sure the row and column values you entered correspond to the grid.")

                except:
                    messagebox.showerror("Error!", "You entered invalid data. Please make sure that you enter the row and columns correctly.")
        else:
            messagebox.showerror("Space Taken", "This parking space has been taken.")


test = Window()
