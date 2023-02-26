# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:31:46 2023

@author: Evandro Rhari
"""

girl = input("Who is best girl?\n")

if girl.lower() in 'shizuku osaka':
    print(f"I see you are a man of culture as well! {girl} surely is best girl!")
else:
    print(f"I would argue, but {girl.title()} is a really good pick as well.")