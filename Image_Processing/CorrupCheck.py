"""
Author	: YIXIANG YANG
Date  	: 10 Feb 2019
Purpose	: find corrupted images

"""

from os import listdir
from PIL import Image
import argparse
import os

parser = argparse.ArgumentParser(description="Input image directory path.")
parser.add_argument("image_path", help="Input image directory path")
args = parser.parse_args()
count = 0

for filename in os.listdir(args.image_path):
    # print(filename)
    if filename.endswith('.jpg'):
        try:
            img = Image.open(filename)  # open the image file
            img.verify()  # verify that it is, in fact an image
            print('Good file:', filename)
        except (IOError, SyntaxError) as e:
            count = count + 1
            print('Bad file:', filename)  # print out the names of corrupt files


print(count)

# for filename in listdir('./'):
#     if filename.endswith('.jpg'):
#         try:
#             img = Image.open('./' + filename)  # open the image file
#             img.verify()  # verify that it is, in fact an image
#         except (IOError, SyntaxError) as e:
#             print('Bad file:', filename)  # print out the names of corrupt files