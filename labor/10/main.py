
from charactermodel import CharacterModel
from charstatview import CharStatView
from controller import Controller

import tkinter as tk

model = CharacterModel('Adam')
window = tk.Tk()
window.geometry('250x180')
window.title('Character stats')
view = CharStatView(window)
view.pack()
c = Controller(model, view)
c.setstat('INT', 100)

window.mainloop()
