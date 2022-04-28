
import tkinter as tk

class CharStatView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        statnames = ['STR', 'INT', 'DEX']
        self.labels = {}
        for stat in statnames:
            self.labels[stat] = tk.Label(self, text=stat + ': 1')
            self.labels[stat].pack()

    def update(self, statname, value):
        self.labels[statname]['text'] = f'{statname}: {value}'