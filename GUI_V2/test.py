from tkinter import *
from tkinter import ttk
import subprocess # 바로 python 실행하기 위해서 사용

def button_pressed(value):
    number_entry.insert("end",value)
    if value =='AC':
        number_entry.delete(0,'end')
    print(value,"pressed")
def insertNum_on():
    number =int(number_entry.get())
    print(number)
    subprocess.call('python3 DB_open.py {}'.format(number) ,shell=True)
def insertNum_off():
    number =int(number_entry.get())
    print(number)
    subprocess.call('python3 DB_close.py {}'.format(number) ,shell=True)

def DBcheck():
    number = int(number_entry.get())
    print(number)
    subprocess.call('python barcode_scanner_viedo.py {}'.format(number) ,shell=True)

def DBdel():
    number =int(number_entry.get())
    print(number)
    subprocess.call('python delete_scanner.py {}'.format(number),shell=True)

def camera():
    subprocess.call('python b.py',shell=True)
subprocess.call('gpio -g mode 21 out',shell=True)  #GPIo 21 번을 출력으르로 사용 
subprocess.call('gpio -g mode 26 out',shell=True) #전원 역활
subprocess.call('gpio -g write 26 1',shell=True) 
root = Tk()
root.title("비밀번호를 입력하시오")
root.geometry("650x600")  # 버튼폭에 맞춰서 확장.
root.grid_rowconfigure(0,weight=3)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)
root.grid_rowconfigure(3,weight=1)
root.grid_rowconfigure(4,weight=2)
root.grid_rowconfigure(5,weight=2)
entry_value = StringVar(root, value='')
 
number_entry = ttk.Entry(root,font = "Helvetica 30 bold", textvariable = entry_value, width=10)
number_entry.grid(row=0, columnspan=7,sticky="nsew") #columnspan 은 여러칸에 걸쳐서 표시함.

# button 15개 추가
button_Delete = ttk.Button(root, text="Delete", command = lambda:button_pressed('AC'))
button_Delete.grid(row=5, column=0,sticky="nsew")
button2 = ttk.Button(root, text="Check_out", command = DBdel)
button2.grid(row=5, column=1,sticky="nsew")
button3 = ttk.Button(root, text="Camera", command = camera)
button3.grid(row=5, column=2,sticky="nsew")
button_ON = ttk.Button(root, text="ON", command = insertNum_on)
button_ON.grid(row=4, column=0,sticky="nsew")
button_OFF = ttk.Button(root, text="OFF", command = insertNum_off)
button_OFF.grid(row=4, column=1,sticky="nsew")
button_Check = ttk.Button(root, text="Check_in", command = DBcheck)
button_Check.grid(row=4, column=2,sticky="nsew")

button7 = ttk.Button(root, text="7", command = lambda:button_pressed('7'))
button7.grid(row=1, column=0,sticky="nsew")
button8 = ttk.Button(root, text="8", command = lambda:button_pressed('8'))
button8.grid(row=1, column=1,sticky="nsew")
button9 = ttk.Button(root, text="9", command = lambda:button_pressed('9'))
button9.grid(row=1, column=2,sticky="nsew")
 
button4 = ttk.Button(root, text="4", command = lambda:button_pressed('4'))
button4.grid(row=2, column=0,sticky="nsew")
button5 = ttk.Button(root, text="5", command = lambda:button_pressed('5'))
button5.grid(row=2, column=1,sticky="nsew")
button6 = ttk.Button(root, text="6", command = lambda:button_pressed('6'))
button6.grid(row=2, column=2,sticky="nsew")
 
button1 = ttk.Button(root, text="1", command = lambda:button_pressed('1'))
button1.grid(row=3, column=0,sticky="nsew")
button2 = ttk.Button(root, text="2", command = lambda:button_pressed('2'))
button2.grid(row=3, column=1,sticky="nsew")
button3 = ttk.Button(root, text="3", command = lambda:button_pressed('3'))
button3.grid(row=3, column=2,sticky="nsew")
 
root.mainloop()
# Connection 닫기
