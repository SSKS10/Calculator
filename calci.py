from tkinter import *
window=Tk()
window.geometry('490x601')
press=0
score='0'
score1='0'
char1=''
char2=''
lbl=Label(window,text='0.0',font=('helvetica',33),height=2,width=20,anchor=SE,background='black',foreground='red',cursor='cross')
lbl.place(x=2,y=0)
btnx=['']*3
btnc=['']*4
num=['']*10
def zero():
	global score,score1,press
	press=0
	score='0'
	score1='0'
	lbl=Label(window,text='0.0',font=('helvetica',33),height=2,width=20,anchor=SE,background='black',foreground='red',cursor='cross')
	lbl.place(x=2,y=0)
def neg():
	global score1
	score1=float(score1)
	score1=-score1
	score1=str(score1)
	lbl=Label(window,text=score1,font=('helvetica',33),height=2,width=20,anchor=SE,background='black',foreground='red',cursor='cross')
	lbl.place(x=2,y=0)
def s(char):
	global score,score1,char1,char2,press
	char2=char1
	char1=char
	if char1=='.':
		press=1
		score1=int(score1)
		score1=str(score1)+'.'
		lbl=Label(window,text=score1,font=('helvetica',33),height=2,width=20,anchor=SE,background='black',foreground='red',cursor='cross')
		lbl.place(x=2,y=0)
		return
	press=0	
	if char1=='=':
		print(char1,char2)
		if char2=='+':
			score=score+score1
		if char2=='-':
			score=score-score1
		if char2=='*':
			score*=score1
		if char2=='/':
			score=score/score1	
		if char2=='%':
			score=score1*score/100
		print(score+score1)											
		lbl=Label(window,text=str(score),font=('helvetica',33),height=2,width=20,anchor=SE,background='black',foreground='red',cursor='cross')
		lbl.place(x=2,y=0)	
		return
	if char2=='' or char2=='.':
		score=float(score1)
		score1=0
		#print(score,score1)
		lbl=Label(window,text=str(score),font=('helvetica',33),height=2,width=20,anchor=SE,background='black',foreground='red',cursor='cross')
		lbl.place(x=2,y=0)	
	if char2=='+':
		score1=float(score1)
		score+=score1
		print(score,score1)	
		score1=0
		lbl=Label(window,text=str(score),font=('helvetica',33),height=2,width=20,anchor=SE,background='black',foreground='red',cursor='cross')
		lbl.place(x=2,y=0)
	if char2=='-':
		score1=float(score1)		
		score-=score1
		#print(score,score1)	
		score1=0
		lbl=Label(window,text=str(score),font=('helvetica',33),height=2,width=20,anchor=SE,background='black',foreground='red',cursor='cross')
		lbl.place(x=2,y=0)	
	if char2=='*':
		score1=float(score1)		
		score*=score1
		#print(score,score1)	
		score1=0
		lbl=Label(window,text=str(score),font=('helvetica',33),height=2,width=20,anchor=SE,background='black',foreground='red',cursor='cross')
		lbl.place(x=2,y=0)
	if char2=='/':
		score1=float(score1)		
		score/=score1
		#print(score,score1)
		score1=0
		lbl=Label(window,text=str(score),font=('helvetica',33),height=2,width=20,anchor=SE,background='black',foreground='red',cursor='cross')
		lbl.place(x=2,y=0)
	if char2=='%':
		score1=float(score1)		
		score=score1*score/100
		#print(score,score1)	
		score1=0
		lbl=Label(window,text=str(score),font=('helvetica',33),height=2,width=20,anchor=SE,background='black',foreground='red',cursor='cross')
		lbl.place(x=2,y=0)														
def total(i):
	global score,score1,char1,lbl,press
	if press==1:
		score1=str(score1+str(i))
		lbl=Label(window,text=str(score1),font=('helvetica',33),height=2,width=20,anchor=SE,background='black',foreground='red',cursor='cross')
		lbl.place(x=2,y=0)
		return
	score1=float(score1)	
	score1=score1*10+i 
	lbl=Label(window,text=str(score1),font=('helvetica',33),height=2,width=20,anchor=SE,background='black',foreground='red',cursor='cross')
	lbl.place(x=2,y=0)

def gui():
	btnx[0]=Button(window,text='AC',font=('helvetica',18),height=2,width=9,command=zero)
	btnx[0].place(x=0,y=115)
	btnx[1]=Button(window,text='+/-',font=('helvetica',18),height=2,width=14,command=neg)
	btnx[1].place(x=144,y=115)
	btnx[2]=Button(window,text='%',font=('helvetica',16),height=3,width=9,command=lambda char='%':s(char))
	btnx[2].place(x=354,y=115)

	btnc[0]=Button(window,text='/',font=('helvetica',16),height=3,width=9,command=lambda char='/':s(char))
	btnc[0].place(x=354,y=212)
	btnc[1]=Button(window,text='*',font=('helvetica',16),height=3,width=9,command=lambda char='*':s(char))
	btnc[1].place(x=354,y=309)
	btnc[2]=Button(window,text='+',font=('helvetica',16),height=3,width=9,command=lambda char='+':s(char))
	btnc[2].place(x=354,y=406)
	btnc[3]=Button(window,text='-',font=('helvetica',16),height=3,width=9,command=lambda char='-':s(char))
	btnc[3].place(x=354,y=503)

	for i in range(7,10):
		num[i]=Button(window,text=i,font=('helvetica',18),height=2,width=7,command=lambda i=i:total(i))
		num[i].place(x=(i-7)*118,y=189)
	for i in range(4,7):
		num[i]=Button(window,text=i,font=('helvetica',18),height=2,width=7,command=lambda i=i:total(i))
		num[i].place(x=(i-4)*118,y=263)
	for i in range(1,4):
		num[i]=Button(window,text=i,font=('helvetica',18),height=2,width=7,command=lambda i=i:total(i))
		num[i].place(x=(i-1)*118,y=337)	
	num[0]=Button(window,text="0",font=('helvetica',18),height=2,width=15,command=lambda i=0:total(i))
	num[0].place(x=0,y=411)
	dot=Button(window,text=".",font=('helvetica',18),height=2,width=8,command=lambda char='.':s(char))
	dot.place(x=222,y=411)
	equal=Button(window,text="=",font=('helvetica',19),height=3,width=23,command=lambda char='=':s(char))
	equal.place(x=3,y=486)
gui()	
window.mainloop()