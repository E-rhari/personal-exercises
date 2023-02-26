# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 17:23:37 2023

@author: Evandro Rhari
"""

def make_album(name, artist, songs=''):
    """Returns a dictionary of strings describing an album by its author and 
    title"""
    album = {}
    album['title'] = name
    album['author'] = artist
    if songs:
        album['number'] = songs
    return album
    
    
for n in range(3):
    if n == 0:
        album = make_album("zero ranger ost", "eero lahtinen")
    if n == 1:
        album = make_album("brasilian skies", "masayoshi takanaka", 7)
    if n == 2:
        album = make_album("scramble full panic session", "gyari")
    for key, value in album.items():
        print(f"{key.title()}: {str(value).title()}")
    print("")