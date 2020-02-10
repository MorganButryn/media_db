#!/usr/bin/python3
#Morgan Butryn
#2020-2-10
"""GUI version of media_db"""
import pickle
import tkinter as tk
from tkinter import scrolledtext

class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        lbl_title = tk.Label(text="Media Database", font=("Verdana", "20"))
        lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        btn_add = tk.Button(text="Add", font=("Verdana", "14"))
        btn_add.grid(row = 1, column = 0)
        btn_edit = tk.Button(text="Edit", font=("Verdana", "14"))
        btn_edit.grid(row = 2, column = 0)
        btn_remove = tk.Button(text="Remove", font=("Verdana", "14"))
        btn_remove.grid(row = 3, column = 0)
        btn_save = tk.Button(text="Save", font=("Verdana", "14"))
        btn_save.grid(row = 4, column = 0)        
#main
if __name__ == "__main__":
    picklefile = open("games.pickle", "rb")
    games = pickle.load(picklefile)
    picklefile.close()
    
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Media Library")
    main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0, sticky = "news")
    root.mainloop()