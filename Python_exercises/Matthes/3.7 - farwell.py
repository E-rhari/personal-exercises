# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:13:30 2023

@author: Evandro Rhari
"""

import math

best_idols = ['shizuku', 'rin', 'hanamaru', 'kasumin', 'emma', 'kotori']
for idol in best_idols:
    print("Luv u dear " + idol.capitalize())

print("\nooops error lol\n")
ex_best_idol = 'kotori'
best_idols.remove(ex_best_idol)

for idol in best_idols:
    print("Luv u dearest " + idol.capitalize())
    
print("\nSorry, " +  ex_best_idol + "-chan.\nI still love you.\n")

best_idols.insert(0, 'honoka')
best_idols.insert(math.ceil(len(best_idols)/2), 'keke')
best_idols.append('kana')
for idol in best_idols:
    print("Reeealy love you, my beloved " + idol.title() +"-chan")
    
print("\nI'm now 18 and people think is cringe to like idols")
i = 0
while i < len(best_idols) - 2:
    heart_broken_idol = best_idols.pop()
    print("Farwell, " + heart_broken_idol.capitalize() + ". I loved you untill the end.")

print("\n\nThis will be tough, " + best_idols[0].capitalize() + ", " + best_idols[1].capitalize() + ". Farwell.")
for i in range(0, 2):
     del best_idols[-1]

print("\n\nNow, this is what remains in my heart: ")
print(best_idols)