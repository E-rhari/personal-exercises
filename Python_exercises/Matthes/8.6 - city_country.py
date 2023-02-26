# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 17:19:39 2023

@author: Evandro Rhari
"""

def city_country(city, country):
    """Returns a string of the name of a city followed by its country, 
    separeted by a comma"""
    return city.title() + ", " + country.title()
    

print(city_country("nova friburgo", "brazil"))
print(city_country("pau grande", "brazil"))
print(city_country("pee pee island", "canada"))
