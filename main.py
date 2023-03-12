from tkinter import *
from tkinter.messagebox import showinfo
import colors

root = Tk()
root.title("Pop It")
root.geometry("400x400")
root.resizable(False , False)

root.configure(bg="gray10")

val = False

game = Frame(root , width=375 , height=375 , bg="gray10")
game.pack()

starttext = Label(text="\n \n Pop It \n \n" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro" , 16))
starttext.pack(in_=game)

buttonplay = Button(text="Play" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1")
buttonplay.pack(in_=game)

n1 = Label(text="\n" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro" , 2))
n1.pack(in_=game)

buttonab = Button(text="About"  , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1" , command=lambda:showinfo("About" , "Pop-It 0.1 Build1 \n https://github.com/sontaimnt/Pop-It \n \n Copyright sontaimnt 2023"))
buttonab.pack(in_=game)

n2 = Label(text="\n \n \n" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro" , 12))
n2.pack(in_=game)

buttonex = Button(text="Exit"  , bg="brown1" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16 , "bold") , width=15 , command=lambda:root.destroy() , relief='flat')
buttonex.pack(in_=game)

button33 = Button(text="3x3" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1")
button44 = Button(text="4x4" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1")
button55 = Button(text="5x5" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1")

n3 = Label(text="\n" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro" , 2))

b1p = [False]
b2p = [False]
b3p = [False]
b4p = [False]
b5p = [False]
b6p = [False]
b7p = [False]
b8p = [False]
b9p = [False]
b10p = [False]
b11p = [False]
b12p = [False]
b13p = [False]
b14p = [False]
b15p = [False]
b16p = [False]
b17p = [False]
b18p = [False]
b19p = [False]
b20p = [False]
b21p = [False]
b22p = [False]
b23p = [False]
b24p = [False]
b25p = [False]

def play_start():
    n1.pack_forget()
    n2.pack_forget()
    buttonab.pack_forget()
    buttonex.pack_forget()
    buttonplay.pack_forget()
    starttext.configure(text="\n Select game mode \n \n")
    button33.pack()
    n1.pack()
    button44.pack()
    n2.configure(text="\n" , font=("Source Code Pro",2))
    n2.pack()
    button55.pack()
    n3.pack()

def three_three():
    global b1 , b2 , b3 , b4 , b5 , b6 , b7 , b8 , b9 , b1p , b2p , b3p , b4p , b5p , b6p , b7p , b8p , b9p
    starttext.configure(text="\n Click the buttons to start popping \n" , font=("Source Code Pro",12))
    button33.pack_forget()
    button44.pack_forget()
    button55.pack_forget()
    n1.pack_forget()
    n2.pack_forget()
    n3.pack_forget()
    gframe = Frame(root , width=345 , height=345)
    gframe.pack()
    f1 = Frame(root , width=115 , height=300 , bg=colors.colorsred[0])
    f2 = Frame(root , width=115 , height=300 , bg=colors.colorsred[0])
    f3 = Frame(root , width=115 , height=300 )
    f1.pack(in_=gframe ,side=LEFT)
    f2.pack(in_=gframe ,side=LEFT)
    f3.pack(in_=gframe ,side=LEFT)
    b1 = Button(root , width=12 , height=5 , bg=colors.colorsred[0] , command=lambda:logic(b1 , b1p , colors.colorsred))
    b2 = Button(root , width=12 , height=5 , bg=colors.colorsred[0] , command=lambda:logic(b2 , b2p , colors.colorsred))
    b3 = Button(root , width=12 , height=5 , bg=colors.colorsred[0] , command=lambda:logic(b3 , b3p , colors.colorsred))
    b4 = Button(root , width=12 , height=5 , bg=colors.colorsyellow[0] , command=lambda:logic(b4 , b4p , colors.colorsyellow)) 
    b5 = Button(root , width=12 , height=5 , bg=colors.colorsyellow[0] , command=lambda:logic(b5 , b5p , colors.colorsyellow))
    b6 = Button(root , width=12 , height=5 , bg=colors.colorsyellow[0] , command=lambda:logic(b6 , b6p , colors.colorsyellow))
    b7 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=lambda:logic(b7 , b7p , colors.colorsblue))
    b8 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=lambda:logic(b8 , b8p , colors.colorsblue))
    b9 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=lambda:logic(b9 , b9p , colors.colorsblue))
    b1.pack(in_=f1)
    b2.pack(in_=f1)
    b3.pack(in_=f1)
    b4.pack(in_=f2)
    b5.pack(in_=f2)
    b6.pack(in_=f2)
    b7.pack(in_=f3)
    b8.pack(in_=f3)
    b9.pack(in_=f3)

def three_three():
    global b1 , b2 , b3 , b4 , b5 , b6 , b7 , b8 , b9
    starttext.configure(text="\n Click the buttons to start popping \n" , font=("Source Code Pro",12))
    button33.pack_forget()
    button44.pack_forget()
    button55.pack_forget()
    n1.pack_forget()
    n2.pack_forget()
    n3.pack_forget()
    gframe = Frame(root , width=345 , height=345)
    gframe.pack()
    f1 = Frame(root , width=115 , height=300 , bg=colors.colorsred[0])
    f2 = Frame(root , width=115 , height=300 , bg=colors.colorsred[0])
    f3 = Frame(root , width=115 , height=300 )
    f1.pack(in_=gframe ,side=LEFT)
    f2.pack(in_=gframe ,side=LEFT)
    f3.pack(in_=gframe ,side=LEFT)
    b1 = Button(root , width=12 , height=5 , bg=colors.colorsred[0] , command=lambda:logic(b1 , b1p , colors.colorsred))
    b2 = Button(root , width=12 , height=5 , bg=colors.colorsred[0] , command=lambda:logic(b2 , b2p , colors.colorsred))
    b3 = Button(root , width=12 , height=5 , bg=colors.colorsred[0] , command=lambda:logic(b3 , b3p , colors.colorsred))
    b4 = Button(root , width=12 , height=5 , bg=colors.colorsyellow[0] , command=lambda:logic(b4 , b4p , colors.colorsyellow)) 
    b5 = Button(root , width=12 , height=5 , bg=colors.colorsyellow[0] , command=lambda:logic(b5 , b5p , colors.colorsyellow))
    b6 = Button(root , width=12 , height=5 , bg=colors.colorsyellow[0] , command=lambda:logic(b6 , b6p , colors.colorsyellow))
    b7 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=lambda:logic(b7 , b7p , colors.colorsblue))
    b8 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=lambda:logic(b8 , b8p , colors.colorsblue))
    b9 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=lambda:logic(b9 , b9p , colors.colorsblue))
    b1.pack(in_=f1)
    b2.pack(in_=f1)
    b3.pack(in_=f1)
    b4.pack(in_=f2)
    b5.pack(in_=f2)
    b6.pack(in_=f2)
    b7.pack(in_=f3)
    b8.pack(in_=f3)
    b9.pack(in_=f3)

def four_four():
    global b1 , b2 , b3 , b4 , b5 , b6 , b7 , b8 , b9 , b10 , b11 , b12 , b13 , b14 , b15 , b16
    starttext.configure(text="\n Click the buttons to start popping \n" , font=("Source Code Pro",12))
    button33.pack_forget()
    button44.pack_forget()
    button55.pack_forget()
    n1.pack_forget()
    n2.pack_forget()
    n3.pack_forget()
    gframe = Frame(root , width=345 , height=345)
    gframe.pack()    
    f1 = Frame(root , width=86 , height=300 , bg=colors.colorsred[0])
    f2 = Frame(root , width=86 , height=300 , bg=colors.colorsyellow[0])
    f3 = Frame(root , width=86 , height=300  , bg=colors.colorsgreen[0])
    f4 = Frame(root , width=86 , height=300  , bg=colors.colorsblue[0])
    b1 = Button(root , width=8 , height=4 , bg=colors.colorsred[0] , command=lambda:logic(b1 , b1p , colors.colorsred))
    b2 = Button(root , width=8 , height=4 , bg=colors.colorsred[0] , command=lambda:logic(b2 , b2p , colors.colorsred))
    b3 = Button(root , width=8 , height=4 , bg=colors.colorsred[0] , command=lambda:logic(b3 , b3p , colors.colorsred))
    b4 = Button(root , width=8 , height=4 , bg=colors.colorsred[0] , command=lambda:logic(b4 , b4p , colors.colorsred)) 
    b5 = Button(root , width=8 , height=4 , bg=colors.colorsyellow[0] , command=lambda:logic(b5 , b5p , colors.colorsyellow))
    b6 = Button(root , width=8 , height=4 , bg=colors.colorsyellow[0] , command=lambda:logic(b6 , b6p , colors.colorsyellow))
    b7 = Button(root , width=8 , height=4 , bg=colors.colorsyellow[0] , command=lambda:logic(b7 , b7p , colors.colorsyellow))
    b8 = Button(root , width=8 , height=4 , bg=colors.colorsyellow[0] , command=lambda:logic(b8 , b8p , colors.colorsyellow)) 
    b9 = Button(root , width=8 , height=4 , bg=colors.colorsgreen[0] , command=lambda:logic(b9 , b9p , colors.colorsgreen))
    b10 = Button(root , width=8 , height=4 , bg=colors.colorsgreen[0] , command=lambda:logic(b10 , b10p , colors.colorsgreen))
    b11 = Button(root , width=8 , height=4 , bg=colors.colorsgreen[0] , command=lambda:logic(b11 , b11p , colors.colorsgreen))
    b12 = Button(root , width=8 , height=4 , bg=colors.colorsgreen[0] , command=lambda:logic(b12 , b12p , colors.colorsgreen)) 
    b13 = Button(root , width=8 , height=4 , bg=colors.colorsblue[0] , command=lambda:logic(b13 , b13p , colors.colorsblue))
    b14 = Button(root , width=8 , height=4 , bg=colors.colorsblue[0] , command=lambda:logic(b14 , b14p , colors.colorsblue))
    b15 = Button(root , width=8 , height=4 , bg=colors.colorsblue[0] , command=lambda:logic(b15 , b15p , colors.colorsblue))
    b16 = Button(root , width=8 , height=4 , bg=colors.colorsblue[0] , command=lambda:logic(b16 , b16p , colors.colorsblue)) 
    f1.pack(in_=gframe ,side=LEFT)
    f2.pack(in_=gframe ,side=LEFT)
    f3.pack(in_=gframe ,side=LEFT)
    f4.pack(in_=gframe ,side=LEFT)
    b1.pack(in_=f1)
    b2.pack(in_=f1)
    b3.pack(in_=f1)
    b4.pack(in_=f1)
    b5.pack(in_=f2) 
    b6.pack(in_=f2) 
    b7.pack(in_=f2) 
    b8.pack(in_=f2) 
    b9.pack(in_=f3)
    b10.pack(in_=f3)
    b11.pack(in_=f3)
    b12.pack(in_=f3)
    b13.pack(in_=f4) 
    b14.pack(in_=f4) 
    b15.pack(in_=f4) 
    b16.pack(in_=f4) 

def five_five():
    global b1 , b2 , b3 , b4 , b5 , b6 , b7 , b8 , b9 , b10 , b11 , b12 , b13 , b14 , b15 , b16
    starttext.configure(text="\n Click the buttons to start popping \n" , font=("Source Code Pro",12))
    button33.pack_forget()
    button44.pack_forget()
    button55.pack_forget()
    n1.pack_forget()
    n2.pack_forget()
    n3.pack_forget()
    gframe = Frame(root , width=345 , height=345)
    gframe.pack()    
    f1 = Frame(root , width=69 , height=300 , bg=colors.colorsred[0])
    f2 = Frame(root , width=69 , height=300 , bg=colors.colorsyellow[0])
    f3 = Frame(root , width=69 , height=300  , bg=colors.colorsgreen[0])
    f4 = Frame(root , width=69 , height=300  , bg=colors.colorsblue[0])
    f5 = Frame(root , width=69 , height=300  , bg=colors.colorspurple[0])
    b1 = Button(root , width=6 , height=3 , bg=colors.colorsred[0] , command=lambda:logic(b1 , b1p , colors.colorsred))
    b2 = Button(root , width=6 , height=3 , bg=colors.colorsred[0] , command=lambda:logic(b2 , b2p , colors.colorsred))
    b3 = Button(root , width=6 , height=3 , bg=colors.colorsred[0] , command=lambda:logic(b3 , b3p , colors.colorsred))
    b4 = Button(root , width=6 , height=3 , bg=colors.colorsred[0] , command=lambda:logic(b4 , b4p , colors.colorsred)) 
    b5 = Button(root , width=6 , height=3 , bg=colors.colorsred[0] , command=lambda:logic(b5 , b5p , colors.colorsred))
    b6 = Button(root , width=6, height=3 , bg=colors.colorsyellow[0] , command=lambda:logic(b6 , b6p , colors.colorsyellow))
    b7 = Button(root , width=6 , height=3 , bg=colors.colorsyellow[0] , command=lambda:logic(b7 , b7p , colors.colorsyellow))
    b8 = Button(root , width=6 , height=3 , bg=colors.colorsyellow[0] , command=lambda:logic(b8 , b8p , colors.colorsyellow)) 
    b9 = Button(root , width=6 , height=3 , bg=colors.colorsyellow[0] , command=lambda:logic(b9 , b9p , colors.colorsyellow))
    b10 = Button(root , width=6 , height=3 , bg=colors.colorsyellow[0] , command=lambda:logic(b10 , b10p , colors.colorsyellow))
    b11 = Button(root , width=6 , height=3 , bg=colors.colorsgreen[0] , command=lambda:logic(b11 , b11p , colors.colorsgreen))
    b12 = Button(root , width=6 , height=3 , bg=colors.colorsgreen[0] , command=lambda:logic(b12 , b12p , colors.colorsgreen)) 
    b13 = Button(root , width=6 , height=3 , bg=colors.colorsgreen[0] , command=lambda:logic(b13 , b13p , colors.colorsgreen))
    b14 = Button(root , width=6 , height=3 , bg=colors.colorsgreen[0] , command=lambda:logic(b14 , b14p , colors.colorsgreen))
    b15 = Button(root , width=6 , height=3 , bg=colors.colorsgreen[0] , command=lambda:logic(b15 , b15p , colors.colorsgreen))
    b16 = Button(root , width=6 , height=3 , bg=colors.colorsblue[0] , command=lambda:logic(b16 , b16p , colors.colorsblue)) 
    b17 = Button(root , width=6 , height=3 , bg=colors.colorsblue[0] , command=lambda:logic(b17 , b17p , colors.colorsblue)) 
    b18 = Button(root , width=6 , height=3 , bg=colors.colorsblue[0] , command=lambda:logic(b18 , b18p , colors.colorsblue)) 
    b19 = Button(root , width=6 , height=3 , bg=colors.colorsblue[0] , command=lambda:logic(b19 , b19p , colors.colorsblue)) 
    b20 = Button(root , width=6 , height=3 , bg=colors.colorsblue[0] , command=lambda:logic(b20 , b20p , colors.colorsblue)) 
    b21 = Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b21 , b21p , colors.colorspurple)) 
    b22 = Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b22 , b22p , colors.colorspurple)) 
    b23 = Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b23 , b23p , colors.colorspurple)) 
    b24 = Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b24 , b24p , colors.colorspurple)) 
    b25 = Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b25 , b25p , colors.colorspurple)) 

    f1.pack(in_=gframe ,side=LEFT)
    f2.pack(in_=gframe ,side=LEFT)
    f3.pack(in_=gframe ,side=LEFT)
    f4.pack(in_=gframe ,side=LEFT)
    f5.pack(in_=gframe , side=LEFT)
    b1.pack(in_=f1)
    b2.pack(in_=f1)
    b3.pack(in_=f1)
    b4.pack(in_=f1)
    b5.pack(in_=f1) 
    b6.pack(in_=f2) 
    b7.pack(in_=f2) 
    b8.pack(in_=f2) 
    b9.pack(in_=f2)
    b10.pack(in_=f2)
    b11.pack(in_=f3)
    b12.pack(in_=f3)
    b13.pack(in_=f3) 
    b14.pack(in_=f3) 
    b15.pack(in_=f3) 
    b16.pack(in_=f4) 
    b17.pack(in_=f4)
    b18.pack(in_=f4)
    b19.pack(in_=f4)
    b20.pack(in_=f4)
    b21.pack(in_=f5)
    b22.pack(in_=f5)
    b23.pack(in_=f5)
    b24.pack(in_=f5)
    b25.pack(in_=f5)

def logic(button: Button , array: list , color: list):
    if array[len(array)-1] == False:
        array.append(True)
        button.configure(bg=color[1])
    else:
        array.append(False)
        button.configure(bg=color[0])

buttonplay.configure(command=play_start)
button33.configure(command=three_three)
button44.configure(command=four_four)
button55.configure(command=five_five)

root.mainloop()
