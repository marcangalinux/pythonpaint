import tkinter
from tkinter.colorchooser import askcolor
from tkinter import ttk

global a
global b
global linewidth
global color1
global colorBg
global posX
global posY
global canvas
global image1
global rulerSet
rulerSet=0
global ruler1

a=None
b=None
linewidth=4
color1='black'
colorBgDefault='#d9d9d9'
colorBg='#d0d0d0'

def left_click(event):
    global a
    global b
    global linewidth
    global color1
    
    x, y = event.x, event.y
    
    
    if a and b:  
        canvas.create_line(a, b, x, y, width= linewidth, fill=color1, smooth=True, capstyle='round', splinesteps=36)
        #canvas.create_oval(x-linewidth, y-linewidth, x+linewidth, y+linewidth, width=0, fill=color1)
    a = x
    b = y


def but1_Release(event):
    global a
    global b
    a=None
    b=None

def ClearScreen():
    global linewidth
    global color1
    global colorBgDefault
    global textPen
    global textColor
    canvas.delete('all')
    color1="black"
    linewidth=4
    canvas.configure(bg=colorBgDefault)
    textPen = canvas.create_text(380, 6, text="Pen: "+str(linewidth) )
    textColor = canvas.create_text(145, 6, text="Color: "+str(color1) )
    canvas.itemconfig(textColor, text="Color: "+str(color1))
    canvas.itemconfig(textPen, text="Pen: "+str(linewidth))
    
    
def SelectColor():
    global color1
    colors = askcolor(title="Set the pen color ...")
    print (colors)
    color1=colors[1]
    canvas.itemconfig(textColor, text="Color: "+str(color1))

def PenPlus():
    global linewidth
    linewidth = linewidth + 1
    print (linewidth)
    canvas.itemconfig(textPen, text="Pen: "+str(linewidth))
    

def PenMinus():
    global linewidth
    if linewidth>2:
        linewidth = linewidth - 1
        print(linewidth)
    else:
        linewidth = 1
    print(linewidth)
    canvas.itemconfig(textPen, text="Pen: "+str(linewidth))
    
    
def setBg():
    global colorBg
    colors = askcolor(title="Set the pen color ...")
    print (colors)
    colorBg=colors[1]
    canvas.configure(bg=colorBg)
  
def InfoAbout():
    canvas.create_text(800,30,fill="black",font="Times 10 italic bold",text="Program version 0.1" , anchor="sw")
    canvas.create_text(800,50,fill="black",font="Times 10 italic",text="Created: 2022, February", anchor="sw")
    canvas.create_text(800,70,fill="black",font="Times 10 italic",text="by autor: Daddy", anchor="sw")
    

def drawRuler():
    global canvas
    global image1
    global rulerSet
    global ruler1
    if rulerSet == 0:
        ruler1 = canvas.create_image( (0,100) , image=image1,  anchor="sw")
        rulerSet=1
    else:
        canvas.delete(ruler1)
        rulerSet=0

def rightClickPress(event):
    global posX
    global posY
    posX,posY = event.x, event.y
    

def rightClickRelease(event):
    global posX
    global posY
    x,y = event.x, event.y
    canvas.create_oval(posX, posY, x, y, width=2 )

def submit():
    None

window=tkinter.Tk()
window.geometry("1024x1200")
window.title("Daddy's Paint program")
image1=tkinter.PhotoImage(file='images/ruler2.png')
canvas = tkinter.Canvas(width=1024, height=700, bg=colorBg)

textPen = canvas.create_text(380, 6, text="Pen: "+str(linewidth) )
textColor = canvas.create_text(145, 6, text="Color: "+str(color1) )
canvas.pack()
canvas.bind('<B1-Motion>', left_click)
canvas.bind('<ButtonPress-3>', rightClickPress)
canvas.bind('<ButtonRelease-3>', rightClickRelease)
canvas.bind('<ButtonRelease-1>', but1_Release)
#canvas.bind('<ButtonPress-2>', middle_click)
#canvas.bind_all('<Key>', colorSet )

btn1 = tkinter.Button(canvas, text='Clear Screen', width=9, height=1, bd='1', bg='red', fg='yellow', command=ClearScreen)
btn1.place(x=5, y=15)

btn2 = tkinter.Button(canvas, text='Pen Color', width=7, height=1, bd='1', bg='cyan', command=SelectColor)
btn2.place(x=105, y=15)

btn3 = tkinter.Button(canvas, text='Background', width=11, height=1, bd='1', command=setBg)
btn3.place(x=200, y=15)

btn4 = tkinter.Button(canvas, text='Pen +', width=4, height=1, bd='1', command=PenPlus)
btn4.place(x=320, y=15)

btn5 = tkinter.Button(canvas, text='Pen -', width=4, height=1, bd='1', command=PenMinus)
btn5.place(x=380, y=15)

btn6 = tkinter.Button(canvas, text='Ruler', width=4, height=1, bd='1', command=drawRuler)
btn6.place(x=500, y=15)

btn7 = tkinter.Button(canvas, text='About', width=5, height=1, bd='1', command=InfoAbout)
btn7.place(x=700, y=15)

name_var=""
passw_var=""

textbox01 = ttk.Label(window, text = 'Username', font=('calibre',10, 'bold'))
textbox02 = ttk.Entry(window)
textbox03 = ttk.Label(window, text = 'Password', font = ('calibre',10,'bold'))
textbox04 = ttk.Entry(window, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
sub_btn = ttk.Button(window,text = 'Submit', command = submit)

textbox01.pack()
textbox02.pack()
textbox03.pack()
textbox04.pack()
sub_btn.pack()

window.mainloop()
