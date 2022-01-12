#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 18:14:33 2022

@author: clockshield
"""


from tkinter import *
import random
from PIL import ImageTk, Image
root=Tk()
root.title("lol")
root.geometry("600x400")
root.config(bg="yellow")

img = ImageTk.PhotoImage(Image.open ("dice copy.png"))
label_player1 = Label(root, text = "Player 1", bg = "royal blue", fg = "white")
label_player1.place(relx = 0.2, rely = 0.3, anchor=CENTER)

label_player2 = Label(root, text = "Player 2", bg = "royal blue", fg = "white")
label_player2.place(relx = 0.8, rely = 0.3, anchor=CENTER)

label_score1 = Label(root, bg = "royal blue", fg = "white")
label_score1.place(relx = 0.2, rely = 0.4, anchor=CENTER)

label_score2 = Label(root, bg = "royal blue", fg = "white")
label_score2.place(relx = 0.8, rely = 0.4, anchor=CENTER)

label_randomdice = Label(root, text = "Random Dice", bg = "orange", fg = "white")
label_randomdice.place(relx = 0.5, rely = 0.3, anchor=CENTER)
player1_score = 0
def player1():
    global player1_score
    random_num = random.randint(1, 6)
    player1_score = player1_score + random_num
    label_score1["text"] = str(player1_score)
    label_randomdice["text"] = "Player 1 rolled " + str(random_num)

btn1 = Button(root, image = img, command = player1)
btn1.place(relx = 0.2, rely = 0.8, anchor=CENTER)

player2_score = 0
def player2():
    global player2_score
    random_num1 = random.randint(1, 6)
    player2_score = player2_score + random_num1
    label_score2["text"] = str(player2_score)
    label_randomdice["text"] = "Player 2 rolled " + str(random_num1)

btn1 = Button(root, image = img, command = player2)
btn1.place(relx = 0.8, rely = 0.8, anchor=CENTER)





root.mainloop()