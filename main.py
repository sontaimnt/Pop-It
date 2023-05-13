from tkinter import Label, Button, Frame, Tk, LEFT
from tkinter.messagebox import showinfo , showerror
from random import randint 
import colors

root = Tk()
root.title("Pop It")
root.geometry("425x425")
root.resizable(False , False)

root.configure(bg="gray10")

game = Frame(root , width=375 , height=375 , bg="gray10")
game.pack()

starttext = Label(text="\n Pop It" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro" , 16))
starttext.pack(in_=game , pady=25)

buttonplayt = Button(text="Play(with toys)" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1")
buttonplayt.pack(in_=game)

buttonplayg = Button(text="Play(with games)" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1")
buttonplayg.pack(in_=game, pady=10)

buttonab = Button(text="About"  , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1" , command=lambda:showinfo("About" , "Pop-It 0.2 Development Copy \n https://github.com/sontaimnt/Pop-It/tree/0.2-build \n \n Copyright sontaimnt 2023"))
buttonab.pack(in_=game)

buttonex = Button(text="Exit"  , bg="brown1" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16 , "bold") , width=15 , command=lambda:root.destroy() , relief='flat')
buttonex.pack(in_=game, pady=50)

button33 = Button(text="3x3" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1")
button44 = Button(text="4x4" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1")
button55 = Button(text="5x5" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1")
button33t = Button(text="3x3(Triangular)" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1")
button44t = Button(text="4x4(Triangular)" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1")
button55t = Button(text="5x5(Triangular)" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1")

buttonpluck = Button(text="Pluck(Luck Determiner)" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1")
buttonuc = Button(text="Pange(3 Challenges)" , bg="gray10" , fg="antiquewhite1" , font=("Source Code Pro Semibold" , 16) , width=15 , activebackground="gray15" , activeforeground="antiquewhite1")

def play_start():
    buttonab.pack_forget()
    buttonex.pack_forget()
    buttonplayt.pack_forget()
    buttonplayg.pack_forget()
    #n6.pack_forget()
    starttext.configure(text="Select the toy for playing")
    button33.pack(pady=5)
    button44.pack(pady=5)
    button55.pack(pady=5)
    
    button33t.pack(pady=5)
    #n4.pack()
    button44t.pack(pady=5)
    #n5.pack()
    button55t.pack(pady=5)

def play_start_game():  
    buttonab.pack_forget()
    buttonex.pack_forget()
    buttonplayt.pack_forget()
    buttonplayg.pack_forget()
    starttext.configure(text="\n Select the game for playing")
    buttonpluck.configure(width=22 , command=pweep_frame)
    buttonpluck.pack(pady=5)
    buttonuc.configure(width=22)
    buttonuc.pack(pady=5)

def three_three():
    global b1 , b2 , b3 , b4 , b5 , b6 , b7 , b8 , b9
    starttext.configure(text="\n Click the buttons to start popping" , font=("Source Code Pro",12))
    button33.pack_forget()
    button44.pack_forget()
    button55.pack_forget()
    button33t.pack_forget()
    button44t.pack_forget()
    button55t.pack_forget()
    gframe = Frame(root , width=345 , height=345)
    gframe.pack()
    f1 = Frame(root , width=115 , height=300 , bg=colors.colorsred[0])
    f2 = Frame(root , width=115 , height=300 , bg=colors.colorsblue[0])
    f3 = Frame(root , width=115 , height=300 , bg=colors.colorsyellow[0])
    f1.pack(in_=gframe ,side=LEFT)
    f2.pack(in_=gframe ,side=LEFT)
    f3.pack(in_=gframe ,side=LEFT)
    b1 = Button(root , width=12 , height=5 , bg=colors.colorsred[0] , command=lambda:logic(b1))
    b2 = Button(root , width=12 , height=5 , bg=colors.colorsred[0] , command=lambda:logic(b2))
    b3 = Button(root , width=12 , height=5 , bg=colors.colorsred[0] , command=lambda:logic(b3))
    b4 = Button(root , width=12 , height=5 , bg=colors.colorsyellow[0] , command=lambda:logic(b4)) 
    b5 = Button(root , width=12 , height=5 , bg=colors.colorsyellow[0] , command=lambda:logic(b5))
    b6 = Button(root , width=12 , height=5 , bg=colors.colorsyellow[0] , command=lambda:logic(b6))
    b7 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=lambda:logic(b7))
    b8 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=lambda:logic(b8))
    b9 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=lambda:logic(b9))
    b1.pack(in_=f1)
    b2.pack(in_=f1)
    b3.pack(in_=f1)
    b4.pack(in_=f2)
    b5.pack(in_=f2)
    b6.pack(in_=f2)
    b7.pack(in_=f3)
    b8.pack(in_=f3)
    b9.pack(in_=f3)

def three_three_t():
    global b1 , b2 , b3 , b4 , b5 , b6 
    starttext.configure(text="\n Click the buttons to start popping" , font=("Source Code Pro" , 12))
    button33t.pack_forget()
    button33.pack_forget()
    button44.pack_forget()
    button55.pack_forget()
    button33t.pack_forget()
    button44t.pack_forget()
    button55t.pack_forget()
    gframe = Frame(root , width=345 , height=345 , bg="grey10")
    gframe.pack()
    f1 = Frame(root , width=345 , height=115 , bg=colors.colorsred[0])
    f2 = Frame(root , width=345 , height=115 , bg=colors.colorsyellow[0])
    f3 = Frame(root , width=345 , height=115 , bg=colors.colorsblue[0])
    f1.pack(in_=gframe)
    f2.pack(in_=gframe)
    f3.pack(in_=gframe)
    b1 = Button(root , width=12 , height=5 , bg=colors.colorsred[0] , command=lambda:logic(b1))
    b2 = Button(root , width=12 , height=5 , bg=colors.colorsyellow[0] , command=lambda:logic(b2))
    b3 = Button(root , width=12 , height=5 , bg=colors.colorsyellow[0] , command=lambda:logic(b3))
    b4 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=lambda:logic(b4)) 
    b5 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=lambda:logic(b5))
    b6 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=lambda:logic(b6))
    b1.pack(in_=f1 , side="left")
    b2.pack(in_=f2 , side="left")
    b3.pack(in_=f2 , side="left")
    b4.pack(in_=f3 , side="left")
    b5.pack(in_=f3 , side="left")
    b6.pack(in_=f3 , side="left")

def four_four():
    global b1 , b2 , b3 , b4 , b5 , b6 , b7 , b8 , b9 , b10 , b11 , b12 , b13 , b14 , b15 , b16
    starttext.configure(text="\n Click the buttons to start popping" , font=("Source Code Pro",12))
    button33.pack_forget()
    button44.pack_forget()
    button55.pack_forget()
    button33t.pack_forget()
    button44t.pack_forget()
    button55t.pack_forget()
    gframe = Frame(root , width=345 , height=345)
    gframe.pack()
    f1 = Frame(root , width=86 , height=300 , bg=colors.colorsred[0])
    f2 = Frame(root , width=86 , height=300 , bg=colors.colorsyellow[0])
    f3 = Frame(root , width=86 , height=300  , bg=colors.colorsgreen[0])
    f4 = Frame(root , width=86 , height=300  , bg=colors.colorsblue[0])
    b1 = Button(root , width=8 , height=4 , bg=colors.colorsred[0] , command=lambda:logic(b1))
    b2 = Button(root , width=8 , height=4 , bg=colors.colorsred[0] , command=lambda:logic(b2))
    b3 = Button(root , width=8 , height=4 , bg=colors.colorsred[0] , command=lambda:logic(b3))
    b4 = Button(root , width=8 , height=4 , bg=colors.colorsred[0] , command=lambda:logic(b4)) 
    b5 = Button(root , width=8 , height=4 , bg=colors.colorsyellow[0] , command=lambda:logic(b5))
    b6 = Button(root , width=8 , height=4 , bg=colors.colorsyellow[0] , command=lambda:logic(b6))
    b7 = Button(root , width=8 , height=4 , bg=colors.colorsyellow[0] , command=lambda:logic(b7))
    b8 = Button(root , width=8 , height=4 , bg=colors.colorsyellow[0] , command=lambda:logic(b8)) 
    b9 = Button(root , width=8 , height=4 , bg=colors.colorsgreen[0] , command=lambda:logic(b9))
    b10 = Button(root , width=8 , height=4 , bg=colors.colorsgreen[0] , command=lambda:logic(b10))
    b11 = Button(root , width=8 , height=4 , bg=colors.colorsgreen[0] , command=lambda:logic(b11))
    b12 = Button(root , width=8 , height=4 , bg=colors.colorsgreen[0] , command=lambda:logic(b12)) 
    b13 = Button(root , width=8 , height=4 , bg=colors.colorsblue[0] , command=lambda:logic(b13))
    b14 = Button(root , width=8 , height=4 , bg=colors.colorsblue[0] , command=lambda:logic(b14))
    b15 = Button(root , width=8 , height=4 , bg=colors.colorsblue[0] , command=lambda:logic(b15))
    b16 = Button(root , width=8 , height=4 , bg=colors.colorsblue[0] , command=lambda:logic(b16)) 
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

def four_four_t():
    global b1 , b2 , b3 , b4 , b5 , b6 , b7 , b8 , b9 , b10
    starttext.configure(text="\n Click the buttons to start popping" , font=("Source Code Pro",12))
    button33.pack_forget()
    button44.pack_forget()
    button55.pack_forget()
    button33t.pack_forget()
    button44t.pack_forget()
    button55t.pack_forget()
    gframe = Frame(root , width=345 , height=345 , bg="gray10")
    gframe.pack()
    f1 = Frame(root , width=345 , height=86 , bg=colors.colorsred[0])  
    f2 = Frame(root , width=345 , height=86 , bg=colors.colorsyellow[0])  
    f3 = Frame(root , width=345 , height=86 , bg=colors.colorsgreen[0])  
    f4 = Frame(root , width=345 , height=86 , bg=colors.colorsblue[0])  
    f1.pack(in_=gframe)
    f2.pack(in_=gframe)
    f3.pack(in_=gframe)
    f4.pack(in_=gframe)
    b1 = Button(root , width=8 , height=4 , bg=colors.colorsred[0] , command=lambda:logic(b1))
    b2 = Button(root , width=8 , height=4 , bg=colors.colorsyellow[0] , command=lambda:logic(b2))
    b3 = Button(root , width=8 , height=4 , bg=colors.colorsyellow[0] , command=lambda:logic(b3))
    b4 = Button(root , width=8 , height=4 , bg=colors.colorsgreen[0] , command=lambda:logic(b4)) 
    b5 = Button(root , width=8 , height=4 , bg=colors.colorsgreen[0] , command=lambda:logic(b5))
    b6 = Button(root , width=8 , height=4 , bg=colors.colorsgreen[0] , command=lambda:logic(b6))
    b7 = Button(root , width=8 , height=4 , bg=colors.colorsblue[0] , command=lambda:logic(b7))
    b8 = Button(root , width=8 , height=4 , bg=colors.colorsblue[0] , command=lambda:logic(b8)) 
    b9 = Button(root , width=8 , height=4 , bg=colors.colorsblue[0] , command=lambda:logic(b9))
    b10 = Button(root , width=8 , height=4 , bg=colors.colorsblue[0] , command=lambda:logic(b10))
    b1.pack(in_=f1 , side="left")
    b2.pack(in_=f2 , side="left")
    b3.pack(in_=f2 , side="left")
    b4.pack(in_=f3 , side="left")
    b5.pack(in_=f3 , side="left")
    b6.pack(in_=f3 , side="left")
    b7.pack(in_=f4 , side="left")
    b8.pack(in_=f4 , side="left")
    b9.pack(in_=f4 , side="left")
    b10.pack(in_=f4 , side="left")

def five_five():
    global b1 , b2 , b3 , b4 , b5 , b6 , b7 , b8 , b9 , b10 , b11 , b12 , b13 , b14 , b15 , b16
    starttext.configure(text="\n Click the buttons to start popping" , font=("Source Code Pro",12))
    button33.pack_forget()
    button44.pack_forget()
    button55.pack_forget()
    button33t.pack_forget()
    button44t.pack_forget()
    button55t.pack_forget()
    gframe = Frame(root , width=345 , height=345)
    gframe.pack()    
    f1 = Frame(root , width=69 , height=300 , bg=colors.colorsred[0])
    f2 = Frame(root , width=69 , height=300 , bg=colors.colorsyellow[0])
    f3 = Frame(root , width=69 , height=300  , bg=colors.colorsgreen[0])
    f4 = Frame(root , width=69 , height=300  , bg=colors.colorsblue[0])
    f5 = Frame(root , width=69 , height=300  , bg=colors.colorspurple[0])
    b1 = Button(root , width=6 , height=3 , bg=colors.colorsred[0] , command=lambda:logic(b1))
    b2 = Button(root , width=6 , height=3 , bg=colors.colorsred[0] , command=lambda:logic(b2))
    b3 = Button(root , width=6 , height=3 , bg=colors.colorsred[0] , command=lambda:logic(b3))
    b4 = Button(root , width=6 , height=3 , bg=colors.colorsred[0] , command=lambda:logic(b4)) 
    b5 = Button(root , width=6 , height=3 , bg=colors.colorsred[0] , command=lambda:logic(b5))
    b6 = Button(root , width=6, height=3 , bg=colors.colorsyellow[0] , command=lambda:logic(b6))
    b7 = Button(root , width=6 , height=3 , bg=colors.colorsyellow[0] , command=lambda:logic(b7))
    b8 = Button(root , width=6 , height=3 , bg=colors.colorsyellow[0] , command=lambda:logic(b8)) 
    b9 = Button(root , width=6 , height=3 , bg=colors.colorsyellow[0] , command=lambda:logic(b9))
    b10 = Button(root , width=6 , height=3 , bg=colors.colorsyellow[0] , command=lambda:logic(b10))
    b11 = Button(root , width=6 , height=3 , bg=colors.colorsgreen[0] , command=lambda:logic(b11))
    b12 = Button(root , width=6 , height=3 , bg=colors.colorsgreen[0] , command=lambda:logic(b12)) 
    b13 = Button(root , width=6 , height=3 , bg=colors.colorsgreen[0] , command=lambda:logic(b13))
    b14 = Button(root , width=6 , height=3 , bg=colors.colorsgreen[0] , command=lambda:logic(b14))
    b15 = Button(root , width=6 , height=3 , bg=colors.colorsgreen[0] , command=lambda:logic(b15))
    b16 = Button(root , width=6 , height=3 , bg=colors.colorsblue[0] , command=lambda:logic(b16)) 
    b17 = Button(root , width=6 , height=3 , bg=colors.colorsblue[0] , command=lambda:logic(b17)) 
    b18 = Button(root , width=6 , height=3 , bg=colors.colorsblue[0] , command=lambda:logic(b18)) 
    b19 = Button(root , width=6 , height=3 , bg=colors.colorsblue[0] , command=lambda:logic(b19)) 
    b20 = Button(root , width=6 , height=3 , bg=colors.colorsblue[0] , command=lambda:logic(b20)) 
    b21 = Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b21)) 
    b22 = Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b22)) 
    b23 = Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b23)) 
    b24 = Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b24)) 
    b25 = Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b25)) 
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

