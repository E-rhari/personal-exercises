# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:49:18 2023

@author: Evandro Rhari
"""

from string import capwords

idol_groups =  {
               'shizuku':   ['nijigasaki gakuen', 'A°ZU°NA'],
               'rin':       ["µ's", "lily white", "after school navigators"],
               'hanamaru':  ['aquors', 'azelea'],
               'kasumin':   ['nijigasaki gakuen', 'QU4RTS'],
               }

for idols, groups in idol_groups.items():
    print(f"\n{capwords(idols)}'s idol groups: ")
    for group in groups:
        print("* " + group.title())
            