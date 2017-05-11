# ConeVolumeCalculator.py
# Your job is to write a function in ConeVolumeCalculator.py (call
# it **calculateConeVolume()** that calculates the volume of a cone
# factor based on the Volume Calculator
# Calculator.net (http://www.calculator.net/volume-calculator.html)

# Define Function below
# be sure to return an integer

import math

def calculateConeVolume(radius, height):
    volume=(1/3)*height*math.pi*radius**2
    volume=round(volume,2)
    return volume

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function