def five_five_t():
    global b1 , b2 , b3 , b4 , b5 , b6 , b7 , b8 , b9 , b10 , b11 , b12 , b13 , b14 , b15
    starttext.configure(text="\n Click the buttons to start popping" , font=("Source Code Pro",12))
    button33.pack_forget()
    button44.pack_forget()
    button55.pack_forget()
    button33t.pack_forget()
    button44t.pack_forget()
    button55t.pack_forget()
    gframe = Frame(root , width=345 , height=345 , bg="gray10")
    gframe.pack()
    f1 = Frame(root , width=345 , height=69 , bg=colors.colorsred[0])  
    f2 = Frame(root , width=345 , height=69 , bg=colors.colorsyellow[0])  
    f3 = Frame(root , width=345 , height=69 , bg=colors.colorsgreen[0])  
    f4 = Frame(root , width=345 , height=69 , bg=colors.colorsblue[0])  
    f5 = Frame(root , width=345 , height=69 , bg=colors.colorspurple[0])  
    f1.pack(in_=gframe)
    f2.pack(in_=gframe)
    f3.pack(in_=gframe)
    f4.pack(in_=gframe)
    f5.pack(in_=gframe)
    b1 = Button(root , width=6 , height=3 , bg=colors.colorsred[0] , command=lambda:logic(b1 , b1p , colors.colorsred))
    b2 = Button(root , width=6 , height=3 , bg=colors.colorsyellow[0] , command=lambda:logic(b2 , b2p , colors.colorsyellow))
    b3 = Button(root , width=6 , height=3 , bg=colors.colorsyellow[0] , command=lambda:logic(b3 , b3p , colors.colorsyellow))
    b4 = Button(root , width=6 , height=3 , bg=colors.colorsgreen[0] , command=lambda:logic(b4 , b4p , colors.colorsgreen)) 
    b5 = Button(root , width=6 , height=3 , bg=colors.colorsgreen[0] , command=lambda:logic(b5 , b5p , colors.colorsgreen))
    b6 = Button(root , width=6 , height=3 , bg=colors.colorsgreen[0] , command=lambda:logic(b6 , b6p , colors.colorsgreen))
    b7 = Button(root , width=6 , height=3 , bg=colors.colorsblue[0] , command=lambda:logic(b7 , b7p , colors.colorsblue))
    b8 = Button(root , width=6 , height=3 , bg=colors.colorsblue[0] , command=lambda:logic(b8 , b8p , colors.colorsblue)) 
    b9 = Button(root , width=6 , height=3 , bg=colors.colorsblue[0] , command=lambda:logic(b9 , b9p , colors.colorsblue))
    b10 = Button(root , width=6 , height=3 , bg=colors.colorsblue[0] , command=lambda:logic(b10 , b10p , colors.colorsblue))
    b11 = Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b11 , b11p , colors.colorspurple))
    b12= Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b12 , b12p , colors.colorspurple))
    b13 = Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b13 , b13p , colors.colorspurple))
    b14 = Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b14 , b14p , colors.colorspurple))
    b15 = Button(root , width=6 , height=3 , bg=colors.colorspurple[0] , command=lambda:logic(b15 , b15p , colors.colorspurple))
    b1.pack(in_=f1 , side="left")
    b2.pack(in_=f2 , side="left")
    b3.pack(in_=f2 , side="left")
    b4.pack(in_=f3 , side="left")
    b5.pack(in_=f3 , side="left")
    b6.pack(in_=f3 , side="left")
    b7.pack(in_=f4 , side="left")
    b8.pack(in_=f4 , side="left")
    b9.pack(in_=f4 , side="left")
    b10.pack(in_=f4 , side="left")
    b11.pack(in_=f5 , side="left")
    b12.pack(in_=f5 , side="left")
    b13.pack(in_=f5 , side="left")
    b14.pack(in_=f5 , side="left")
    b15.pack(in_=f5 , side="left")

