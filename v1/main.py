#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

import cipher

class V001App:
    def __init__(self, master=None):
        # build ui
        self.mainWindow = ttk.Frame(master)
        self.mainWindow.configure(height=200, padding=10, width=200)
        self.textLabel = ttk.Label(self.mainWindow)
        self.textLabel.configure(text='Enter Text:')
        self.textLabel.grid(column=0, row=0)
        self.textEntry = ttk.Entry(self.mainWindow)
        self.textEntryVar = tk.StringVar()
        self.textEntry.configure(textvariable=self.textEntryVar)
        self.textEntry.grid(column=1, row=0)
        self.cipherButton = ttk.Button(self.mainWindow)
        self.cipherButton.configure(text='Cipher')
        self.cipherButton.grid(column=0, row=2)
        self.cipherButton.configure(command=self.cipher)
        self.cipherKeyLabel = ttk.Label(self.mainWindow)
        self.cipherKeyLabel.configure(text='Enter Cipher Key:')
        self.cipherKeyLabel.grid(column=0, row=1)
        self.cipherKeyEntry = ttk.Entry(self.mainWindow)
        self.cipherKeyEntryVar = tk.StringVar()
        self.cipherKeyEntry.configure(
            textvariable=self.cipherKeyEntryVar,
            validate="all")
        self.cipherKeyEntry.grid(column=1, row=1)
        _validatecmd = (self.cipherKeyEntry.register(self.validateText), "%P")
        self.cipherKeyEntry.configure(validatecommand=_validatecmd)
        self.resultText = tk.Message(self.mainWindow)
        self.resultText.configure(text='Result')
        self.resultText.grid(column=0, columnspan=2, row=3, rowspan=2)
        self.mainWindow.grid(column=0, row=0)

        # Main widget
        self.mainwindow = self.mainWindow

    def run(self):
        self.mainwindow.mainloop()

    def validateText(self, p_entry_value):
        try:
            if p_entry_value:
                int(p_entry_value)
            return True
        except:
            return False

    def cipher(self):
        text = self.textEntryVar.get()
        key = self.cipherKeyEntryVar.get()
        if key:
            key = int(key)
            result = cipher.cipher(text, key)
            self.resultText.configure(text=result)
        else:
            self.resultText.configure(text="Please enter a valid key to cipher.")


if __name__ == "__main__":
    root = tk.Tk()
    app = V001App(root)
    app.run()
