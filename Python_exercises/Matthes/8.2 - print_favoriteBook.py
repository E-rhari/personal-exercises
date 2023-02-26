# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 23:21:14 2023

@author: Evandro Rhari
"""

def print_favoriteBook(favoriteBook):
    """Inserts a user inserted string to a predetermined message, then prints
    it"""
    print("One of your favotire books is:" + favoriteBook.title() + "'")
    
    
favoriteBook = input("What is your favorite book?\n")
print_favoriteBook(favoriteBook)