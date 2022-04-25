from functools import partial
from os import path
import json
from tkinter import *
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = Tk()
window.geometry("600x300")
window.title("Shopping list")


def click(*args):
    if name.get() == 'Item name':
        name.set("")


def leave(*args):
    if name.get() != 'Item name' and name.get() != "":
        addButton.config(state=NORMAL)
    else:
        addButton.config(state=DISABLED)


def callback(input):
    return input.isdigit()


fig, ax = plt.subplots()


def show_stats():
    top = Toplevel(window)
    top.title("Shopping stats")
    top.geometry("600x600")
    canvas = FigureCanvasTkAgg(fig, top)
    generate_stats()
    canvas.get_tk_widget().pack(fill=BOTH, expand=YES)


def generate_stats():
    plt.cla()
    names = []
    sums = []
    for entry in entries:
        names.append(entry["name"])
        sums.append(entry["sum"])
    ax.bar(names, sums)

# TOOLBAR


toolbar = Frame(window)
toolbar.pack(side=BOTTOM, fill=X, padx=(0, 20))

name = StringVar(value="Item name")
nameWidget = Entry(toolbar, textvariable=name)
nameWidget.pack(side=LEFT, fill=X, expand=YES)

nameWidget.bind('<FocusIn>', click)
nameWidget.bind('<Leave>', leave)

entries = []
selected = []


def addEntry():
    entries.append({"id": random.random(), "price": price.get(
    ), "amount": amount.get(), "name": name.get(), "sum": price.get() * amount.get()})
    name.set("")
    update()


def delete_selected():
    global entries
    newEntries = []
    for entry in entries:
        if entry["id"] not in selected:
            newEntries.append(entry)
    entries = newEntries
    update()


amount = IntVar(value=1)
Scale(toolbar, variable=amount, orient=HORIZONTAL,
      showvalue=0, from_=1, to=10).pack(side=LEFT)
Label(toolbar, textvariable=amount).pack(side=LEFT)


price = IntVar(value=10)
reg = window.register(callback)
Spinbox(toolbar, textvariable=price, from_=1,
        to=1000000, increment=10, validate="key", validatecommand=(reg, '%P')).pack(side=LEFT)


addButton = Button(toolbar, text="Add", command=addEntry)
addButton.config(state=DISABLED)
addButton.pack(side=LEFT)

# MAIN AREA

frame = LabelFrame(window, text="Items")
frame.pack(side=TOP, fill=BOTH, expand=YES)

frameToolbar = Frame(frame)
frameToolbar.pack(fill=X)

Button(frameToolbar, text="Delete selected",
       command=delete_selected).pack(side=LEFT)
Button(frameToolbar, text="Stats", command=show_stats).pack(side=RIGHT)

# ITEMS

items = Frame(frame, bg="#102000")


def select(item, state):
    if state.get():
        selected.append(item)
    else:
        selected.remove(item)


def update():
    for item in items.pack_slaves():
        item.destroy()
    for entry in entries:
        line = Frame(items)
        selected = BooleanVar(value=False)
        checkButton = Checkbutton(
            line, variable=selected, onvalue=True, offvalue=False, command=partial(select, entry["id"], selected))
        checkButton.pack(side=LEFT)
        Label(line, text=entry["name"], anchor=W).pack(
            side=LEFT, fill=X, expand=YES)
        Label(line, text=str(entry["amount"])+"db", width=8).pack(side=LEFT)
        Label(line, text=str(entry["price"]) +
              "HUF/db", width=15).pack(side=LEFT)
        Label(line, text=str(entry["sum"]) + "HUF",
              anchor=E).pack(side=LEFT, fill=X, expand=YES)

        line.pack(fill=X)


items.pack(fill=BOTH, expand=YES)

# MENUBAR


def reset():
    global entries
    entries = []
    update()


def save_image():
    generate_stats()
    fig.savefig("image.png")


menubar = Menu(window, relief=FLAT)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Reset", command=reset)
filemenu.add_command(label="Save image", command=save_image)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
window.config(menu=menubar)

# CONTROLLER

if path.exists("list.json"):
    with open("list.json") as f:
        entries = json.load(f)
        update()

window.mainloop()

with open("list.json", "w") as f:
    json.dump(entries, f)
