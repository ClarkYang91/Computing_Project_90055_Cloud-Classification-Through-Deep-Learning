"""
Author	: YIXIANG YANG
Date  	: 21 Jan 2019
Purpose	: Resize images and keep each on under 300kb

"""
import cv2
import os
import argparse
import math

parser = argparse.ArgumentParser(description="Input image directory path.")
parser.add_argument("image_path", help="Input image directory path")
args = parser.parse_args()


def resize (file_path, type):
    print(type + ":-- " + file_path)
    origin_size = os.path.getsize(file_path)
    if origin_size >=210000:
        print(origin_size)
        new_size = math.sqrt(210000/origin_size)
        image = cv2.imread(file_path)
        resized = cv2.resize(image, None, fx=new_size, fy=new_size, interpolation=cv2.INTER_AREA)
        cv2.imwrite(file_path, resized)


for dir_name in os.listdir(args.image_path):
    # print("args.image_path --- " + args.image_path)
    for filename in os.listdir(args.image_path + "\\" + dir_name):
        # print("filename --- " + filename)
        # If the images are not .JPG images, change the line below to match the image type.
        if filename.endswith(".jpg") or filename.endswith(".JPG"):
            resize(args.image_path + "\\" + dir_name + "\\" + filename, ".jpg" )
        elif filename.endswith(".png") or filename.endswith(".PNG"):
            resize(args.image_path + "\\" + dir_name + "\\" + filename, ".png")
        elif filename.endswith(".jpeg") or filename.endswith(".JPEG"):
            resize(args.image_path + "\\" + dir_name + "\\" + filename, ".jpeg")

