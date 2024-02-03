import tkinter
import tkinter.font as tk_font

window=tkinter.Tk()
window.title("test")
window.geometry("640x400+100+100")
window.resizable(False, False)

font = tk_font.Font(family="맑은 고딕" , size=20)

entry=tkinter.Entry(window , font = font)
entry.pack()

import 외부함수

label = tkinter.Label(window , text = "결과1" ,font = font)
label.pack()

button = tkinter.Button(window , text = "실행" , command = lambda : 외부함수.enle(entry, label) , font = font  )
button.pack()

window.mainloop()