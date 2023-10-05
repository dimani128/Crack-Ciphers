#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
import sys
import threading

class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        frame1 = ttk.Frame(master)
        frame1.configure(height=200, padding=20, width=200)
        label1 = ttk.Label(frame1)
        label1.configure(padding=20, text="By clicking 'I agree' to the terms and conditions, you hereby acknowledge your simultaneous commitment to not acknowledging the existence of said terms and conditions, rendering your agreement null and void, yet binding you to the act of rendering your agreement null and void, which is in itself a form of agreement. Please agree to disagree to the terms and conditions, but also agree to agree to disagree, so that you can simultaneously agree and disagree while agreeing to not agree, which ultimately results in a state of perpetual paradoxical non-agreement. Thank you for your understanding.", wraplength=500)
        label1.grid(column=0, columnspan=3, row=0)
        button1 = ttk.Button(frame1)
        button1.configure(text='Agree')
        button1.grid(column=0, row=1)
        button1.configure(command=self.agree)
        button2 = ttk.Button(frame1)
        button2.configure(text='Refuse to Answer')
        button2.grid(column=1, row=1)
        button2.configure(command=self.refuse)
        button3 = ttk.Button(frame1)
        button3.configure(text='Disagree')
        button3.grid(column=2, row=1)
        button3.configure(command=self.disagree)
        frame1.grid(column=0, row=0)
        frame1.bind("<Destroy>", self.refuse, add="")

        # Main widget
        self.mainwindow = frame1

    def run(self, *args, **kwargs):
        self.mainwindow.mainloop()

    def agree(self, *args, **kwargs):
        sys.exit(0)

    def refuse(self, *args, **kwargs):
        for i in range(3):
            th = threading.Thread(target=main)
            th.start()

    def disagree(self, *args, **kwargs):
        sys.exit(0)

def main():
    root = tk.Tk()
    app = NewprojectApp(root)
    app.run()

if __name__ == "__main__":
    main()