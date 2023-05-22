#IDE
import os
from tkinter import*
import subprocess

language=".txt"
string=""
def Selectcpp():
    global language
    language=".cpp"
    global string
    string='''#include<iostream>\nusing namespace std;\nint main(){\ncout<<"hello World"<<endl;\n}'''
    text1.insert(END,string)
def Selectpy():
    global language
    language=".py"
    global string
    string='''print("hello")'''
    text1.insert(END,string)
def Selectc():
    global language
    language=".c" 
    global string
    string='''#include<stdio.h>\nint main(){\nprintf("hello World");\n}'''
    text1.insert(END,string)
def printLang():
    global language
    print(language)
    print(text1.get(1.0, END))


def RunProgram():
    Output.delete(0.1,"end")
    with open(f"Runner{language}",'w') as f:
        f.write(text1.get(1.0, END))
    loc=os.getcwd()
    if language==".cpp"or language==".c":
        try:
            subprocess.call(f"cd {loc}",shell=True)
            subprocess.check_output(["g++",f"Runner{language}","-o","Runner.exe"])
            out=subprocess.check_output([".\Runner.exe"])
            out=out.decode('utf-8')
            Output.insert(END,out)

            os.remove(f"Runner{language}")
            os.remove(f"Runner.exe")
        except Exception as e:
            Output.insert(END,e)
    elif language==".py":
        try:
            subprocess.call(f"cd {loc}",shell=True)
            out=subprocess.check_output(["python","Runner.py"])
            out=out.decode('utf-8')
            Output.insert(END,out)

            os.remove(f"Runner{language}")
        except Exception as e:
            Output.insert(END,e)






root=Tk()
root.geometry('600x600')
#Menu part
MainMenu=Menu(root)
m1=Menu(MainMenu,tearoff=0)
m1.add_command(label="Cpp",command=Selectcpp)
m1.add_command(label="Python",command=Selectpy)
m1.add_command(label="C",command=Selectc)
m1.add_command(label="print",command=printLang)
MainMenu.add_cascade(label="Select",menu=m1)
root.config(menu=MainMenu)

frame1=Frame(root,height=400,width=580,borderwidth=3, relief="sunken",pady=10)
frame1.pack()
frame1.config(bg="red")

text1=Text(frame1,font=("Helvetica",10))
text1.pack(fill=BOTH,expand=True)

frame2=Frame(root,height=170,width=580,borderwidth=3, relief="sunken",pady=10)
frame2.pack()
frame2.config(bg="blue")

Button(frame2,text="Run",command=RunProgram).pack()
Output=Text(frame2,font=("Helvetica",10))
Output.pack(fill=BOTH,expand=True)

root.mainloop()

# #include<iostream>
# using namespace std;
# int main(){
# cout<<"hello wolrd";
# }