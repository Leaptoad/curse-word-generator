import random

import os

import sys

import subprocess

import time

import tkinter as tk

root=tk.Tk()
root.config(bg = "#F0F8FF")
root.geometry('700x400')
root.title("Random Curse Word Generator")



def generate_curse_word():
    first_part = ('Ass', 'Fuck', 'Cock', 'Tampon', 'Shit', 'Penis', 'Juice', 'Ball', 'Jizz', 'Cum', 'Fanny', 'Dick','Bitch', 'Douche','Fart', 'Nut', 'Gina', 'Piss', 'Whore', 'Slut', 'Mother', 'Sissy', 'Wench', 'Crap', 'Nipple', 'Anus', 'Jerk', 'Trash', 'Tit', 'Snot', 'Scum', 'Diaper', 'Granny', 'Pecker', 'Cooch', 'Twat', 'Mouth', 'Rectum', 'Wiener', 'Cunt', 'Fetus', 'Clit', 'Ho', 'Schlong', 'Sack', 'Meat', 'Pussy', 'Testicle', 'Dildo', 'Prick', 'Scrotum', 'Muff', 'Panty', 'Pube', 'Sperm', 'Poop', 'Butt', 'Pork', 'Feces', 'Beef', 'Queef', 'Clown', 'Virgin', 'Clout', 'Juggalo', 'Pie', 'Spaz')
    second_part = (' ')
    third_part = ('Chunk', 'Bagger', 'Flaps', 'Licker', 'Munch', 'Sucker', 'Waffle', 'Eater', 'Face','Biter', 'Bucket', 'Monkey', 'Dumpster', 'Jacket', 'Junkie', 'Chomper', 'Lips', 'Fucker', 'Blower', 'Donkey', 'Monster', 'Wad', 'Jockey', 'Dangler', 'Skank', 'Pooper', 'Farm', 'Lover' , ' Shitter', 'Hole', 'Pincher', 'Beater', 'Sniffer', 'Wipe', 'Twister', 'Slammer', 'Folds', 'Clot', 'Glob', 'Jammer', 'Fondler', 'Tickler', 'Fungus', 'Plug', 'Packer', 'Wrangler', 'Slime', 'Diddler', 'Sandwich', 'Gobbler', 'Wanker', 'Muncher', 'Stain', 'Boner', 'Nugget', 'Booger', 'Rag', 'Basket', 'Burger', 'Biscuit', 'Bandit', 'Gargler', 'Tugger', 'Cabbage', 'Brick', 'Cop', 'Cuck') 
    label.config(text=random.choice(first_part) + (second_part) + (random.choice(third_part)))
    time.sleep(.5)


label= tk.Label(root, text="", font=("Arial", 52))
label.pack(padx=10, pady=65)
label.config(bg = '#F0F8FF')
label.config(fg = '#000000')

button=tk.Button(root, text="Curse!", font=("Arial", 40), command=generate_curse_word)
button.pack(padx=10, pady=50)


root.mainloop()


