from tkinter import *
import os

def restartFunc():
    os.system("shutdown /r /t 60")
def LogFunc():
    os.system("shutdown -l")
def ShutDownFunc():
    os.system("shutdown /s /t 1")


st=Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.configure(bg="blue")

RestartButton=Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restartFunc)
RestartButton.place(x=150,y=60,height=50,width=200)

LogButton=Button(st,text="Log Out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=LogFunc)
LogButton.place(x=150,y=160,height=50,width=200)
st.mainloop()