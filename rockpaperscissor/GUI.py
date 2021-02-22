import tkinter
from tkinter import *
import random

root = tkinter.Tk()

root.title("ROCK PAPER SCISSOR")
root.resizable(width=True,height=True)
root.configure(bg="white")

click = True

rHandPhoto = PhotoImage(file=r"C:\Users\Poojita\Desktop\working\practice1\rockpaperscissor\images\rhand.png")
pHandPhoto = PhotoImage(file=r"C:\Users\Poojita\Desktop\working\practice1\rockpaperscissor\images\phand.png")
sHandPhoto = PhotoImage(file=r"C:\Users\Poojita\Desktop\working\practice1\rockpaperscissor\images\shand.png")

rockPhoto = PhotoImage(file=r"C:\Users\Poojita\Desktop\working\practice1\rockpaperscissor\images\rock1.png")
paperPhoto = PhotoImage(file=r"C:\Users\Poojita\Desktop\working\practice1\rockpaperscissor\images\paper1.png")
scissorPhoto = PhotoImage(file=r"C:\Users\Poojita\Desktop\working\practice1\rockpaperscissor\images\scissor.png")

winPhoto = PhotoImage(file=r"C:\Users\Poojita\Desktop\working\practice1\rockpaperscissor\images\win1.png")
losePhoto = PhotoImage(file=r"C:\Users\Poojita\Desktop\working\practice1\rockpaperscissor\images\lose.png")
tiePhoto = PhotoImage(file=r"C:\Users\Poojita\Desktop\working\practice1\rockpaperscissor\images\tie1.png")




def play():
    global rhandbutton,phandbutton,shandbutton
    global score
    global score1
    
    rhandbutton = tkinter.Button(root,image=rHandPhoto,command=lambda:youPick('rock'),relief=FLAT,bg="white")
    phandbutton = tkinter.Button(root,image=pHandPhoto,command=lambda:youPick('paper'),relief=FLAT,bg="white")
    shandbutton = tkinter.Button(root,image=sHandPhoto,command=lambda:youPick('scissor'),relief=FLAT,bg="white")
    
    rhandbutton.grid(row=0,column=0)
    phandbutton.grid(row=0,column=1)
    shandbutton.grid(row=0,column=2)
    
def computerPick():
    choice=random.randint(1,3)

    if(choice==1):
        computerpick="rock"
    elif(choice==2):
        computerpick="paper"
    else:
        computerpick="scissor"
    return choice


def youPick(yourchoice):
    global click
    score=0
    score1=0

    computerpick = computerPick()
    if click==True:
        if yourchoice=='rock':
            rhandbutton.configure(image=rockPhoto)
            if computerpick==1:
                phandbutton.configure(image=rockPhoto)
                shandbutton.configure(image=tiePhoto)
                click==False
            elif computerpick==2:
                phandbutton.configure(image=paperPhoto)
                shandbutton.configure(image=losePhoto)
                click==False
                score1=score1+1
            else: 
                phandbutton.configure(image=scissorPhoto)
                shandbutton.configure(image=winPhoto)
                click==False
                score=score+1
        elif yourchoice=='paper':
            rhandbutton.configure(image=paperPhoto)
            if computerpick==1:
                phandbutton.configure(image=rockPhoto)
                shandbutton.configure(image=winPhoto)
                click==False
                score=score+1
            elif computerpick==2:
                phandbutton.configure(image=paperPhoto)
                shandbutton.config(image=tiePhoto)
                click==False
            else: 
                phandbutton.configure(image=scissorPhoto)
                shandbutton.configure(image=losePhoto)
                click==False
                score1=score1+1
        else:
            rhandbutton.configure(image=scissorPhoto)
            if computerpick==1:
                phandbutton.configure(image=rockPhoto)
                shandbutton.configure(image=losePhoto)
                click==False
                score1=score1+1
            elif computerpick==2:
                phandbutton.configure(image=paperPhoto)
                shandbutton.configure(image=winPhoto)
                click==False
                score=score+1
            else: 
                phandbutton.configure(image=scissorPhoto)
                shandbutton.configure(image=tiePhoto)
                click==False
        Label(text="your score is:",bg="white").grid(row=1,column=0)
        Label(text=score,bg="white").grid(row=2,column=0)
        Label(text="computer score is:",bg="white").grid(row=1,column=1)
        Label(text=score1,bg="white").grid(row=2,column=1)
        def exit():
            root.destroy()
        def reset():
            play()
        Button(root,text="Play Again",command=reset,relief=FLAT,bg="white",width=10).grid(row=1,column=3)
        Button(root,text="Exit",command=exit,relief=FLAT,bg="white",width=10).grid(row=2,column=3)
                
play()
root.mainloop()
