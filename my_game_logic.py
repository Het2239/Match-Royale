from tkinter import *
import random
from tkinter import messagebox
from PIL import ImageTk,Image
import pygame
import time
# creating a pygame mixer for adding sound effects
pygame.mixer.init()
root=Tk()

root.title("Match Royale")
ico = Image.open('images//Naruto.jpg')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.state("zoomed")
bg_image=ImageTk.PhotoImage(Image.open("images\\narutobg1.jpg"))
bg_label=Label(root,image=bg_image)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

# class that contains the logic for the game
class GameLogic:
    
    def __init__(self, valist):
        self.valist = valist
        self.root = root
        
        self.alabel = Label(self.root, text="",font=("OCR A Extended","20"),bg="black",fg="white")
        self.mlabel = Label(self.root, text="",font=("OCR A Extended","20"),bg="black",fg="white")
        self.alabel.place(x=665,y=700)
        self.mlabel.pack()
        self.label_var = StringVar()
        self.label_var.set("Time: 0 s")
        self.label = Label(self.root, textvariable=self.label_var, font=("OCR A Extended", 30),bg="black",fg="white")
        self.label.pack(pady=20)
        random.shuffle(self.valist)

        
        self.timer_running = False
        self.start_time = None

    counter = 0
    running = False

    # method to start the stopwatch
    def start_timer(self):
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True
            self.update_timer()

    # method to contionuously update the stopwatch label on game screen
    def update_timer(self):
        if self.timer_running:
            elapsed_time = int(time.time() - self.start_time)
            self.label_var.set(f"Time: {elapsed_time} s")
            self.root.after(1000, self.update_timer)

    # method to stop the stopwatch
    def stop_timer(self):
        global completion_time
        if self.timer_running:
            self.timer_running = False
            completion_time = int(time.time() - self.start_time)
            self.label_var.set(f"Final Time: {completion_time} s")
            print(f"Game finished in {completion_time} seconds!")

    # method returns elapsed time for use in the ui file        
    def gametime():
        global completion_time
        return completion_time
    
    # method to reset the stopwatch
    def reset(self):
        global counter, running
        self.running = False
        self.counter = 0
        self.label_var.set("0 s")


    alist = list()
    adict = dict()
    counter = 0
    matchmoves = 0
    gamemoves = 0

    img1 = ImageTk.PhotoImage(Image.open("images\\aburame new 80.jpg"))
    img2 = ImageTk.PhotoImage(Image.open("images\\akimichi new 80.jpg"))
    img3 = ImageTk.PhotoImage(Image.open("images\\hatake new 80.jpg"))
    img4 = ImageTk.PhotoImage(Image.open("images\\izunaka new 80.jpg"))
    img5 = ImageTk.PhotoImage(Image.open("images\\namikaze new 80.jpg"))
    img6 = ImageTk.PhotoImage(Image.open("images\\nara new 80.jpg"))
    img7 = ImageTk.PhotoImage(Image.open("images\\yamanka new 80.jpg"))
    img8 = ImageTk.PhotoImage(Image.open("images\\otsutsuki new 80.jpg"))
    img9 = ImageTk.PhotoImage(Image.open("images\\senju new 80.jpg"))
    img10 = ImageTk.PhotoImage(Image.open("images\\tushi newt 80.jpg"))
    img11 = ImageTk.PhotoImage(Image.open("images\\uchiha new 80.jpg"))
    img12 = ImageTk.PhotoImage(Image.open("images\\uzumaki new 80.jpg"))
    imb = ImageTk.PhotoImage(Image.open("images\\blank 80.jpg"))

    # sound effect for correct match
    def match_found(self):
        pygame.mixer.music.load("soundtracks\\match found.mp3")
        pygame.mixer.music.play(loops=0)

    # sound effect for incorrect match
    def error_sound(self):
        pygame.mixer.music.load("soundtracks\\error sound.mp3")
        pygame.mixer.music.play(loops=0)
    
    # command when a tile is flipped 
    # it also consists the main logic of the game
    def clk(self, tn, val):
        global alist, adict, counter, matchmoves, gamemoves

        if tn["text"] == ' ' and self.counter < 2:
            tn['text'] = val
            tn['image'] = self.valist[val]
            self.alist.append(val)
            self.adict[tn] = self.valist[val]
            self.counter += 1
            self.matchmoves += 1

            
            if self.matchmoves == 1:
                self.start_timer()

        if len(self.alist) == 2:
            if self.valist[self.alist[0]] == self.valist[self.alist[1]]:
                self.alabel.config(text=' Match\n Found')
                self.match_found()
                self.gamemoves += 1
                self.counter = 0
                self.alist = list()
                for key in self.adict:
                    key['state'] = 'disabled'
                self.adict = dict()
            else:
                self.alabel.config(text='Wasted')
                self.error_sound()
                self.root.after(500,self.reverse)

            if self.gamemoves == 12:
                self.alabel.config(text='  Game\n  Over')
                root.after(2000,self.closeWin)
                
                global moves
                moves=self.matchmoves
                self.stop_timer()
                
                



        self.mlabel.config(text=f'Moves: {self.matchmoves // 2}')
    def closeWin(self):
        import main
        self.root.destroy()
        
    def mmoves():
        global moves
        return moves
    def reverse(self):
        self.counter = 0
        self.alist = list()
        for key in self.adict:
            key['image'] = self.imb
            key['text'] = ' '
        self.adict = dict()
