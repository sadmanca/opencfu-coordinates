"""Usage: get-coordinates.py CSV

This program takes detailed CSV files from OpenCFU as an input and prints
detected colonies as a string array (also saving that string in a text file).
"""

"""
@ params
  CSV file

@ returns
  txt file containing string array of image coordinates of detected colonies
"""

import sys
import csv

coordinates = '['

with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row[' IsValid']) == 1:
            coordinates += '(' + row['X'] + ', ' + row['Y'] + '), '
    coordinates = coordinates[:-2] + ']'

print(coordinates)
with open('coordinates.txt', 'w') as coordinates_txt:
    coordinates_txt.write(coordinates)