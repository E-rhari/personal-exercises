# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:13:47 2023

@author: Evandro Rhari
"""

def display_bestGirl(*bestGirls):
    """Prints a undetermineted amount of reafirming messages about user's 
    opinion on who is best girl"""
    for bestGirl in bestGirls:
        print(f"{bestGirl.title()} is indeed best girl!")
    print("")
      
        
display_bestGirl('shizuku osaka')
display_bestGirl('shizuku osaka', 'kasumi nakasu', 'emma verde')
display_bestGirl('arima kana', 'kana arima', 'anak amira', 'amira anak')