def pweep_frame():
    global b1 , b2 , b3 , b4 , b5 , b6 
    buttonuc.pack_forget()
    
    buttonpluck.pack_forget()
    starttext.configure(text="\n Click the buttons to know your luck" , font=("Source Code Pro" , 12))
    gframe = Frame(root , width=345 , height=345 , bg="grey10")
    gframe.pack()
    f1 = Frame(root , width=345 , height=115 , bg=colors.colorsred[0])
    f2 = Frame(root , width=345 , height=115 , bg=colors.colorsyellow[0])
    f3 = Frame(root , width=345 , height=115 , bg=colors.colorsblue[0])
    f1.pack(in_=gframe)
    f2.pack(in_=gframe)
    f3.pack(in_=gframe)
    b1 = Button(root , width=12 , height=5 , bg=colors.colorsred[0] , command=mines)
    b2 = Button(root , width=12 , height=5 , bg=colors.colorsyellow[0] , command=mines)
    b3 = Button(root , width=12 , height=5 , bg=colors.colorsyellow[0] , command=mines)
    b4 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=mines) 
    b5 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=mines)
    b6 = Button(root , width=12 , height=5 , bg=colors.colorsblue[0] , command=mines)
    b1.pack(in_=f1 , side="left")
    b2.pack(in_=f2 , side="left")
    b3.pack(in_=f2 , side="left")
    b4.pack(in_=f3 , side="left")
    b5.pack(in_=f3 , side="left")
    b6.pack(in_=f3 , side="left")

