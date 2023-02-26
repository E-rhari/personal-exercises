# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:03:30 2023

@author: Evandro Rhari
"""

def make_shirt(sh_print = 'I luv Shizuku Osaka', sh_size = 'xxl'):
    """Prints a predetermineted message about a custom shirt placing the 
    argument provided info within it"""
    print(f"So you are havin' a {sh_size.upper()} sized shirt with "+
          f'"{sh_print}" on it? Sounds wonderful!')
    
    
shirt_print = input("What's the message you would like to print in your shirt?"+
                    "\n")
shirt_size = input("'kay! And what's your size?\n")

make_shirt()