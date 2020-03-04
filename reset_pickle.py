#!/usr/bin/python3
# Morgan Butryn
# 2020-1-28
# reset_pickle.py
"""resets pickle file"""

import pickle

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

games = {1:['Halo 3', 'FPS', 'Bungee', 'Microsoft', '2007', 'XBox 360', '1/15/2008', 30.00, "True", "True", "True", '10', '']}

pfile = open("games.pickle", "wb")
pickle.dump(games, pfile)
pfile.close()

