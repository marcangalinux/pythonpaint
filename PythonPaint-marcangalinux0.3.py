import tkinter
from tkinter.colorchooser import askcolor
from tkinter import ttk
from tkinter import OptionMenu, StringVar

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
global dSelect

dSelect = "drawLine"

a=None
b=None

linewidth=4
color1='black'
colorBgDefault='#fff3e9'
colorBg='#d0d0d0'

def left_click(event):
    global a
    global b
    global linewidth
    global color1
    global dSelect
    
    
    if dSelect == "drawLine":
        x, y = event.x, event.y
            
        if a and b:  
            canvas.create_line(a, b, x, y, width= linewidth, fill=color1, smooth=True, capstyle='round', splinesteps=36)
            #canvas.create_oval(x-linewidth, y-linewidth, x+linewidth, y+linewidth, width=0, fill=color1)
        a = x
        b = y
    elif dSelect == "drawSpray":
        
        x, y = event.x, event.y
        t1 = canvas.create_text(x,   y, text="*" , fill=color1 )
        t2 = canvas.create_text(x-1, y+1, text="**" , fill=color1 )
        t3 = canvas.create_text(x-2, y+2, text="***" , fill=color1)
        t4 = canvas.create_text(x-3, y+3, text="****" , fill=color1)
        t5 = canvas.create_text(x-4, y+4, text="*****" , fill=color1)
        t6 = canvas.create_text(x-3, y+5, text="****" , fill=color1)
        t7 = canvas.create_text(x-2, y+6, text="***" , fill=color1)
        t8 = canvas.create_text(x-1, y+7, text="**" , fill=color1)
        t9 = canvas.create_text(x,   y+8, text="*" , fill=color1)
    
    elif dSelect == "drawOval":
        global posX
        global posY
        x,y = event.x, event.y
        canvas.create_oval(posX, posY, x, y, width=2 )
        

def but1_Release(event):
    global a
    global b
    global posX
    global posY
    global dSelect
    
    if dSelect=="drawLine":
        a=None
        b=None
    elif dSelect=="drawOval":
        posX=event.x
        posY.event.y
        
        
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
    global linewidth
    l=entrybox01.get()
    linewidth=int(l)

def drawSpray():
    global dSelect
    dSelect = "drawSpray"

def drawLine():
    global dSelect
    dSelect = "drawLine"
    
def drawOval():
    global dSelect
    dSelect = "drawOval"
    
    
    #canvas.create_text(x, y, text="Text ... "+str(color1))

window=tkinter.Tk()
window.geometry("1024x1200")
window.title("PythonPaint")
image1=tkinter.PhotoImage(file='/home/pi/Desktop/PythonProgs/images/ruler2.png')


textbox01 = ttk.Label(window, text = 'Pen size', font=('calibre',10, 'bold') )
entrybox01 = ttk.Entry(window)
sub_btn = ttk.Button(window,text = 'Submit', command = submit)
textbox01.pack()
entrybox01.pack()
sub_btn.pack()

menuItem=StringVar(window)
menuItem.set("Line")
w = OptionMenu(window, menuItem, "Line", "Text", "Oval")
w.pack()
print (menuItem)

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
btn6.place(x=450, y=15)

btn7 = tkinter.Button(canvas, text='Line', width=4, height=1, bd='1', command=drawLine)
btn7.place(x=500, y=15)

btn8 = tkinter.Button(canvas, text='Spray', width=4, height=1, bd='1', command=drawSpray)
btn8.place(x=550, y=15)

btn9 = tkinter.Button(canvas, text='Oval', width=4, height=1, bd='1', command=drawOval)
btn9.place(x=600, y=15)

btn10 = tkinter.Button(canvas, text='About', width=5, height=1, bd='1', command=InfoAbout)
btn10.place(x=700, y=15)



window.mainloop()
