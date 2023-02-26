# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 11:22:56 2023

@author: Evandro Rhari
"""

best_girl = 'Shizuku'
print("Is Shizuku Best girl? I think so")
print(best_girl.lower() == 'shizuku')

print("Is Lanzhu Best girl? I don't think so")
print(best_girl.lower() == 'lanzhu')


best_girl_BBF= 'Kasumin'
print("\nIs Kasumin Best girl's best friend? I think so")
print(best_girl.lower() == 'shizuku' and best_girl_BBF.lower() == 'kasumin')

print("Is Araragi Best girl's best friend? I don't think so")
print(best_girl.lower() == 'sengyogahara' and best_girl_BBF.lower == 'araragi')


stupidity = True
print('\nIs this program stupid? I think so')
print(stupidity)
