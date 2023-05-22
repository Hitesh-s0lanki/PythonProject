from tkinter import*
root=Tk()

string=""

def myfunc(event):
    global string
    text = event.widget.cget("text")
    if text=='C':
        newstring=""
        for j in range(len(string)):
            if j==len(string)-1:
                break
            newstring+=string[j]
        string=newstring
    else:
        string+=text
    valueBar.set(string)


def equate(event):
    global string
    try:
        string=eval(string)
        valueBar.set(string)
    except:
        valueBar.set("error")


Screen_width=320
Screen_height=450
root.geometry(f"{Screen_width}x{Screen_height}")
root.maxsize(Screen_width,Screen_height)
root.minsize(Screen_width,Screen_height)
valueBar=StringVar()
Entry(root,textvariable=valueBar,font=('None',30)).pack(fill=X)

frame1=Frame(root)
frame1.pack(anchor="nw")

b1=Button(frame1,text="7",font=('None',30))
b1.bind('<Button-1>',myfunc)
b1.grid(row=0,column=0,padx=10,pady=10)
#
b2=Button(frame1,text="8",font=('None',30))
b2.bind('<Button-1>',myfunc)
b2.grid(row=0,column=1,padx=10,pady=10)
#
b3=Button(frame1,text="9",font=('None',30))
b3.bind('<Button-1>',myfunc)
b3.grid(row=0,column=2,padx=10,pady=10)
#
b3=Button(frame1,text="/",font=('None',30))
b3.bind('<Button-1>',myfunc)
b3.grid(row=0,column=3,padx=10,pady=10)
#
b4=Button(frame1,text="4",font=('None',30))
b4.bind('<Button-1>',myfunc)
b4.grid(row=1,column=0,padx=10,pady=10)
#
b5=Button(frame1,text="5",font=('None',30))
b5.bind('<Button-1>',myfunc)
b5.grid(row=1,column=1,padx=10,pady=10)
#
b6=Button(frame1,text="6",font=('None',30))
b6.bind('<Button-1>',myfunc)
b6.grid(row=1,column=2,padx=10,pady=10)
#
b7=Button(frame1,text="*",font=('None',30))
b7.bind('<Button-1>',myfunc)
b7.grid(row=1,column=3,padx=10,pady=10)
#
b8=Button(frame1,text="1",font=('None',30))
b8.bind('<Button-1>',myfunc)
b8.grid(row=2,column=0,padx=10,pady=10)
#
b9=Button(frame1,text="2",font=('None',30))
b9.bind('<Button-1>',myfunc)
b9.grid(row=2,column=1,padx=10,pady=10)
#
b0=Button(frame1,text="3",font=('None',30))
b0.bind('<Button-1>',myfunc)
b0.grid(row=2,column=2,padx=10,pady=10)
#
b11=Button(frame1,text="-",font=('None',30))
b11.bind('<Button-1>',myfunc)
b11.grid(row=2,column=3,padx=10,pady=10)
#
b80=Button(frame1,text="0",font=('None',30))
b80.bind('<Button-1>',myfunc)
b80.grid(row=3,column=0,padx=10,pady=10)
#
b90=Button(frame1,text="C",font=('None',30))
b90.bind('<Button-1>',myfunc)
b90.grid(row=3,column=1,padx=10,pady=10)
#
b01=Button(frame1,text="+",font=('None',30))
b01.bind('<Button-1>',myfunc)
b01.grid(row=3,column=2,padx=10,pady=10)
#
b110=Button(frame1,text="=",font=('None',30))
b110.bind('<Button-1>',equate)
b110.grid(row=3,column=3)
#
root.mainloop()