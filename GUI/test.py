from tkinter import *
from tkinter import ttk
import subprocess
def insertNum_on():
    txt.insert(100, "On")
    subprocess.call('gpio -g write 21 1',shell=True)
def insertNum_off():
    txt.insert(100, "Off")
    subprocess.call('gpio -g write 21 0',shell=True)
def Camera():
    subprocess.call('python camera_test.py',shell=True)

subprocess.call('gpio -g mode 21 out',shell=True)

root = Tk()
root.title("Title")
root.geometry("300x200")
 
txt = Entry(root, width=15)
txt.place(x = 150, y = 15, anchor=CENTER)
 
btn1 = Button(root, text="On", command=insertNum_on)
btn1.place(x= 32, y = 120)

btn2 = Button(root, text="Off", command=insertNum_off)
btn2.place(x= 130, y= 120)

btn3 = Button(root, text ="Camera",command=Camera)
btn3.place(x=80,y=60)
root.mainloop()
