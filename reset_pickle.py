#!/usr/bin/python3
# Morgan Butryn
# 2020-1-28
# reset_pickle.py
"""resets pickle file"""

import pickle

# [0] = title
# [1] = dev
# [2] = pub
# [3] = release
# [4] = platform
# [5] = purchase date
# [6] = purchase price
# [7] = has SP
# [8] = has MP
# [9] = genre
# [10] = completed
# [11] = rating
# [12] = notes

games = {1:['Halo 3', 'Bungee', 'Microsoft', '2007', 'XBox 360', '1/15/2008', 30.00, True, True, 'FPS', True, '10', '']}

pfile = open("games.pickle", "wb")
pickle.dump(games, pfile)
pfile.close()

