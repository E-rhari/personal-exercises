# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 21:42:23 2023

@author: Evandro Rhari
"""

artouris = {
            'animal':   'stoat',
            'owner':    'michael',
           }

ophelia =  {
            'animal':   'dog',
            'owner':    'shizuku',
           }

neve =     {
            'animal':   'goat',
            'owner':    'emma'
           }

shitake =  {
            'animal':   'dog',
            'owner':    'chika',    
           }

animals = [artouris, ophelia, neve, shitake]

for animal in animals:
    animal_name = [name for name in globals() if globals()[name] is animal]
    print(animal_name[0].title() + ' is a really cute ' + animal['animal'] + ' '
          'owned by the really cute ' + animal['owner'].title() + '!')