def pange_frame():
    global f3 , f4 , b1 , b2 , b3
    buttonuc.pack_forget()
    buttonpluck.pack_forget()
    starttext.configure(text="\n Click the buttons to accept a challenge" , font=("Source Code Pro" , 12))
    grame = Frame(width=345 , height=172 , bg="grey10")
    grame.pack()
    f1 = Frame(width=345 , height=86)
    f2 = Frame(width=345 , height=86)
    f3 = Frame(width=345 , height=115 , bg="gray10")
    f4 = Frame(width=345 , height=86 , bg="gray10")
    f1.pack(in_=grame)
    f2.pack(in_=grame)
    b1 = Button(root , width=6 , height=3 , bg=colors.colorsred[0] , command=palin_gui)
    b2 = Button(root , width=6 , height=3 , bg=colors.colorsorange[0] , state="disabled")
    b3 = Button(root , width=6 , height=3 , bg=colors.colorsorange[0] , state="disabled")
    b1.pack(in_=f1)
    b2.pack(in_=f2, side=LEFT)
    b3.pack(in_=f2 , side=LEFT)
    
def palin_gui():
    global sbmt , lab , entry
    f3.pack()
    lab = Label(root , text="Palindrome:-" , bg="grey10" , fg="antiquewhite" , font=("Source Code Pro" , 12))
    sbmt = Button(root , text="Submit" , bg="slateblue3" , fg="antiquewhite" , width=6 , font=("Source Code Pro" , 12) , command=lambda:pange_games.palindrome(entry.get() , b1 , colors.colorsred)) 
    entry = Entry(root , bg="grey15" , fg="antiquewhite" , insertbackground="antiquewhite" , font=("Source Code Pro" , 12))
    lab.pack(side="left")
    entry.pack(side="left")
    sbmt.pack(side="left")

