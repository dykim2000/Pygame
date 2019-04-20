import tkinter as tk

def open():
    pass

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
