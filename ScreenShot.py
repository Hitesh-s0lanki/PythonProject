import pyscreenshot
from tkinter import *

sk=Tk()
sk.title('screenshot')
def takeShot():
    pyscreenshot.grab().save("new.png")
button=Button(sk,text="Take shot",font=('digital-ds,20'),command=takeShot)
button.pack(anchor="center")

sk.mainloop()