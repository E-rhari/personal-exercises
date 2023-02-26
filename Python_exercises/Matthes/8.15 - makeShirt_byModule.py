# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:55:23 2023

@author: Evandro Rhari
"""

import makeShirt as ms

def make_shirt(sh_print, sh_size):
    """Prints a predetermineted message about a custom shirt placing the 
    argument provided info within it"""
    print(f"So you are havin' a {sh_size.upper()} sized shirt with "+
          f'"{sh_print}" on it? Sounds wonderful!')
    
    
shirt_print = input("What's the message you would like to print in your shirt?"+
                    "\n")
shirt_size = input("'kay! And what's your size?\n")

ms.make_shirt(shirt_print, shirt_size)