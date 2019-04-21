'''import tkinter
import math
import datetime

C_width, C_height = 500, 500


def Redraw():
    Clock.delete("all")
    for i in range(60):
        angle = -6 * i * math.pi / 180
        if i % 5 == 0:
            L_p = 185
        else:
            L_p = 200
        Clock.create_line(L_p * math.cos(angle) + 250, L_p * math.sin(angle) + 250, 230 * math.cos(angle) + 250,
                          230 * math.sin(angle) + 250, fill="black")
    time = datetime.datetime.now()
    hour = time.hour
    minu = time.minute
    sec = time.second
    angle_h = -math.pi * 0.5 + 30 * (hour % 12) * math.pi / 180 + 0.5 * minu * math.pi / 180
    angle_m = -math.pi * 0.5 + 6 * minu * math.pi / 180 + 6 * sec * math.pi / 180 / 60
    angle_s = -math.pi * 0.5 + 6 * sec * math.pi / 180

    Clock.create_line(250, 250, 140 * math.cos(angle_h) + 250, 140 * math.sin(angle_h) + 250, width=4)
    Clock.create_line(250, 250, 175 * math.cos(angle_m) + 250, 175 * math.sin(angle_m) + 250, width=2)
    Clock.create_line(250, 250, 175 * math.cos(angle_s) + 250, 175 * math.sin(angle_s) + 250)
    Clock.after(1000, Redraw)


Screen = tkinter.Tk()
Screen.title("Clock")
Clock = tkinter.Canvas(Screen, width=C_width, height=C_height)
Clock.pack()
Redraw()
Screen.mainloop()'''

'''import turtle
import tkinter as tk

WIDTH = 500
HEIGHT = 500


class MyTurtle(turtle.RawTurtle):
    def __init__(self, canvas):
        super(MyTurtle, self).__init__(canvas)
        self.shape("turtle")
        self.shapesize(2, 2)
        self.getscreen().bgcolor("yellow")

        self.center_offset_x = WIDTH / 2
        self.center_offset_y = HEIGHT / 2

        canvas.bind("<Button-1>", self.on_mouse_clicked)

        self.is_moving = False

    def on_mouse_clicked(self, event):
        if self.acquire_lock():
            x = event.x - self.center_offset_x
            y = -(event.y - self.center_offset_y)

            print("clicked ({0}, {1})".format(x, y))
            self.goto(x, y)

            self.release_lock()

    def acquire_lock(self):
        if self.is_moving is True:
            return False

        self.is_moving = True
        return True

    def release_lock(self):
        self.is_moving = False


root = tk.Tk()
canvas = tk.Canvas(master=root, width=WIDTH, height=HEIGHT)
canvas.pack()

t = MyTurtle(canvas)

tk.Button(master=root, text="Forward", command=lambda: t.forward(100)).pack(side=tk.TOP)
tk.Button(master=root, text="Back", command=lambda: t.back(100)).pack(side=tk.BOTTOM)
tk.Button(master=root, text="Left", command=lambda: t.left(90)).pack(side=tk.LEFT)
tk.Button(master=root, text="Right", command=lambda: t.right(90)).pack(side=tk.RIGHT)

root.mainloop()'''

import tkinter as tk

def open():
    photo = tk.PhotoImage(file="img/")
    imageLabel = tk.Label(window, image=photo)
    imageLabel.pack()


def quit():
    window.quit()

window = tk.Tk()
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)

filemenu.add_command(label="열기", command=open)
filemenu.add_command(label="종료", command=quit)

menubar.add_cascade(label="파일", menu=filemenu)

window.config(menu=menubar)
window.mainloop()


'''def process():
    e2.delete(0,END)
    sum=0
    total = int(e1.get())
    for i in range(total+1):
        sum+=i
    e2.insert(0, str(sum))

window  = Tk()

l1 = Label(window , text="끝 값")
l2 = Label(window, text="합계 값")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text="합계를 구해보자", command=process)
#b2 = Button(window, text="섭씨->화씨")
b1.grid(row=2, column=0)
#b2.grid(row=2, column=1)

window.mainloop()'''


'''from tkinter import *

window = Tk()
window.title("My Calculator")
display = Entry(window, width=33, bg="yellow")
display.grid(row=0, column=0, columnspan=5)

button_list = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', ' ',
    '1', '2', '3', '-', ' ',
    '0', '.', '=', '+', ' ']

row_index = 1
col_index = 0

for button_text in button_list:
    def process(t=button_text):
        click(t)

    Button(window, text=button_text, width=5,
           command=process).grid(row=row_index, column=col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0

def click(key):
    if (key == "="):
        result = eval(display.get())
        s = str(result)
        display.insert(END, "=" + s)
    else:
        display.insert(END, key)

window.mainloop()'''
