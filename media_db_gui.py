#!/usr/bin/python3
#Morgan Butryn
#2020-2-10
"""GUI version of media_db"""
import pickle
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

"""class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        
        
        lbl_title = tk.Label(text="Media database", font=("Verdana", "20"))
        lbl_title.grid(row = 0, column = 1, columnspan = 3, sticky = "news")
        
        btn_add = tk.Button(text="Add", font=("Verdana", "14"))
        btn_add.grid(row = 1, column = 1)
        
        btn_edit = tk.Button(text="Edit", font=("Verdana", "14"))
        btn_edit.grid(row = 2, column = 1)
        
        btn_remove = tk.Button(text="Remove", font=("Verdana", "14"))
        btn_remove.grid(row = 3, column = 1)
        
        btn_search = tk.Button(text="Search", font=("Verdana", "14"))
        btn_search.grid(row = 4, column = 1)  
        
        btn_save = tk.Button(text="Save", font=("Verdana", "14"))
        btn_save.grid(row = 5, column = 1)"""
        
"""class EditMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)"""
        
        

class SearchMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        lbl_title = tk.Label(text="Search", font=("Verdana", "20"))
        lbl_title.grid(row = 0, column = 1, sticky = "news")
        
        lbl_searchby = tk.Label(text="Search by:", font=("Verdana", "14"))
        lbl_searchby.grid(row = 1, column = 0, sticky = "news")
        
        lbl_searchfor = tk.Label(text="Search for:", font=("Verdana", "14"))
        lbl_searchfor.grid(row = 3, column = 0, sticky = "news")
        
        self.searchlist = {"genre", "title"}
        self.searchselect = ""

        dbx_search = tk.OptionMenu(self.searchselect, *self.searchlist)
        dbx_search.grid(row = 2, column = 0, sticky = "news")

#main
if __name__ == "__main__":
    picklefile = open("games.pickle", "rb")
    games = pickle.load(picklefile)
    picklefile.close()
    
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Media Library")
    main_menu = SearchMenu()
    main_menu.grid(row = 0, column = 0, sticky = "news")
    root.mainloop()