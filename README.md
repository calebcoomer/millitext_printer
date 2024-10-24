# millitext_printer
A python program which takes alphanumeric text as input and outputs a 1x5 or 2x5 millitext png image.

-User's input will be checked to ensure for only alphanumeric characters.

-Each letter and number has a corresponding letter code in the text_libraries.py file.

-Each letter code consists of 5 (or 10 in the case of the 2x5 font) color codes.

-Each color code consists of 3 RGB values.

Iterating through an input will result in pillow/PIL coloring one pixel at a time
until the entire message has been translated. The program will then output a .png image
containing the user input in 1x5 or 2x5 millitext.
