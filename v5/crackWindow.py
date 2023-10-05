#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk

class CrackProgress(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(CrackProgress, self).__init__(master, **kw)
        self.TitleLabel = ttk.Label(self)
        self.TitleLabel.configure(text='Cracking...')
        self.TitleLabel.grid(column=0, row=0)
        self.TotalBar = ttk.Progressbar(self)
        self.TotalBarValue = tk.IntVar()
        self.TotalBar.configure(
            mode="determinate",
            variable=self.TotalBarValue)
        self.TotalBar.grid(column=0, row=1)
        self.CeaserBarLabel = ttk.Label(self)
        self.CeaserBarLabel.configure(text='Ceaser')
        self.CeaserBarLabel.grid(column=0, row=2)
        self.CeaserBar = ttk.Progressbar(self)
        self.CeaserBarValue = tk.IntVar()
        self.CeaserBar.configure(
            mode="determinate",
            variable=self.CeaserBarValue)
        self.CeaserBar.grid(column=0, row=3)
        self.RailfenceBarLabel = ttk.Label(self)
        self.RailfenceBarLabel.configure(text='Railfence')
        self.RailfenceBarLabel.grid(column=0, row=4)
        self.RailfenceBar = ttk.Progressbar(self)
        self.RailfenceBarValue = tk.IntVar()
        self.RailfenceBar.configure(
            mode="determinate",
            variable=self.RailfenceBarValue)
        self.RailfenceBar.grid(column=0, row=5)
        self.configure(height=200, padding=10, width=200)
        self.grid(column=0, row=0)