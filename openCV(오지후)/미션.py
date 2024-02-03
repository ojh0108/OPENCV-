import tkinter as tk
import tkinter.font as tk_font
import main
import tkinter

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("Grid of Buttons")
root.geometry("640x400+100+100")
root.resizable(False, False)

font = tk_font.Font(family="맑은 고딕" , size=20)
def 얼굴인식(s):
    if s == "얼굴인식":
      main.face()
    else:
        print("아직 미완")

# 2x2 격자의 버튼 생성
arr = [["얼굴인식","고양이얼굴인식"] , ["body인식" , "손인식"]]
for row in range(2):
    for col in range(2):
        button = tk.Button(root, text=arr[row][col], font = font , command= lambda i = arr[row][col] : 얼굴인식(i))
        button.grid(row=row, column=col, padx=30, pady=30)

        
# 윈도우 실행
root.mainloop()