# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:10:27 2023

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