# Function Based Code
# Author: Deepu S Gupta
# Date: 04/03/2022

from PIL import Image, ImageDraw, ImageFont

def add_text_img(text):
    """Description: This function adds text to an image

    Args:
        text (_type_): The text to be added to the image

    Returns:
        None
    """
    img = Image.open('images/image1.jpeg') # open the image 
    image_editable = ImageDraw.Draw(img) # ImageDraw function to convert our image into an editable format
    text_font = ImageFont.truetype('comic-sans-ms/ComicSansMS3.ttf', 40) # set the font of the text
    image_editable.text((465,235), text, (0, 0, 0), font=text_font) # draw the text on the image with the position, text, color and font
    img.save('images/edited_image.jpeg') # save the image

print("Program to Add Text to an Image.")
name =  input("Enter your full name: ") # Take the input from the user for the name
add_text_img(name) # Call the function to add the text to the image