img1=ImageTk.PhotoImage(Image.open("images\\aburame new 80.jpg"))
img2=ImageTk.PhotoImage(Image.open("images\\akimichi new 80.jpg"))
img3=ImageTk.PhotoImage(Image.open("images\\hatake new 80.jpg"))
img4=ImageTk.PhotoImage(Image.open("images\\izunaka new 80.jpg"))
img5=ImageTk.PhotoImage(Image.open("images\\namikaze new 80.jpg"))
img6=ImageTk.PhotoImage(Image.open("images\\nara new 80.jpg"))
img7=ImageTk.PhotoImage(Image.open("images\\yamanka new 80.jpg"))
img8=ImageTk.PhotoImage(Image.open("images\\otsutsuki new 80.jpg"))
img9=ImageTk.PhotoImage(Image.open("images\\senju new 80.jpg"))
img10=ImageTk.PhotoImage(Image.open("images\\tushi newt 80.jpg"))
img11=ImageTk.PhotoImage(Image.open("images\\uchiha new 80.jpg"))
img12=ImageTk.PhotoImage(Image.open("images\\uzumaki new 80.jpg"))
imgNaruto=ImageTk.PhotoImage(Image.open("images\\match royale 105.jpg"))
# creating an object of the class GameLogic
a=GameLogic([img1,img1,img2,img2,img3,img3,img4,img4,img5,img5,img6,img6,img7,img7,img8,img8,img9,img9,img10,img10,img11,img11,img12,img12])
my_frame1=Frame(root,background="dark grey")
my_frame1.pack()
imb=ImageTk.PhotoImage(Image.open("images\\blank 80.jpg"))
# overall design of game screen
t0=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t0,0),height=100,width=100,bg='white')
t1=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t1,1),height=100,width=100,bg='white')
t2=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t2,2),height=100,width=100,bg='white')
t3=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t3,3),height=100,width=100,bg='white')
t4=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t4,4),height=100,width=100,bg='white')
t5=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t5,5),height=100,width=100,bg='white')
t6=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t6,6),height=100,width=100,bg='white')
t7=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t7,7),height=100,width=100,bg='white')
t8=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t8,8),height=100,width=100,bg='white')
t9=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t9,9),height=100,width=100,bg='white')
t10=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t10,10),height=100,width=100,bg='white')
t11=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t11,11),height=100,width=100,bg='white')
t12=Label(my_frame1,text=' ',image=imgNaruto)
t13=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t13,12),height=100,width=100,bg='white')
t14=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t14,13),height=100,width=100,bg='white')
t15=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t15,14),height=100,width=100,bg='white')
t16=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t16,15),height=100,width=100,bg='white')
t17=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t17,16),height=100,width=100,bg='white')
t18=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t18,17),height=100,width=100,bg='white')
t19=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t19,18),height=100,width=100,bg='white')
t20=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t20,19),height=100,width=100,bg='white')
t21=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t21,20),height=100,width=100,bg='white')
t22=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t22,21),height=100,width=100,bg='white')
t23=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t23,22),height=100,width=100,bg='white')
t24=Button(my_frame1,text=' ',image=imb, command=lambda : a.clk(t24,23),height=100,width=100,bg='white')


t0.grid(row=0,column=0,padx=2,pady=2)
t1.grid(row=0,column=1,padx=2,pady=2)
t2.grid(row=0,column=2,padx=2,pady=2)
t3.grid(row=0,column=3,padx=2,pady=2)
t4.grid(row=0,column=4,padx=2,pady=2)

t5.grid(row=1,column=0,padx=2,pady=2)
t6.grid(row=1,column=1,padx=2,pady=2)
t7.grid(row=1,column=2,padx=2,pady=2)
t8.grid(row=1,column=3,padx=2,pady=2)
t9.grid(row=1,column=4,padx=2,pady=2)

t10.grid(row=2,column=0,padx=2,pady=2)
t11.grid(row=2,column=1,padx=2,pady=2)
t12.grid(row=2,column=2,padx=2,pady=2)
t13.grid(row=2,column=3,padx=2,pady=2)
t14.grid(row=2,column=4,padx=2,pady=2)

t15.grid(row=3,column=0,padx=2,pady=2)
t16.grid(row=3,column=1,padx=2,pady=2)
t17.grid(row=3,column=2,padx=2,pady=2)
t18.grid(row=3,column=3,padx=2,pady=2)
t19.grid(row=3,column=4,padx=2,pady=2)

t20.grid(row=4,column=0,padx=2,pady=2)
t21.grid(row=4,column=1,padx=2,pady=2)
t22.grid(row=4,column=2,padx=2,pady=2)
t23.grid(row=4,column=3,padx=2,pady=2)
t24.grid(row=4,column=4,padx=2,pady=2)





root.mainloop()