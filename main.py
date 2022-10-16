import math

import json
import requests


from getdata import get_data_func
#from kivydisplay import app_display


#asking user for their preferences: 
welcome_note = "Welcome to Food Tinder, an app where we help you to find your favorite restaurant!"
location = input("Enter a Location! ") # any location 
preference = input("What kind of food do you like? ")  # any preference
distance = input("How far are you will to go? ") # max distance is 40000
price = input("What price were you considering? Pick one: $,$$,$$$: ") # $-1, $$-2, $$$-3, $$$$-4

data, length_data = get_data_func(location, preference, distance, price)

print(length_data)

for i in range(length_data):
    print("This is Restaurant 1: ")
    print(data.loc[i,:])
    right_or_left = input("Swipe Right or Left: (R for Right and L for Left") 
    if(right_or_left == 'R'):
        data = data.drop(i)


print(data)