def arithmetic_gui():
    global sbmt , lab , entry
    test = pange_games.arithmetic_question()
    f3.pack()
    lab = Label(root , text=f"{test[0]} {test[2]} {test[1]} =" , bg="grey10" , fg="antiquewhite" , font=("Source Code Pro" , 12))
    sbmt = Button(root , text="Submit" , bg="slateblue3" , fg="antiquewhite" , width=6 , font=("Source Code Pro" , 12) , command=lambda:pange_games.check_arithmetic(test[0] , test[1] , test[2]  , entry.get() , b2 , colors.colorsyellow)) 
    entry = Entry(root , bg="grey15" , fg="antiquewhite" , insertbackground="antiquewhite" , font=("Source Code Pro" , 12))
    lab.pack(side="left")
    entry.pack(side="left")
    sbmt.pack(side="left")

def guess_gui():
    global sbmt , lab , entry
    f4.pack()
    test = pange_games.guess_question()
    lab = Label(root , text=f"{test[0]} \n Guess color =" , bg="grey10" , fg="antiquewhite" , font=("Source Code Pro" , 12))
    sbmt = Button(root , text="Sub\nmit" , bg="slateblue3" , fg="antiquewhite" , width=6 , height=3, font=("Source Code Pro" , 12) , command=lambda:pange_games.check_question_guess(entry.get() , test[0][test[1]] , b3 , color=colors.colorsyellow)) 
    entry = Entry(root , bg="grey15" , fg="antiquewhite" , insertbackground="antiquewhite" , font=("Source Code Pro" , 12))
    lab.pack(side="left")
    entry.pack(side="left")
    sbmt.pack(side="left")

