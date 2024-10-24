## converts user input text to 1x5 millitext
## https://www.msarnoff.org/millitext/subtext1.png used as reference
## Matt Sarnoff, 10.22.08
## Python implementation by Caleb Coomer, 08.16.24

## using PIL's Image module to create PNG and fill pixel colors
from PIL import Image
## importing two dictionaries containing letter information
from text_libraries import pixelColor, letterPixel


## function that will take the user input as text and output a png with millitext
def text_to_image(text):
    # width is 2x+1 input length to give space between words and black border
    img_width = (len(text) * 2) + 1
    # height is 7 to give black border
    img_height = 7
    # output image uses RGB format
    output_image = Image.new('RGB', (img_width, img_height))

## Each letter in text -> five vertical pixels
## Each vertical pixel -> three RGB values
## Enumerate through the text to get each letter and its index
    for x, letter in enumerate(text):
## Enumerate through each letter to get each pixel and its index
        for y, pixel in enumerate(letterPixel[letter]):
            # letter index gives us x
            x_coord = (x * 2) + 1
            # pixel index gives us y
            y_coord = (y + 1)
            # pixel gives us RGB values for color
            color = pixelColor.get(pixel)
            # this outputs the pixel into our final image
            output_image.putpixel((x_coord, y_coord), color)
    # return output
    return output_image

## Main function uses while True loop to catch input error and allow break
def main():
    print('This program will take input and output text in 1x5 subpixel font')
    print('This program was inspired by https://www.msarnoff.org/millitext/\n')
    while True:
        # use .upper() to convert user input so it matches the dictionary keys
        text = input('Enter an alphanumeric message, enter "!done" to exit: ').upper()
        try:
            # user input to break true loop
            if text == '!DONE':
                break
            # user input does not break loop nor throw error
            else:
                output_image = text_to_image(text)
                output_image.show()
                continue
            # user input error cause by providing input not found in dictionary
        except KeyError:
            print('Error: unacceptable entry.')
            continue
        
main()
