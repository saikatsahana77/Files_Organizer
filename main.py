import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from organize import Organize


def his_load():
    try:
        with open("history.txt", "r") as f:
            label["text"] = f.readline()
    except:
        label["text"] = ""


def select():
    folder_selected = filedialog.askdirectory()
    if(folder_selected != ""):
        label["text"] = folder_selected
        btn3["state"] = tk.NORMAL
        btn3.bind("<Enter>", entered3)
        btn3.bind("<Leave>", left3)


def delete():
    label["text"] = ""
    btn3["state"] = tk.DISABLED
    btn3.unbind("<Enter>", entered3)
    btn3.unbind("<Leave>", left3)

def organize():
    Organize(label["text"].replace("/","//"))


def entered1(event):
    btn1.configure(
        bg="#343434",
        fg="#ffffff",
    )


def left1(event):
    btn1.configure(
        bg="#ffffff",
        fg="#000000",
    )


def entered2(event):
    btn2.configure(
        bg="#343434",
        fg="#ffffff",
    )


def left2(event):
    btn2.configure(
        bg="#ffffff",
        fg="#000000",
    )


def entered3(event):
    btn3.configure(
        bg="#343434",
        fg="#ffffff",
    )


def left3(event):
    btn3.configure(
        bg="#ffffff",
        fg="#000000",
    )


def save_his():
    with open("history.txt", "w") as f:
        f.write(label["text"])
    root.destroy()


root = tk.Tk()
root.title('File Organizer')
root.iconbitmap('./icon.ico')
root.geometry("400x200")
root.resizable(0, 0)

canvas = tk.Canvas(root, width=400, height=400, bg="#070769")
canvas.create_text(200, 30, fill="white", font="Arial 15 bold",
                   text="Organize Files In Just One Click!!")
label = tk.Label(root, width=50, bg="#fff", text="", relief=tk.RAISED)
label.place(x=25, y=80)
his_load()
canvas.pack(expand=True, fill=tk.BOTH)
btn1 = tk.Button(canvas, text="Choose Folder",
                 font='Arial 12 bold', command=select, padx=5, pady=3)
btn1.place(x=25, y=140)
btn2 = tk.Button(canvas, text="Clear", font='Arial 12 bold',
                 command=delete, padx=5, pady=3)
btn2.place(x=170, y=140)
if label["text"] == "":
    btn3 = tk.Button(canvas, text="Organize Files!",
                     font='Arial 12 bold', state=tk.DISABLED, command=organize, padx=5, pady=3)
else:
    btn3 = tk.Button(canvas, text="Organize Files!",
                     font='Arial 12 bold', state=tk.NORMAL, command=organize, padx=5, pady=3)
    btn3.bind("<Enter>", entered3)
    btn3.bind("<Leave>", left3)
btn3.place(x=240, y=140)
btn1.bind("<Enter>", entered1)
btn1.bind("<Leave>", left1)
btn2.bind("<Enter>", entered2)
btn2.bind("<Leave>", left2)
root.protocol("WM_DELETE_WINDOW", save_his)
root.mainloop()