class pange_games():
    def arithmetic_question():
        n1 = randint(1 , 10)
        n2 = randint(1 , 10)
        opr = randint(1 , 3)
        if opr == 1:
            operation = "+"
        elif opr == 2:
            operation = "-"
        elif opr == 3:
            operation = '*'

        return [n1 , n2 , operation]
        
    def guess_question():
        colos = ["red" , "blue"]
        guess = randint(0 , 1)

        return [colos , guess]
    
    def check_question_guess(choice: str , ans: str , button: Button , color: list):
        f4.pack_forget()
        lab.pack_forget()
        entry.pack_forget()
        sbmt.pack_forget()
        if choice == "":
            showerror("Error" , "No choice detected")
        else:
            if choice == ans:
                showinfo("Congratulations" , "You have passed")
                button.configure(bg=color[1] , state="disabled")
                guessd = True
                if palind == True and guessd == True and arithd == True:
                    showinfo("Congratulations" , "You successfully popped the pop-it")
            else:
                showerror("Error" , "Answer is incorrect")
                button.configure(bg=color[1] , state="disabled")
                guessd = False
                showerror("Error" , "Pop It was not popped sucessfully")

    def check_arithmetic(n1: int , n2: int , operation: str , ans: str , button: Button , color: list):
        global arithd
        f3.pack_forget()
        lab.pack_forget()
        entry.pack_forget()
        sbmt.pack_forget()
        if ans == "":
            showerror("Error" , "No answer detected")
        else:
            if operation == "+":
                if not ans == str(n1+n2):
                    showerror("Error" , "Answer is incorrect")
                    button.configure(bg=color[1] , state="disabled")
                    b3.configure(state="active" , bg=color[0] , command=guess_gui)
                    arithd = False
                else:
                    showinfo("Sucess" , "Answer is correct")
                    button.configure(bg=color[1] , state="disabled")
                    b3.configure(state="active" , bg=color[0] , command=guess_gui)
                    arithd = True 
            elif operation == "-":
                if not ans == str(n1-n2):
                    showerror("Error" , "Answer is not correct")
                    button.configure(bg=color[1] , state="disabled")
                    b3.configure(state="active" , bg=color[0] , command=guess_gui)
                    arithd = False
                else:
                    showinfo("Sucess" , "Answer is correct")
                    button.configure(bg=color[1] , state="disabled")
                    b3.configure(state="active" , bg=color[0] , command=guess_gui)
                    arithd = True
            elif operation == "*":
                if not ans == str(n1*n2):
                    showerror("Error" , "Answer is not correct")
                    button.configure(bg=color[1] , state="disabled")
                    b3.configure(state="active" , bg=color[0] , command=guess_gui)
                    arithd = False
                else:
                    showinfo("Sucess" , "Answer is correct")
                    button.configure(bg=color[1] , state="disabled")
                    b3.configure(state="active" , bg=color[0] , command=guess_gui)
                    arithd = True
                    
    def palindrome(name: str , button: Button , color: list):
        global palind
        f3.pack_forget()
        entry.pack_forget()
        sbmt.pack_forget()
        lab.pack_forget()
        if name == "":
            showerror("Error" , "No name detected")
            button.configure(bg = color[1] , state="disabled")
            palind = False
        else:
            if name == name[:: -1]:
                showinfo("Congratulations" , "The name given above is a palindrome")
                button.configure(bg = color[1] , state="disable")
                palind = True
                b2.configure(bg=colors.colorsyellow[0] , state="active" , command=arithmetic_gui)
            else:
                showerror("Error" , "The given name is not a palindrome")
                button.configure(bg = color[1] , state="disable")
                b2.configure(bg=colors.colorsyellow[0] , state="active" , command=arithmetic_gui)
                palind = False
        
