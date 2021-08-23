import sys
import os
from PIL import Image, ImageFilter


# grab the first and second args from the user
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if (new) folder exist/ if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through the directory, then convert (image.type) to png
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    print('all done!')
