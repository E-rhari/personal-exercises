# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 17:23:01 2023

@author: Evandro Rhari
"""

def make_profile (name, **info):
    """Creates someone's profile - a dictionary of personal info provided by
    the user"""
    profile = {'name': name}
    
    for key, value in info.items():
        profile[key] = value
    
    return profile


for key, info in make_profile('shizuku', height=157, blood = 'a', year='first', 
                              occupation='student').items():
    print(f"{str(key).title()}: {str(info).title()}")