def mines():
    assignednum = randint(1 , 100)
    if assignednum == 1:
        showinfo("Congratulations" , "Your luck is extremely good")
    elif assignednum in range(2 , 10):
        showinfo("Congratulations" , "Your luck is good")
    elif assignednum in range(11 , 75):
        showinfo("Ok" , "Your luck is moderate")
    else:
        showerror("Error" , "Better luck next time")

def logic(button: Button):
    if button["bg"] == colors.colorsred[0]:
        button.configure(bg=colors.colorsred[1])
    elif button["bg"] == colors.colorsred[1]:
        button.configure(bg=colors.colorsred[0])
    elif button["bg"] == colors.colorsyellow[1]:
        button.configure(bg=colors.colorsyellow[0])
    elif button["bg"] == colors.colorsyellow[0]:
        button.configure(bg=colors.colorsyellow[1])
    elif button["bg"] == colors.colorsgreen[0]:
        button.configure(bg=colors.colorsgreen[1])
    elif button["bg"] == colors.colorsgreen[1]:
        button.configure(bg=colors.colorsgreen[0])
    elif button["bg"] == colors.colorsblue[0]:
        button.configure(bg=colors.colorsblue[1])
    elif button["bg"] == colors.colorsblue[1]:
        button.configure(bg=colors.colorsblue[0])
    elif button["bg"] == colors.colorspurple[1]:
        button.configure(bg=colors.colorspurple[0])
    else:
        button.configure(bg=colors.colorspurple[1])

buttonplayt.configure(command=play_start)
buttonplayg.configure(command=play_start_game)
buttonuc.configure(command=pange_frame)
button33.configure(command=three_three)
button44.configure(command=four_four)
button55.configure(command=five_five)
button33t.configure(command=three_three_t)
button44t.configure(command=four_four_t)
button55t.configure(command=five_five_t)

root.mainloop()
