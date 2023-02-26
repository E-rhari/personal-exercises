# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 23:00:29 2023

@author: Evandro Rhari
"""

def make_album(name, artist, songs=''):
    """Returns a dictionary of strings describing an album by its author and 
    title, and possibly amout of tracks"""
    album = {}
    album['title'] = name
    album['author'] = artist
    if songs:
        album['number'] = songs
    return album
    

title = input("Please, insert the name of the album: ")
author = input("Please, insert the author of the album: ")

songs = input("Would you like to insert the amout of tracks? [y/n]\nR:")
if songs in "yes":
    songs = input("Please, insert the amout of tracks of the album: ")
else:
    songs = ''

album = make_album(title, author, songs)

for key, value in album.items():
    print(f"{key.title()}: {str(value).title()}")