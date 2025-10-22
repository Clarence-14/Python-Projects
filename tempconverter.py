# Code that converts temperature from Celsius to Fahrenheit.

import math

toCelsius = str("FtoC")
toFahrenheit = str("CtoF")

conversion = input("Enter conversion type (CtoF or FtoC): ")

if conversion == toFahrenheit:
    temp_celsius = float(input("What is the temperature?:"))
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    print(f"The temperature in Fahrenheit is {temp_fahrenheit}F")

elif conversion == toCelsius:  
    temp_fahrenheit = float(input("What is the temperature?:"))
    temp_celsius = (temp_fahrenheit - 32) * 5/9
    print(f"The temperature in Celsius is {temp_celsius}C")

else:
    print("Invalid Option.")     
    

