# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:09:26 2023

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
idol_messages = fan_message(idols[:])

show_idols(idols)
show_idols(idol_messages)