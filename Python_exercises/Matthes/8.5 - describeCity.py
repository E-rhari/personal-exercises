# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:06:17 2023

@author: Evandro Rhari
"""

def describe_city(city, country="brasil"):
    """Prints a predetermineted message about a city and the country it's 
    located, placing the argument provided info within it"""
    print(f"{city.title()} is located at {country.title()}")
    
    
describe_city("nova friburgo")
describe_city("pau grande", "brasil")
describe_city("pee pee island", "canada")
