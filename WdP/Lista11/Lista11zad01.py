from tkinter import *


class TicTacToe(Frame):

    player = 0
    font = ("Arial", 15, "bold")
    used1 = 0
    used2 = 0
    used3 = 0
    used4 = 0
    used5 = 0
    used6 = 0
    used7 = 0
    used8 = 0
    used9 = 0

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.place()

    def place(self):
        self.button1 = Button(self)
        self.button1.config(height=5, width=10, font=self.font)
        self.button1["text"] = ""
        self.button1["command"] = self.click1
        self.button1.grid(column=0, row=0)

        self.button2 = Button(self)
        self.button2.config(height=5, width=10, font=self.font)
        self.button2["text"] = ""
        self.button2["command"] = self.click2
        self.button2.grid(column=0, row=1)

        self.button3 = Button(self)
        self.button3.config(height=5, width=10, font=self.font)
        self.button3["text"] = ""
        self.button3["command"] = self.click3
        self.button3.grid(column=0, row=2)

        self.button4 = Button(self)
        self.button4.config(height=5, width=10, font=self.font)
        self.button4["text"] = ""
        self.button4["command"] = self.click4
        self.button4.grid(column=1, row=0)

        self.button5 = Button(self)
        self.button5.config(height=5, width=10, font=self.font)
        self.button5["text"] = ""
        self.button5["command"] = self.click5
        self.button5.grid(column=1, row=1)

        self.button6 = Button(self)
        self.button6.config(height=5, width=10, font=self.font)
        self.button6["text"] = ""
        self.button6["command"] = self.click6
        self.button6.grid(column=1, row=2)

        self.button7 = Button(self)
        self.button7.config(height=5, width=10, font=self.font)
        self.button7["text"] = ""
        self.button7["command"] = self.click7
        self.button7.grid(column=2, row=0)

        self.button8 = Button(self)
        self.button8.config(height=5, width=10, font=self.font)
        self.button8["text"] = ""
        self.button8["command"] = self.click8
        self.button8.grid(column=2, row=1)

        self.button9 = Button(self)
        self.button9.config(height=5, width=10, font=self.font)
        self.button9["text"] = ""
        self.button9["command"] = self.click9
        self.button9.grid(column=2, row=2)

        self.restart = Button(self)
        self.restart.config(text="Restart", font=self.font, command=self.reset)
        self.restart.grid()

        self.quit = Button(self, text="WYJSCIE", fg="red", command=self.master.destroy)
        self.quit.grid(column=2, row=3)

    def click1(self):
        if self.used1 == 0:
            if self.player == 0:
                self.button1.config(text="o")
            else:
                self.button1.config(text="x")
            self.player = not self.player
            self.used1 += 1
        else:
            pass

    def click2(self):
        if self.used2 == 0:
            if self.player == 0:
                self.button2.config(text="o")
            else:
                self.button2.config(text="x")
            self.player = not self.player
            self.used2 += 1
        else:
            pass

    def click3(self):
        if self.used3 == 0:
            if self.player == 0:
                self.button3.config(text="o")
            else:
                self.button3.config(text="x")
            self.player = not self.player
            self.used3 += 1
        else:
            pass

    def click4(self):
        if self.used4 == 0:
            if self.player == 0:
                self.button4.config(text="o")
            else:
                self.button4.config(text="x")
            self.player = not self.player
            self.used4 += 1
        else:
            pass

    def click5(self):
        if self.used5 == 0:
            if self.player == 0:
                self.button5.config(text="o")
            else:
                self.button5.config(text="x")
            self.player = not self.player
            self.used5 += 1
        else:
            pass

    def click6(self):
        if self.used6 == 0:
            if self.player == 0:
                self.button6.config(text="o")
            else:
                self.button6.config(text="x")
            self.player = not self.player
            self.used6 += 1
        else:
            pass

    def click7(self):
        if self.used7 == 0:
            if self.player == 0:
                self.button7.config(text="o")
            else:
                self.button7.config(text="x")
            self.player = not self.player
            self.used7 += 1
        else:
            pass

    def click8(self):
        if self.used8 == 0:
            if self.player == 0:
                self.button8.config(text="o")
            else:
                self.button8.config(text="x")
            self.player = not self.player
            self.used8 += 1
        else:
            pass

    def click9(self):
        if self.used9 == 0:
            if self.player == 0:
                self.button9.config(text="o")
            else:
                self.button9.config(text="x")
            self.player = not self.player
            self.used9 += 1
        else:
            pass

    def reset(self):
        self.button1.config(text="")
        self.button2.config(text="")
        self.button3.config(text="")
        self.button4.config(text="")
        self.button5.config(text="")
        self.button6.config(text="")
        self.button7.config(text="")
        self.button8.config(text="")
        self.button9.config(text="")
        self.used1 = 0
        self.used2 = 0
        self.used3 = 0
        self.used4 = 0
        self.used5 = 0
        self.used6 = 0
        self.used7 = 0
        self.used8 = 0
        self.used9 = 0
        # self.player = 0


window = Tk()
window.geometry("800x600")
window.title("Tic-tac-toe")

game = TicTacToe(master=window)

game.mainloop()
