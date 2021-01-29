from tkinter import*
from random import randint

score=0
game_flag=True
dx=3
dy=3
r=25

def motion():
    global dx, dy, score, game_flag
    if game_flag:
        x1,y1,x2,y2=c.coords(ball)        
        if x2>300 or x1<0:
            dx=-dx
            c.itemconfig(ball,fil='#%0x%0x%0x'%(randint(0,15),randint(0,15),randint(0,15)))
        px1,py1,px2,py2=c.coords(paddle)
        if y1<0 or y2>550:
            if y1<0 or (y2>550 and ((px1<x1 and px2>x1) or (px1<x2 and px2>x2))):
                if y2>550:
                    score+=1
                    c.itemconfig(score_text,text='Счёт: {}'.format(score))
                dy=-dy
                c.itemconfig(ball,fil='#%0x%0x%0x'%(randint(0,15),randint(0,15),randint(0,15)))                
            else:
                game_flag=False
                c.create_text(130,260,text='Игра Окончена',fil='#f5f5dc',font=('Arial',25,'bold'))
            
        c.move(ball,dx,dy)
    a.after(20,motion)

def left(event):
    if c.coords(paddle)[0]>0:
        c.move(paddle,-7,0)

def right(event):
    if c.coords(paddle)[2]<300:
        c.move(paddle,+7,0)

a=Tk()
a.title('Пинг-понг')
a.iconbitmap('images/icon.ico')
a.geometry('300x600+500+30')
a.resizable(width=False,height=False)

c=Canvas(a,width=300,height=600,bg='#98777b')
c.pack()
c.create_rectangle(0,550,300,600,fil='#f5f5dc',outline='#f5f5dc')

x=randint(10,270)
ball=c.create_oval(x,5,x+r,30,fil='#9966cc',outline='#f5f5dc')

paddle=c.create_rectangle(120,550,180,570,fil='yellowgreen',outline='white')

score_text=c.create_text(240,580,text='Счёт: {}'.format(score),fil='blueviolet',font=('Arial',14,'bold'))

a.bind('<Left>',left)
a.bind('<Right>',right)

motion()
a.mainloop()
