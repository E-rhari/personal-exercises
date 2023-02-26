# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 23:14:08 2023

@author: Evandro Rhari
"""

def show_idols(idols):
    for idol in idols:
        print(idol.title())


def fan_message(group):
    n = 0
    while n < len(group):
        group[n] = f"I love you from the bottom of my heart, {group[n]}!"
        n += 1
    return group


idols = ['shizuku', 'kasumin', 'emma', 'kana', 'keke', 'rin', 'hanamaru']

show_idols(fan_message(idols))