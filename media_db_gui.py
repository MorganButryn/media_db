#!/usr/bin/python3
#Morgan Butryn
#2020-2-10
"""GUI version of media_db"""
import pickle
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

class Screen(tk.Frame):
    current = 0
    def __init__(self):
        tk.Frame.__init__(self)

class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
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
        
class EditMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
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
        
        #Frames
        self.frm_lblent = EntSubframe(self)
        self.frm_lblent.grid(row = 1, column = 0, columnspan = 3)
        
        #Buttons
        self.btn_back = tk.Button(self, text="Back", font=("Verdana","14"))
        self.btn_back.grid(row = 7, column = 0)
        
        self.btn_clear = tk.Button(self, text="Clear", font=("Verdana","14"))
        self.btn_clear.grid(row = 7, column = 1)
        
        self.btn_submit = tk.Button(self, text="Submit", font=("Verdana","14"))
        self.btn_submit.grid(row = 7, column = 2)

class SearchMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
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
        
        self.chk_plat = tk.Checkbutton(self, text="Platform          ", font=("Verdana","10"))
        self.chk_plat.grid(row = 0, column = 1, sticky = "news")
        
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

class EntSubframe(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        
        #Labels
        self.lbl_title = tk.Label(self, text="Title:", font=("Verdana","10"))
        self.lbl_title.grid(row = 0, column = 0)
        
        self.lbl_genre = tk.Label(self, text="Genre:", font=("Verdana","10"))
        self.lbl_genre.grid(row = 1, column = 0)
        
        self.lbl_dev = tk.Label(self, text="Developer:", font=("Verdana","10"))
        self.lbl_dev.grid(row = 2, column = 0)
        
        self.lbl_pub = tk.Label(self, text="Publisher:", font=("Verdana","10"))
        self.lbl_pub.grid(row = 3, column = 0)
        
        self.lbl_plat = tk.Label(self, text="Platform:", font=("Verdana","10"))
        self.lbl_plat.grid(row = 4, column = 0)
        
        self.lbl_release = tk.Label(self, text="Release year:", font=("Verdana","10"))
        self.lbl_release.grid(row = 0, column = 2)
        
        self.lbl_purchase = tk.Label(self, text="Purchase date:", font=("Verdana","10"))
        self.lbl_purchase.grid(row = 1, column = 2)
        
        self.lbl_price = tk.Label(self, text="Purchase price:", font=("Verdana","10"))
        self.lbl_price.grid(row = 2, column = 2)
        
        self.lbl_rating = tk.Label(self, text="Rating:", font=("Verdana","10"))
        self.lbl_rating.grid(row = 3, column = 2)
        
        #Entries
        self.ent_title = tk.Entry(self, font=("Verdana","10"))
        self.ent_title.grid(row = 0, column = 1)
        
        self.ent_genre = tk.Entry(self, font=("Verdana","10"))
        self.ent_genre.grid(row = 1, column = 1)
        
        self.ent_dev = tk.Entry(self, font=("Verdana","10"))
        self.ent_dev.grid(row = 2, column = 1)
        
        self.ent_pub = tk.Entry(self, font=("Verdana","10"))
        self.ent_pub.grid(row = 3, column = 1)
        
        self.ent_plat = tk.Entry(self, font=("Verdana","10"))
        self.ent_plat.grid(row = 4, column = 1)
        
        self.ent_release = tk.Entry(self, font=("Verdana","10"))
        self.ent_release.grid(row = 0, column = 3)
        
        self.ent_purchase = tk.Entry(self, font=("Verdana","10"))
        self.ent_purchase.grid(row = 1, column = 3)
        
        self.ent_price = tk.Entry(self, font=("Verdana","10"))
        self.ent_price.grid(row = 2, column = 3)
        
        self.ent_rating = tk.Entry(self, font=("Verdana","10"))
        self.ent_rating.grid(row = 3, column = 3)

#main
if __name__ == "__main__":
    picklefile = open("games.pickle", "rb")
    games = pickle.load(picklefile)
    picklefile.close()
    
    root = tk.Tk()
    root.geometry("500x420")
    root.title("Media Library")
    screens = [MainMenu(), SearchMenu(), EditMenu()]
    #Main Menu = screens[0]
    #Search Menu = screens[1]
    #Edit Menu = screens[2]
    screens[0].grid(row = 0, column = 0, sticky = "news")
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    
    screens[2].tkraise()
    
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)
    root.mainloop()