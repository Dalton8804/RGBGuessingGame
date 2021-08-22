from tkinter import *
import random
import time,math

tk = Tk()
canvas = Canvas(tk,height = 600, width=1000)
frame = Frame(tk)
frame1 = Frame(tk)
label = Label(frame)
clrCreatedLbl = Label(frame,text="The color you created is:")
canvas1 = Canvas(frame,height=50,width=1000)
rSlide = Scale(frame1, from_=0,to=255,orient=HORIZONTAL,bd=.5,troughcolor="#FFFFFF")
gSlide = Scale(frame1, from_=0,to=255,orient=HORIZONTAL,bd=.5,troughcolor="#FFFFFF")
bSlide = Scale(frame1, from_=0,to=255,orient=HORIZONTAL,bd=.5,troughcolor="#FFFFFF")

def getVal():
	return random.randint(0,255)
r,g,b = getVal(),getVal(),getVal()
colorval = "#%02x%02x%02x" % (r, g, b)

def newColor(x,y,z):
	global r,g,b,colorval,frame
	frame.pack_forget()
	r,g,b = x,y,z
	colorval = "#%02x%02x%02x" % (r, g, b)

def setColor():
	canvas.create_rectangle(10,10,995,995, fill=colorval)
	canvas.pack(fill=BOTH)

def reset():
	newColor(getVal(),getVal(),getVal())
	setColor()
	canvas.update()

def cycle():
	global r,g,b
	for x in range(0,50):
		time.sleep((x*math.exp(4))/10000+.1)
		reset()

def guess():
	global label,r,g,b,frame,canvas1
	frame.pack()
	rG,gG,bG = rSlide.get(),gSlide.get(),bSlide.get()
	guessColorVal = "#%02x%02x%02x" % (rG,gG,bG)
	if abs(rG-r)<20 and abs(gG-g)<20 and abs(bG-b)<20:
		label.config(text="GOT IT, the values are {},{},{}".format(r,g,b))
	else:
		label.config(text="Incorrect, the correct values are {},{},{}".format(r,g,b))
	canvas1.create_rectangle(10,10,1000,40,fill=guessColorVal)	
	label.pack()
	clrCreatedLbl.pack()
	canvas1.pack()
	


setColor()
rLbl = Label(frame1, text="R", font=("Arial",25))
rLbl.grid(row=0,column=0,)
gLbl = Label(frame1, text="G", font=("Arial",25))
gLbl.grid(row=1,column=0)
bLbl = Label(frame1, text="B", font=("Arial",25))
bLbl.grid(row=2,column=0)
rSlide.grid(row = 0,column = 1)
gSlide.grid(row = 1,column = 1)
bSlide.grid(row = 2,column = 1)
frame1.pack()

resetBtn = Button(tk, command=reset, text='New Color').pack()
cycleBtn = Button(tk, command=cycle, text='Cycle Colors').pack()
guessBtn = Button(tk, command=guess, text='Make Guess').pack()
frame.pack()
tk.mainloop()
print(colorval)