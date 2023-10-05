#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

import cipher

class V011App:
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

        self.cipherKeyLabel = ttk.Label(self.mainWindow)
        self.cipherKeyLabel.configure(text='Enter Cipher Key A:')
        self.cipherKeyLabel.grid(column=0, row=1)

        self.cipherKeyEntry = ttk.Entry(self.mainWindow)
        self.cipherKeyEntryVar = tk.StringVar()
        self.cipherKeyEntry.configure(textvariable=self.cipherKeyEntryVar)
        self.cipherKeyEntry.grid(column=1, row=1)

        self.cipherKey2Label = ttk.Label(self.mainWindow)
        self.cipherKey2Label.configure(text='Enter Cipher Key B:')
        self.cipherKey2Label.grid(column=2, row=1)

        self.cipherKey2Entry = ttk.Entry(self.mainWindow)
        self.cipherKey2EntryVar = tk.StringVar()
        self.cipherKey2Entry.configure(textvariable=self.cipherKey2EntryVar)
        self.cipherKey2Entry.grid(column=3, row=1)

        self.cipherButton = ttk.Button(self.mainWindow)
        self.cipherButton.configure(text='Cipher')
        self.cipherButton.grid(column=0, row=2)
        self.cipherButton.configure(command=self.cipher)

        self.cipherTypeVar = tk.StringVar(value='Ceaser')

        __values = ['Ceaser', 'Railfence', 'Affine']
        self.cipherOption = ttk.OptionMenu(
            self.mainWindow,
            self.cipherTypeVar,
            "Ceaser",
            *__values,
            command=None)
        self.cipherOption.grid(column=1, row=2)

        self.decipherButton = ttk.Button(self.mainWindow)
        self.decipherButton.configure(text='Decipher')
        self.decipherButton.grid(column=2, row=2)
        self.decipherButton.configure(command=self.decipher)

        self.resultText = tk.Message(self.mainWindow)
        self.resultText.configure(text='Result', width=200)
        self.resultText.grid(column=0, columnspan=2, row=3, rowspan=2)

        self.crackButton = ttk.Button(self.mainWindow)
        self.crackButton.configure(text='Crack')
        self.crackButton.grid(column=3, row=2)
        self.crackButton.configure(command=self.crack)

        self.mainWindow.grid(column=0, row=0)

        # Main widget
        self.mainwindow = self.mainWindow

    def run(self):
        self.mainwindow.mainloop()

    def crack(self):
        import crack
        
        text = self.textEntryVar.get()

        for i in crack.crack(text):
            i = i[1]
            # print(mostLikely)
            score, key = list(i[1].items())[0]
            detext = i[0]
            print(f"Key: {key}, Deciphered: {detext}")
        
        return

    def validateText(self, p_entry_value):
        try:
            if p_entry_value:
                int(p_entry_value)
            return True
        except:
            return False

    def cipher(self):
        try:
            _type = self.cipherTypeVar.get()
            text = self.textEntryVar.get()
            key = self.cipherKeyEntryVar.get()
            # if not key:
            #     raise TypeError
            
            key2 = self.cipherKey2EntryVar.get()
            # if not key2:
            #     raise TypeError
            
            result = cipher.cipher(text, key, key2, _type)
            print(f'Ciphered: {text}, result: {result}, ciphertype: {_type}, key a: {key}, key b: {key2}')

            if not result:
                raise TypeError
            
            self.resultText.configure(text=result)
        except TypeError:
            self.resultText.configure(text="Please enter a valid key to cipher.")

    def decipher(self):
        try:
            _type = self.cipherTypeVar.get()
            text = self.textEntryVar.get()
            key = self.cipherKeyEntryVar.get()
            # if not key:
            #     raise TypeError
            
            key2 = self.cipherKey2EntryVar.get()
            # if not key2:
            #     raise TypeError
            
            result = cipher.decipher(text, key, key2, _type)
            print(f'Deciphered: {text}, result: {result}, ciphertype: {_type}, key a: {key}, key b: {key2}')

            if not result:
                raise TypeError
            
            self.resultText.configure(text=result)
        except TypeError:
            self.resultText.configure(text="Please enter a valid key to decipher.")


if __name__ == "__main__":
    root = tk.Tk()
    app = V011App(root)
    app.run()
