# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 15:25:26 2023

@author: Evandro Rhari
"""

book = ''
try:
    cthulhu = open("call_of_cthulhu_gutenberg.txt")
    book = cthulhu.read()
    cthulhu.close()
except FileNotFoundError:
    print("Book not found")

word = "the"
times = book.lower().count(word)
print(f"The word '{word}' appears {times} times in Call of Cthulhu, "+
      "by H. P. Lovecraft")
