import tkinter as tk
import random

window = tk.Tk()

window.title("간단게임")
window.geometry("600x600")


canvas=tk.Canvas(window , width=500, height=500, bg="white")

canvas.pack()


ball = canvas.create_oval(100, 100, 210, 210, fill="blue")



점수 = 0

def 공만들기():
  x = random.randint(20,480)
  y = random.randint(20,480)
  b1 = canvas.create_oval(x, y, x+20, y+20, fill="red")
  return b1

b1 = 공만들기()

def 충돌():
    global 점수
    주인공위치 = canvas.coords(ball)
    먹이 = canvas.coords(b1)
    if (주인공위치[1] <= 먹이[1] <= 주인공위치[3]) and (주인공위치[0] <= 먹이[0] <= 주인공위치[2]):
      점수 += 10
      label.config(text =f"점수 : {점수}")
      canvas.delete(b1)
      
def move_up(event):
  canvas.move(ball , 0, -10)
  충돌()

def move_down(event):
  canvas.move(ball , 0, 10)
  충돌()
def move_left(event):
  canvas.move(ball , -10, 0)
  충돌()
def move_right(event):
  canvas.move(ball , 10, 0)
  충돌()


window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)


label = tk.Label(window , text = "점수")
label.pack()

window.mainloop()