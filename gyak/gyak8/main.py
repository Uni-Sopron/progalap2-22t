from tkinter import *

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


def show_stats():
    print('clicked stats')
    top = Toplevel(window)
    top.title("Shopping stats")
    top.geometry("600x600")
    Label(top, text="valami").pack()


# TOOLBAR

toolbar = Frame(window)
toolbar.pack(side=BOTTOM, fill=X, padx=(0, 20))

name = StringVar(value="Item name")
nameWidget = Entry(toolbar, textvariable=name)
nameWidget.pack(side=LEFT, fill=X, expand=YES)

nameWidget.bind('<FocusIn>', click)
nameWidget.bind('<Leave>', leave)


amount = IntVar(value=1)
Scale(toolbar, variable=amount, orient=HORIZONTAL,
      showvalue=0, from_=1, to=10).pack(side=LEFT)
Label(toolbar, textvariable=amount).pack(side=LEFT)


price = IntVar(value=10)
reg = window.register(callback)
Spinbox(toolbar, textvariable=price, from_=1,
        to=1000000, increment=10, validate="key", validatecommand=(reg, '%P')).pack(side=LEFT)


addButton = Button(toolbar, text="Add", command=print)
addButton.config(state=DISABLED)
addButton.pack(side=LEFT)

# MAIN AREA

frame = LabelFrame(window, text="Items")
frame.pack(side=TOP, fill=BOTH, expand=YES)

frameToolbar = Frame(frame)
frameToolbar.pack(fill=X)

Button(frameToolbar, text="Delete selected", command=print).pack(side=LEFT)
Button(frameToolbar, text="Stats", command=show_stats).pack(side=RIGHT)

# ITEMS

items = Frame(frame, bg="#102000")
for i in range(4):
    Label(items, text='Demo').pack()

items.pack(fill=BOTH, expand=YES)

# MENUBAR

menubar = Menu(window, relief=FLAT)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Reset", command=print)
filemenu.add_command(label="Save image", command=print)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)
window.config(menu=menubar)

# CONTROLLER

window.mainloop()
