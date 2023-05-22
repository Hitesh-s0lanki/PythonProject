from tkinter import*
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

root=Tk()
def cut():
    text.event_generate(("<<Cut>>"))

def copy():
    text.event_generate(("<<Copy>>"))

def paste():
    text.event_generate(("<<Paste>>"))

def new():
    global file
    root.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)


def open():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()

def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()





root.geometry('600x400')
root.title("Untitled - Notepad")
file=None

#Scroll Bar
Scroll=Scrollbar(root)
Scroll.pack(side=RIGHT,fill=Y)

#textArea
text=Text(root,font=('lucida',13),yscrollcommand=Scroll)
text.pack(fill="both",expand=True)
Scroll.config(command=text.yview)

#MenuBar
MenuBar=Menu(root)

fileMenu=Menu(MenuBar,tearoff=0)
fileMenu.add_command(label="Open",command=open)
fileMenu.add_command(label="Save",command=save)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)
MenuBar.add_cascade(label="File",menu=fileMenu)

editMenu=Menu(MenuBar,tearoff=0)
editMenu.add_command(label="cut",command=cut)
editMenu.add_command(label="copy",command=copy)
editMenu.add_command(label="paste",command=paste)
MenuBar.add_cascade(label="Edit",menu=editMenu)


root.config(menu=MenuBar)

root.mainloop()