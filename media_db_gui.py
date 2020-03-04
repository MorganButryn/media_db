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
        
    def switch_frame():
        screens[Screen.current].tkraise()
        
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
        self.btn_add = tk.Button(self, text="Add", font=("Verdana", "14"), command=self.go_add)
        self.btn_add.grid(row = 1, column = 1, sticky = "news")
        
        self.btn_edit = tk.Button(self, text="Edit", font=("Verdana", "14"), command=self.go_edit)
        self.btn_edit.grid(row = 2, column = 1, sticky = "news")
        
        self.btn_remove = tk.Button(self, text="Remove", font=("Verdana", "14"))
        self.btn_remove.grid(row = 3, column = 1, sticky = "news")
        
        self.btn_search = tk.Button(self, text="Search", font=("Verdana", "14"), command=self.go_search)
        self.btn_search.grid(row = 4, column = 1, sticky = "news")  
        
        self.btn_save = tk.Button(self, text="Save", font=("Verdana", "14"), command=self.save)
        self.btn_save.grid(row = 5, column = 1, sticky = "news")
        
    def go_add(self):
        screens[2].edit_key = 0
        screens[2].clear_entry()
        Screen.current = 2
        Screen.switch_frame()
        
        
    def go_search(self):
        Screen.current = 1
        Screen.switch_frame()
        
    def save(self):
        picklefile = open("games.pickle", "wb")
        pickle.dump(games, picklefile)
        picklefile.close()
        messagebox.showinfo(message = "File saved")
    
    def go_edit(self):
        popup = tk.Tk()
        popup.title("Edit/Remove")
        
        frm_select = SelectMenu(popup)
        frm_select.grid(row = 0, column = 0)
        #Screen.current = 3
        #Screen.switch_frame()
        #screens[Screen.current].grid(row = 0, column = 0, sticky = "news")
        
class EditMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
        self.edit_key = 0
        
        self.sp_var = tk.BooleanVar(self)
        self.mp_var = tk.BooleanVar(self)
        self.comp_var = tk.BooleanVar(self)
        
        #Labels
        self.lbl_title = tk.Label(self, text="Add/Edit", font=("Verdana", "20"))
        self.lbl_title.grid(row = 0, column = 1, sticky = "news")
        
        self.lbl_notes = tk.Label(self, text="Notes:", font=("Verdana", "14"))
        self.lbl_notes.grid(row = 3, column = 0, sticky = "news")
        
        #Checkbuttons
        self.chk_sp = tk.Checkbutton(self, text="Has Singleplayer?", font=("Verdana", "10"), variable= self.sp_var, selectcolor = "Black")
        self.chk_sp.grid(row = 2, column = 0, sticky = "news")
        
        self.chk_mp = tk.Checkbutton(self, text="Has Multiplayer?", font=("Verdana", "10"), variable= self.mp_var, selectcolor = "Black")
        self.chk_mp.grid(row = 2, column = 1, sticky = "news")
        
        self.chk_complete = tk.Checkbutton(self, text="Completed?", font=("Verdana", "10"), variable= self.comp_var, selectcolor = "Black")
        self.chk_complete.grid(row = 2, column = 2, sticky = "news")
        
        #Scrolltext
        self.scr_notes = ScrolledText(self, height=10, width=40)
        self.scr_notes.grid(row = 6, column = 0, columnspan = 3, sticky = "news")
        
        #Frames
        self.frm_lblent = EntSubframe(self)
        self.frm_lblent.grid(row = 1, column = 0, columnspan = 3)
        
        #Buttons
        self.btn_back = tk.Button(self, text="Back", font=("Verdana","14"), command=self.go_back)
        self.btn_back.grid(row = 7, column = 0)
        
        self.btn_clear = tk.Button(self, text="Clear", font=("Verdana","14"), command=self.clear_entry)
        self.btn_clear.grid(row = 7, column = 1)
        
        self.btn_submit = tk.Button(self, text="Submit", font=("Verdana","14"), command=self.submit_edit)
        self.btn_submit.grid(row = 7, column = 2)
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def clear_entry(self):
        self.frm_lblent.ent_title.delete(0,"end")
        self.frm_lblent.ent_genre.delete(0,"end")
        self.frm_lblent.ent_dev.delete(0,"end")
        self.frm_lblent.ent_pub.delete(0,"end")
        self.frm_lblent.ent_release.delete(0,"end")
        self.frm_lblent.ent_plat.delete(0,"end")
        self.frm_lblent.ent_purchase.delete(0,"end")
        self.frm_lblent.ent_price.delete(0,"end")
        self.frm_lblent.ent_rating.delete(0,"end")
        self.scr_notes.delete(0.0,"end")
        self.sp_var.set(False)
        self.mp_var.set(False)
        self.comp_var.set(False)
        
    def edit_update(self):
        self.clear_entry()
        
        if self.edit_key > 0:
            entry = games[self.edit_key]

        self.frm_lblent.ent_title.insert(0,entry[0])
        self.frm_lblent.ent_genre.insert(0,entry[1])                
        self.frm_lblent.ent_dev.insert(0,entry[2])
        self.frm_lblent.ent_pub.insert(0,entry[3])                
        self.frm_lblent.ent_release.insert(0,entry[4])
        self.frm_lblent.ent_plat.insert(0,entry[5])
        self.frm_lblent.ent_purchase.insert(0,entry[6])
        self.frm_lblent.ent_price.insert(0,entry[7])
        self.frm_lblent.ent_rating.insert(0,entry[11])        
        self.scr_notes.insert(0.0,entry[12])
        
    def submit_edit(self):
        entry = []
        entry.append(self.frm_lblent.ent_title.get())
        entry.append(self.frm_lblent.ent_genre.get())
        entry.append(self.frm_lblent.ent_dev.get())
        entry.append(self.frm_lblent.ent_pub.get())
        entry.append(self.frm_lblent.ent_release.get())
        entry.append(self.frm_lblent.ent_plat.get())
        entry.append(self.frm_lblent.ent_purchase.get())
        entry.append(self.frm_lblent.ent_price.get())
        
        if self.sp_var.get() == True:
            entry.append("True")
        else:
            entry.append("False")
            
        if self.mp_var.get() == True:
            entry.append("True")
        else:
            entry.append("False")
            
        if self.comp_var.get() == True:
            entry.append("True")
        else:
            entry.append("False")
            
        entry.append(self.frm_lblent.ent_rating.get())
        
        entry.append("")
        #TODO: append checkboxes/scrolltext
        if self.edit_key > 0:
            games[self.edit_key] = entry
            messagebox.showinfo(message = "Item '" +entry[0]+"' edited")
        else:
            games[len(games.keys()) +1] = entry
            messagebox.showinfo(message = "Item '" +entry[0]+"' added")

        Screen.current=0
        Screen.switch_frame()    

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
        
        self.lbl_filters = tk.Label(self, text="Display filters", font=("Verdana", "14"))
        self.lbl_filters.grid(row = 1, column = 2, sticky = "news")
        
        #Dropdowns
        self.options = ["Add", "Title", "Genre", "Developer", "Publisher"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(self.options[0])

        self.dbx_search = tk.OptionMenu(self, self.tkvar, *self.options)
        self.dbx_search.grid(row = 3, column = 0, sticky = "news")
        
        #Entries
        self.ent_search = tk.Entry(self)
        self.ent_search.grid(row = 5, column = 0, sticky = "news")
        
        #Scrolltext
        self.scr_search = ScrolledText(self, height=10, width=40)
        self.scr_search.grid(row = 6, column = 0, columnspan = 3, sticky = "news")
        
        #Buttons
        self.btn_back = tk.Button(self, text="Back", font=("Verdana", "14"), command=self.go_back)
        self.btn_back.grid(row = 7, column = 0, sticky = "news")
        
        self.btn_clear = tk.Button(self, text="Clear", font=("Verdana", "14"), command = self.clear_search)
        self.btn_clear.grid(row = 7, column = 1, sticky = "news")
        
        self.btn_submit = tk.Button(self, text="Submit", font=("Verdana", "14"), command=self.print_search)
        self.btn_submit.grid(row = 7, column = 2, sticky = "news")
        
        #Subframes
        self.frm_chkbtn = ChkSubframe(self)
        self.frm_chkbtn.grid(row = 2, column = 1, columnspan = 2, rowspan = 4, sticky = "news")
        
        self.print_search()
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def clear_search(self):
        self.scr_search.configure(state="normal")
        self.scr_search.delete(0.0, "end")
        self.scr_search.configure(state="disabled")
        self.ent_search.delete(0, "end")
        self.frm_chkbtn.title_bool.set(False)
        self.frm_chkbtn.genre_bool.set(False)
        self.frm_chkbtn.dev_bool.set(False)
        self.frm_chkbtn.pub_bool.set(False)
        self.frm_chkbtn.plat_bool.set(False)
        self.frm_chkbtn.rel_bool.set(False)
        self.frm_chkbtn.pur_bool.set(False)
        self.frm_chkbtn.price_bool.set(False)
        self.frm_chkbtn.sp_bool.set(False)
        self.frm_chkbtn.mp_bool.set(False)
        self.frm_chkbtn.comp_bool.set(False)
        self.frm_chkbtn.rate_bool.set(False)        
        
    def print_search(self):
        self.scr_search.configure(state="normal")
        self.scr_search.delete(0.0, "end")
        for key in games.keys():
            entry = games[key]
            
            if self.tkvar.get() == "All":
                pass
            if self.tkvar.get() == 
            
            if self.frm_chkbtn.title_bool.get() == True:
                msg = entry[0] + "\n"
                self.scr_search.insert("insert", msg)
                
            if self.frm_chkbtn.genre_bool.get() == True:
                msg = entry[1] + "\n"
                self.scr_search.insert("insert", msg)
                
            if self.frm_chkbtn.dev_bool.get() == True:
                msg = entry[2] + "\n"
                self.scr_search.insert("insert", msg)
                
            if self.frm_chkbtn.pub_bool.get() == True:
                msg = entry[3] + "\n"
                self.scr_search.insert("insert", msg)
                
            if self.frm_chkbtn.rel_bool.get() == True:
                msg = entry[4] + "\n"
                self.scr_search.insert("insert", msg)
                
            if self.frm_chkbtn.plat_bool.get() == True:
                msg = entry[5] + "\n"
                self.scr_search.insert("insert", msg)
                
            if self.frm_chkbtn.pur_bool.get() == True:
                msg = entry[6] + "\n"
                self.scr_search.insert("insert", msg)
                
            if self.frm_chkbtn.price_bool.get() == True:
                msg = entry[7] + "\n"
                self.scr_search.insert("insert", msg)
                
            if self.frm_chkbtn.sp_bool.get() == True:
                msg = entry[8] + "\n"
                self.scr_search.insert("insert", msg)
                
            if self.frm_chkbtn.mp_bool.get() == True:
                msg = entry[9] + "\n"
                self.scr_search.insert("insert", msg)
                
            if self.frm_chkbtn.comp_bool.get() == True:
                msg = entry[10] + "\n"
                self.scr_search.insert("insert", msg)
            
            if self.frm_chkbtn.rate_bool.get() == True:
                msg = entry[11] + "\n"
                self.scr_search.insert("insert", msg)
                
            self.scr_search.configure(state="disabled")

class SelectMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        self.parent = parent
        #Labels
        self.lbl_title = tk.Label(self, text="Select a title:", font=("Verdana", "14"))
        self.lbl_title.grid(row = 0, column = 0, sticky = "news", columnspan = 2)
        
        #Dropdowns
        self.options = ["Select a title"]
        
        for key in games.keys():
            self.options.append(games[key][0]) #appends key title to options
            
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(self.options[0])

        self.dbx_item = tk.OptionMenu(self, self.tkvar, *self.options)
        self.dbx_item.grid(row = 1, column = 0, sticky = "news", columnspan = 2)
        
        #Buttons
        self.btn_back = tk.Button(self, text="Back", font=("Verdana", "14"), command = parent.destroy)
        self.btn_back.grid(row = 2, column = 0, sticky = "news")
        self.btn_submit = tk.Button(self, text="Submit", font=("Verdana", "14"), command = self.go_edit)
        self.btn_submit.grid(row = 2, column = 1, sticky = "news")
        
    
    def go_edit(self):
        if self.tkvar.get() != self.options[0]: #reversed condition from lecture example
            for i in range(len(self.options)):
                if self.tkvar.get() == self.options[i]:
                    screens[2].edit_key = i
                    screens[2].edit_update()
                    break
            self.parent.destroy()
            Screen.current = 2
            Screen.switch_frame()
        else:
            messagebox.showinfo(message = "Select a title")

class ChkSubframe(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        
        #Bool_vars
        self.title_bool = tk.BooleanVar(self)
        self.genre_bool = tk.BooleanVar(self)
        self.dev_bool = tk.BooleanVar(self)
        self.pub_bool = tk.BooleanVar(self)
        self.plat_bool = tk.BooleanVar(self)
        self.rel_bool = tk.BooleanVar(self)
        self.pur_bool = tk.BooleanVar(self)
        self.price_bool = tk.BooleanVar(self)
        self.sp_bool = tk.BooleanVar(self)
        self.mp_bool = tk.BooleanVar(self)
        self.comp_bool = tk.BooleanVar(self)
        self.rate_bool = tk.BooleanVar(self)
        
        
        #Checkbuttons
        self.chk_title = tk.Checkbutton(self, text="Title         ",
                                        font=("Verdana","10"),variable = self.title_bool, selectcolor = "Black")
        self.chk_title.grid(row = 0, column = 0, sticky = "news")
        
        self.chk_genre = tk.Checkbutton(self, text="Genre       ",
                                        font=("Verdana","10"),variable = self.genre_bool, selectcolor = "Black")
        self.chk_genre.grid(row = 1, column = 0, sticky = "news")
        
        self.chk_dev = tk.Checkbutton(self, text="Developer",
                                      font=("Verdana","10"),variable = self.dev_bool, selectcolor = "Black")
        self.chk_dev.grid(row = 2, column = 0, sticky = "news")
        
        self.chk_pub = tk.Checkbutton(self, text="Publisher  ",
                                      font=("Verdana","10"),variable = self.pub_bool, selectcolor = "Black")
        self.chk_pub.grid(row = 3, column = 0, sticky = "news")
        
        self.chk_plat = tk.Checkbutton(self, text="Platform          ",
                                       font=("Verdana","10"),variable = self.plat_bool, selectcolor = "Black")
        self.chk_plat.grid(row = 0, column = 1, sticky = "news")
        
        self.chk_release = tk.Checkbutton(self, text="Release           ",
                                          font=("Verdana","10"),variable = self.rel_bool, selectcolor = "Black")
        self.chk_release.grid(row = 1, column = 1, sticky = "news")
        
        self.chk_purchase = tk.Checkbutton(self, text="Purchase date ",
                                           font=("Verdana","10"),variable = self.pur_bool, selectcolor = "Black")
        self.chk_purchase.grid(row = 2, column = 1, sticky = "news")
        
        self.chk_price = tk.Checkbutton(self, text="Purchase price",
                                        font=("Verdana","10"),variable = self.price_bool, selectcolor = "Black")
        self.chk_price.grid(row = 3, column = 1, sticky = "news")
        
        self.chk_sp = tk.Checkbutton(self, text="Singleplayer?",
                                     font=("Verdana","10"),variable = self.sp_bool, selectcolor = "Black")
        self.chk_sp.grid(row = 0, column = 2, sticky = "news")
        
        self.chk_mp = tk.Checkbutton(self, text="Multiplayer?  ",
                                     font=("Verdana","10"),variable = self.mp_bool, selectcolor = "Black")
        self.chk_mp.grid(row = 1, column = 2, sticky = "news")
        
        self.chk_complete = tk.Checkbutton(self, text="Completed?   ",
                                           font=("Verdana","10"),variable = self.comp_bool, selectcolor = "Black")
        self.chk_complete.grid(row = 2, column = 2, sticky = "news")
        
        self.chk_rating = tk.Checkbutton(self, text="Rating            ",
                                         font=("Verdana","10"),variable = self.rate_bool, selectcolor = "Black")
        self.chk_rating.grid(row = 3, column = 2, sticky = "news")
        
        self.title_bool.set(True)
        self.genre_bool.set(True)
        self.dev_bool.set(True)
        self.pub_bool.set(True)
        self.plat_bool.set(True)
        self.rel_bool.set(True)
        self.pur_bool.set(True)
        self.price_bool.set(True)
        self.sp_bool.set(True)
        self.mp_bool.set(True)
        self.comp_bool.set(True)
        self.rate_bool.set(True)        

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
        
        self.lbl_release = tk.Label(self, text="Release year:", font=("Verdana","10"))
        self.lbl_release.grid(row = 4, column = 0)
        
        self.lbl_plat = tk.Label(self, text="Platform:", font=("Verdana","10"))
        self.lbl_plat.grid(row = 0, column = 2)        
        
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
        
        self.ent_release = tk.Entry(self, font=("Verdana","10"))
        self.ent_release.grid(row = 4, column = 1)
        
        self.ent_plat = tk.Entry(self, font=("Verdana","10"))
        self.ent_plat.grid(row = 0, column = 3)        
        
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
    # dictionary indices
    # [0] = title
    # [1] = genre
    # [2] = dev
    # [3] = pub
    # [4] = release
    # [5] = platform
    # [6] = purchase date
    # [7] = purchase price
    # [8] = has SP
    # [9] = has MP
    # [10] = completed
    # [11] = rating
    # [12] = notes    
    
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
    
    Screen.current = 0
    Screen.switch_frame()
    
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)
    root.mainloop()