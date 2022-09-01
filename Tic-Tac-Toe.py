## Importing tkinter for the gui
import tkinter as tk

## setting root as tk.TK
root = tk.Tk()

## adding varibles
box1var = tk.StringVar()
box2var = tk.StringVar()
box3var = tk.StringVar()
box4var = tk.StringVar()
box5var = tk.StringVar()
box6var = tk.StringVar()
box7var = tk.StringVar()
box8var = tk.StringVar()
box9var = tk.StringVar()
butttext = tk.StringVar()

## setting buttons
butttext.set("X")

## setting definitions
def butt1cmd():
    if butttext.get() == "X":
        if box1var.get() == "X":
            print("invalid move")
        elif box1var.get() == "O":
            print("Invalid move")
        else:
            box1var.set("X")
            butttext.set("O")
    elif butttext.get() == "O":
        if box1var.get() == "X":
            print("Invalid move")
        elif box1var.get() == "O":
            print("Invalid move")
        else:
            box1var.set("O")
            butttext.set("X")


def butt2cmd():
    if butttext.get() == "X":
        if box2var.get() == "X":
            print("invalid move")
        elif box2var.get() == "O":
            print("Invalid move")
        else:
            box2var.set("X")
            butttext.set("O")
    elif butttext.get() == "O":
        if box2var.get() == "X":
            print("Invalid move")
        elif box2var.get() == "O":
            print("Invalid move")
        else:
            box2var.set("O")
            butttext.set("X")


def butt3cmd():
    if butttext.get() == "X":
        if box3var.get() == "X":
            print("invalid move")
        elif box3var.get() == "O":
            print("Invalid move")
        else:
            box3var.set("X")
            butttext.set("O")
    elif butttext.get() == "O":
        if box3var.get() == "X":
            print("Invalid move")
        elif box3var.get() == "O":
            print("Invalid move")
        else:
            box3var.set("O")
            butttext.set("X")


def butt4cmd():
    if butttext.get() == "X":
        if box4var.get() == "X":
            print("invalid move")
        elif box4var.get() == "O":
            print("Invalid move")
        else:
            box4var.set("X")
            butttext.set("O")
    elif butttext.get() == "O":
        if box4var.get() == "X":
            print("Invalid move")
        elif box4var.get() == "O":
            print("Invalid move")
        else:
            box4var.set("O")
            butttext.set("X")


def butt5cmd():
    if butttext.get() == "X":
        if box5var.get() == "X":
            print("invalid move")
        elif box5var.get() == "O":
            print("Invalid move")
        else:
            box5var.set("X")
            butttext.set("O")
    elif butttext.get() == "O":
        if box5var.get() == "X":
            print("Invalid move")
        elif box5var.get() == "O":
            print("Invalid move")
        else:
            box5var.set("O")
            butttext.set("X")


def butt6cmd():
    if butttext.get() == "X":
        if box6var.get() == "X":
            print("invalid move")
        elif box6var.get() == "O":
            print("Invalid move")
        else:
            box6var.set("X")
            butttext.set("O")
    elif butttext.get() == "O":
        if box6var.get() == "X":
            print("Invalid move")
        elif box6var.get() == "O":
            print("Invalid move")
        else:
            box6var.set("O")
            butttext.set("X")


def butt7cmd():
    if butttext.get() == "X":
        if box7var.get() == "X":
            print("invalid move")
        elif box7var.get() == "O":
            print("Invalid move")
        else:
            box7var.set("X")
            butttext.set("O")
    elif butttext.get() == "O":
        if box7var.get() == "X":
            print("Invalid move")
        elif box7var.get() == "O":
            print("Invalid move")
        else:
            box7var.set("O")
            butttext.set("X")


def butt8cmd():
    if butttext.get() == "X":
        if box8var.get() == "X":
            print("invalid move")
        elif box8var.get() == "O":
            print("Invalid move")
        else:
            box8var.set("X")
            butttext.set("O")
    elif butttext.get() == "O":
        if box8var.get() == "X":
            print("Invalid move")
        elif box8var.get() == "O":
            print("Invalid move")
        else:
            box8var.set("O")
            butttext.set("X")


def butt9cmd():
    if butttext.get() == "X":
        if box9var.get() == "X":
            print("invalid move")
        elif box9var.get() == "O":
            print("Invalid move")
        else:
            box9var.set("X")
            butttext.set("O")
    elif butttext.get() == "O":
        if box9var.get() == "X":
            print("Invalid move")
        elif box9var.get() == "O":
            print("Invalid move")
        else:
            box9var.set("O")
            butttext.set("X")


def clrcmd():
    box1var.set("")
    box2var.set("")
    box3var.set("")
    box4var.set("")
    box5var.set("")
    box6var.set("")
    box7var.set("")
    box8var.set("")
    box9var.set("")

## seting frame
frame = tk.Frame(root, height=120, width=100)
## setting lable
box1 = tk.Label(root, height=1, width=5, textvariable=box1var)
box1.place(y=0, x=0)
box2 = tk.Label(root, height=1, width=5, textvariable=box2var)
box2.place(y=0, x=30)
box3 = tk.Label(root, height=1, width=5, textvariable=box3var)
box3.place(y=0, x=60)
box4 = tk.Label(root, height=1, width=5, textvariable=box4var)
box4.place(y=20, x=0)
box5 = tk.Label(root, height=1, width=5, textvariable=box5var)
box5.place(y=20, x=30)
box6 = tk.Label(root, height=1, width=5, textvariable=box6var)
box6.place(y=20, x=60)
box7 = tk.Label(root, height=1, width=5, textvariable=box7var)
box7.place(y=40, x=0)
box8 = tk.Label(root, height=1, width=5, textvariable=box8var)
box8.place(y=40, x=30)
box9 = tk.Label(root, height=1, width=5, textvariable=box9var)
box9.place(y=40, x=60)
## setting buttons and displaying
butt1 = tk.Button(root, height=1, width=2, textvariable=butttext, command=butt1cmd)
butt1.place(y=60, x=0)
butt2 = tk.Button(root, height=1, width=2, textvariable=butttext, command=butt2cmd)
butt2.place(y=60, x=40)
butt3 = tk.Button(root, height=1, width=2, textvariable=butttext, command=butt3cmd)
butt3.place(y=60, x=80)
butt4 = tk.Button(root, height=1, width=2, textvariable=butttext, command=butt4cmd)
butt4.place(y=90, x=0)
butt5 = tk.Button(root, height=1, width=2, textvariable=butttext, command=butt5cmd)
butt5.place(y=90, x=40)
butt6 = tk.Button(root, height=1, width=2, textvariable=butttext, command=butt6cmd)
butt6.place(y=90, x=80)
butt7 = tk.Button(root, height=1, width=2, textvariable=butttext, command=butt7cmd)
butt7.place(y=120, x=0)
butt8 = tk.Button(root, height=1, width=2, textvariable=butttext, command=butt8cmd)
butt8.place(y=120, x=40)
butt9 = tk.Button(root, height=1, width=2, textvariable=butttext, command=butt9cmd)
butt9.place(y=120, x=80)

clr = tk.Button(root, height=1, width=5, text="CLR", command=clrcmd)
clr.place(y=150, x=20)


root.mainloop()
