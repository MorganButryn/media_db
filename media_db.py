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
     print("4 \t Go back")
     
     uinput = input("-> ")
     
     if uinput == '4':
          return
     if uinput == '1':
          record_creation(len(games) +1)
     else:
          try:
               uindex = int(input("Index of record: "))
               if uindex in games.keys():
                    if uinput == '3':
                         for key in range(1, len(games)+1):
                              if key >= uindex and key != len(games):
                                   games[key] = games[key - 1]
                              if key == len(games):
                                   removal = games.pop(key)
                                   print("Index", uindex, "removed")
                    else:
                         record_creation(uindex)
               else:
                    print("Record does not exist!")
          except:
               print("Error, returning to main menu")
               print()
          
def print_records(index):
     if index == '':
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
     else:
          print("----------------------")
          print("Index:", index)
          print("Title:", games[index][0])
          print("Developer:", games[index][1])
          print("Publisher:", games[index][2])
          print("Release Year:", games[index][3])
          print("Platform:", games[index][4])
          print("Purchase Date:", games[index][5])
          print("Purchase Price:", games[index][6])
          print("Has Singleplayer?:", games[index][7])
          print("Has Multiplayer?:", games[index][8])
          print("Genre:", games[index][9])
          print("Completed?:", games[index][10])
          print("Personal Rating:", games[index][11])
          print("Notes:", games[index][12])
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
          entry.append(float(input("Purchase Price (must be a decimal number only): ")))
          entry.append('')
          entry.append('')
          entry.append(input("Genre: "))
          entry.append('')
          entry.append(input("Personal Rating: "))
          entry.append(input("Notes: "))
          
          boolinput = input("Does the game have singleplayer? (Y/n) ").lower
          if boolinput in yesputs:
               entry[7] = "True"
          else:
               entry[7] = "False"
               
          boolinput = input("Does the game have multiplayer? (Y/n) ").lower
          if boolinput in yesputs:
               entry[8] = "True"
          else:
               entry[8] = "False"
               
          boolinput = input("Have you completed the game? (Y/n) ").lower
          if boolinput in yesputs:
               entry[10] = "True"
          else:
               entry[10] = "False"
               
          boolinput = input("Is the previous information correct? (Y/n) ").lower
          if boolinput in yesputs:
               valid == True
          else:
               entry = []
     games[key] = entry
     print()
     
def search_menu():
     print("Search by:")
     print("----------")
     print("1: \t Title")
     print("2: \t Developer")
     print("3: \t Publisher")
     print("4: \t Release year")
     print("5: \t Platform")
     print("6: \t Purchase date")
     print("7: \t Purchase price")
     print("8: \t Singleplayer status")
     print("9: \t Multiplayer status")
     print("10: \t Genre")
     print("11: \t Personal rating")
     print("12: \t Completion")
     print("13: \t Go back")
     
     uinput = input("-> ")
     
     if uinput == "1":
          uinput = input("Enter Title: ")
          searches(0, uinput)
          
     if uinput == "2":
          uinput = input("Enter Developer: ")
          searches(1, uinput)
          
     if uinput == "3":
          uinput = input("Enter Publisher: ")
          searches(2, uinput) 
          
     if uinput == "4":
          uinput = input("Enter Release year: ")
          searches(3, uinput)
          
     if uinput == "5":
          uinput = input("Enter Platform: ")
          searches(4, uinput) 
          
     if uinput == "6":
          uinput = input("Enter Purchase date: ")
          searches(5, uinput)
          
     if uinput == "7":
          uinput = input("Enter Purchase price (must be a decimal number only): ")
          searches(6, uinput)
          
     if uinput == "8":
          uinput = input("Singleplayer status? (Y/n): ").lower()
          if uinput not in yesputs:
               searches(7, "False")
          else:
               searches(7, "True")
               
     if uinput == "9":
          uinput = input("Multiplayer status? (Y/n): ").lower()
          if uinput not in yesputs:
               searches(8, "False")
          else:
               searches(8, "True")
               
     if uinput == "10":
          uinput = input("Enter Genre: ")
          searches(9, uinput)
                       
     if uinput == "11":
          uinput = input("Enter Personal rating: ")
          searches(10, uinput)
          
     if uinput == "12":
          uinput = input("Completion status? (Y/n): ").lower()
          if uinput not in yesputs:
               searches(11, "False")
          else:
               searches(11, "True")
               
     if uinput == "13":
          return
     
def searches(search_type, uinput):
     matches = 0
     for key in games.keys():
          if uinput in games[key][search_type]:
               print_records(key)
               matches += 1
     print(matches, "matches found!")
     print()
     
picklefile = open("games.pickle", "rb")
games = pickle.load(picklefile)
picklefile.close()

yesputs = ['', 'y', 'yes']

menu()
while True:
     print("Main Menu")
     uinput = input("-> ")
     
     if uinput == '1':
          menu()
          
     if uinput == '2':
          print_records('')
          
     if uinput == '3':
          add_del_edit()
          
     if uinput == '4':
          search_menu()
          
     if uinput == '5':
          picklefile = open("games.pickle", "wb")
          pickle.dump(games, picklefile)
          picklefile.close()        
          exit()
          
print("Major logic error!")