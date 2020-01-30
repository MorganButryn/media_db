#!/usr/bin/python3
# Morgan Butryn
# 2020-1-28
# media_db.py
"""Simple database for various forms of media."""

import pickle

def menu():
     print()
     print("| Simple Media Database |")
     print("_________________________")
     print()
     print("Enter a number at the arrow prompt (->):")
     print()
     print("Commands: ")
     print("----------")
     print("1: \t view this dialogue again")
     print("2: \t prints all records")
     print("3: \t add/remove/edit record")
     print("4: \t search for record")
     print("5: \t save and quit")
     
def add_del_edit():
     print("1: \t Add record")
     print("2: \t Edit record")
     print("3: \t Remove record")
     
     uinput = input("-> ")
     
     if uinput == '1':
          record_creation(len(games) +1)
     else:   
          uindex = input("Index of record: ")
          if uindex in games.keys():
               if uinput == '3':
                    removal = games.pop(uindex)
                    print("Index", uindex, "removed")
               else:
                    record_creation(uindex)
          else:
               print("Record does not exist!")
          
def print_records():
     for key in games.keys():
          print("----------------------")
          print("Index:", key)
          print("Title:", games[key][0])
          print("Developer:", games[key][1])
          print("Publisher:", games[key][2])
          print("Release Year:", games[key][3])
          print("Platform:", games[key][4])
          print("Purchase Date:", games[key][5])
          print("Purchase Price:", games[key][6])
          print("Has Singleplayer?:", games[key][7])
          print("Has Multiplayer?:", games[key][8])
          print("Genre:", games[key][9])
          print("Completed?:", games[key][10])
          print("Personal Rating:", games[key][11])
          print("Notes:", games[key][12])
          print("----------------------")

def record_creation(key):
     print("Record Creation")
     print("---------------")
     print()
     print("Current information:", games[key])
     valid = False
     entry = []
     while not valid:
          entry.append(input("Title: "))
          entry.append(input("Developer: "))
          entry.append(input("Publisher: "))
          entry.append(input("Release Year: "))
          entry.append(input("Platform: "))
          entry.append(input("Purchase Date: "))
          entry.append(input("Purchase Price: "))
          entry.append('')
          entry.append('')
          entry.append(input("Genre: "))
          entry.append('')
          entry.append(input("Personal Rating: "))
          entry.append(input("Notes: "))
          boolinput = input("Does the game have singleplayer? (Y/n) ").lower
          yesputs = ['', 'y', 'yes']
          if boolinput in yesputs:
               entry[7] = True
          boolinput = input("Does the game have multiplayer? (Y/n) ").lower
          if boolinput in yesputs:
               entry[8] = True
          boolinput = input("Have you completed the game? (Y/n) ").lower
          if boolinput in yesputs:
               entry[10] = True
          boolinput = input("Is the previous information correct? (Y/n) ").lower
          if boolinput in yesputs:
               valid == True
          else:
               entry = []
     games[key] = entry
     print()
     
def searches():
     print("Searching")
          
picklefile = open("games.pickle", "rb")
games = pickle.load(picklefile)
picklefile.close()

menu()
while True:
     uinput = input("-> ")
     
     if uinput == '1':
          menu()
          
     if uinput == '2':
          print_records()
          
     if uinput == '3':
          add_del_edit()
          
     if uinput == '4':
          searches()
          
     if uinput == '5':
          picklefile = open("games.pickle", "wb")
          pickle.dump(games, picklefile)
          picklefile.close()        
          exit()
          
print("Major logic error!")