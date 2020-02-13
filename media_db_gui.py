#!/usr/bin/python3
#Morgan Butryn
#2020-2-10
"""GUI version of media_db"""
import pickle
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.grid_columnconfigure(0, weight = 2)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 2)
        
        #Labels
        self.lbl_title = tk.Label(self, text="Media database", font=("Verdana", "20"))
        self.lbl_title.grid(row = 0, column = 0, columnspan = 3, sticky = "news")
        
        #Buttons
        self.btn_add = tk.Button(self, text="Add", font=("Verdana", "14"))
        self.btn_add.grid(row = 1, column = 1, sticky = "news")
        
        self.btn_edit = tk.Button(self, text="Edit", font=("Verdana", "14"))
        self.btn_edit.grid(row = 2, column = 1, sticky = "news")
        
        self.btn_remove = tk.Button(self, text="Remove", font=("Verdana", "14"))
        self.btn_remove.grid(row = 3, column = 1, sticky = "news")
        
        self.btn_search = tk.Button(self, text="Search", font=("Verdana", "14"))
        self.btn_search.grid(row = 4, column = 1, sticky = "news")  
        
        self.btn_save = tk.Button(self, text="Save", font=("Verdana", "14"))
        self.btn_save.grid(row = 5, column = 1, sticky = "news")
        
        messagebox.showinfo(message = "File saved")
        
class EditMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
        #Labels
        self.lbl_title = tk.Label(self, text="Add/Edit", font=("Verdana", "20"))
        self.lbl_title.grid(row = 0, column = 1, sticky = "news")
        
        self.lbl_notes = tk.Label(self, text="Notes:", font=("Verdana", "14"))
        self.lbl_notes.grid(row = 3, column = 0, sticky = "news")
        
        #Checkbuttons
        self.chk_sp = tk.Checkbutton(self, text="Has Singleplayer?", font=("Verdana", "10"))
        self.chk_sp.grid(row = 2, column = 0, sticky = "news")
        
        self.chk_mp = tk.Checkbutton(self, text="Has Multiplayer?", font=("Verdana", "10"))
        self.chk_mp.grid(row = 2, column = 1, sticky = "news")
        
        self.chk_complete = tk.Checkbutton(self, text="Completed?", font=("Verdana", "10"))
        self.chk_complete.grid(row = 2, column = 2, sticky = "news")
        
        #Scrolltext
        self.scr_notes = ScrolledText(self, height=10, width=40)
        self.scr_notes.grid(row = 6, column = 0, columnspan = 3, sticky = "news")        

class SearchMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)        
        
        #Labels
        self.lbl_title = tk.Label(self, text="Search", font=("Verdana", "20"))
        self.lbl_title.grid(row = 0, column = 1, sticky = "news")
        
        self.lbl_searchby = tk.Label(self, text="Search by:", font=("Verdana", "14"))
        self.lbl_searchby.grid(row = 2, column = 0, sticky = "news")
        
        self.lbl_searchfor = tk.Label(self, text="Search for:", font=("Verdana", "14"))
        self.lbl_searchfor.grid(row = 4, column = 0, sticky = "news")
        
        self.lbl_filters = tk.Label(self, text="Filters", font=("Verdana", "14"))
        self.lbl_filters.grid(row = 1, column = 2, sticky = "news")
        
        #Dropdowns
        self.searchlist = {"genre", "title"}
        self.searchselect = ""

        self.dbx_search = tk.OptionMenu(self, self.searchselect, *self.searchlist)
        self.dbx_search.grid(row = 3, column = 0, sticky = "news")
        
        #Entries
        self.ent_search = tk.Entry(self)
        self.ent_search.grid(row = 5, column = 0, sticky = "news")
        
        #Scrolltext
        self.scr_search = ScrolledText(self, height=10, width=40)
        self.scr_search.grid(row = 6, column = 0, columnspan = 3, sticky = "news")
        
        #Buttons
        self.btn_back = tk.Button(self, text="Back", font=("Verdana", "14"))
        self.btn_back.grid(row = 7, column = 0, sticky = "news")
        
        self.btn_clear = tk.Button(self, text="Clear", font=("Verdana", "14"))
        self.btn_clear.grid(row = 7, column = 1, sticky = "news")
        
        self.btn_submit = tk.Button(self, text="Submit", font=("Verdana", "14"))
        self.btn_submit.grid(row = 7, column = 2, sticky = "news")
        
        #Subframes
        frm_chkbtn = ChkSubframe(self)
        frm_chkbtn.grid(row = 2, column = 1, columnspan = 2, rowspan = 4, sticky = "news")

class ChkSubframe(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
        #Checkbuttons
        self.chk_title = tk.Checkbutton(self, text="Title         ", font=("Verdana","10"))
        self.chk_title.grid(row = 0, column = 0, sticky = "news")
        
        self.chk_genre = tk.Checkbutton(self, text="Genre       ", font=("Verdana","10"))
        self.chk_genre.grid(row = 1, column = 0, sticky = "news")
        
        self.chk_dev = tk.Checkbutton(self, text="Developer", font=("Verdana","10"))
        self.chk_dev.grid(row = 2, column = 0, sticky = "news")
        
        self.chk_pub = tk.Checkbutton(self, text="Publisher  ", font=("Verdana","10"))
        self.chk_pub.grid(row = 3, column = 0, sticky = "news")
        
        self.chk_platform = tk.Checkbutton(self, text="Platform          ", font=("Verdana","10"))
        self.chk_platform.grid(row = 0, column = 1, sticky = "news")
        
        self.chk_release = tk.Checkbutton(self, text="Release           ", font=("Verdana","10"))
        self.chk_release.grid(row = 1, column = 1, sticky = "news")
        
        self.chk_purchase = tk.Checkbutton(self, text="Purchase date ", font=("Verdana","10"))
        self.chk_purchase.grid(row = 2, column = 1, sticky = "news")
        
        self.chk_price = tk.Checkbutton(self, text="Purchase price", font=("Verdana","10"))
        self.chk_price.grid(row = 3, column = 1, sticky = "news")
        
        self.chk_sp = tk.Checkbutton(self, text="Singleplayer?", font=("Verdana","10"))
        self.chk_sp.grid(row = 0, column = 2, sticky = "news")
        
        self.chk_mp = tk.Checkbutton(self, text="Multiplayer?  ", font=("Verdana","10"))
        self.chk_mp.grid(row = 1, column = 2, sticky = "news")
        
        self.chk_complete = tk.Checkbutton(self, text="Completed?   ", font=("Verdana","10"))
        self.chk_complete.grid(row = 2, column = 2, sticky = "news")
        
        self.chk_rating = tk.Checkbutton(self, text="Rating            ", font=("Verdana","10"))
        self.chk_rating.grid(row = 3, column = 2, sticky = "news")

#main
if __name__ == "__main__":
    picklefile = open("games.pickle", "rb")
    games = pickle.load(picklefile)
    picklefile.close()
    
    root = tk.Tk()
    root.geometry("500x400")
    root.title("Media Library")
    main_menu = EditMenu()
    main_menu.grid(row = 0, column = 0, sticky = "news")
    root.grid_columnconfigure(0, weight = 1)
    root.mainloop()