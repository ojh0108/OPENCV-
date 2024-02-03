import tkinter
from math import *

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x480+100+100")
window.resizable(False, False)

def calc():
    label.config(text="결과="+str(eval(entry.get())))

entry=tkinter.Entry(window)
#entry.bind("<Return>", calc)
entry.pack()

# 버튼을 하나 만들고 위에 함수를 실행 하도록 하기 

button = tkinter.Button(window, overrelief="solid", width=15, command=calc, repeatdelay=1000, repeatinterval=100)
button.pack()

label=tkinter.Label(window)
label.pack()

window.mainloop()