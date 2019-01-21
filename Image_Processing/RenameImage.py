"""
Author	: YIXIANG YANG
Date  	: 20 Jan 2019
Purpose	: Rename all image name

"""

import os
import argparse
import shutil


parser = argparse.ArgumentParser(description="Input image directory path.")
parser.add_argument("image_path", help="Input image directory path")
args = parser.parse_args()

print("Image directory path is " + args.image_path)

# help function: help to rename image name
def renameImageName(path, filename, count, type):
    # print("previous image " + path + filename)
    os.rename(path + "\\" + filename, path + "_" + str(count) + type)
    # print("after rename " + path + filename + "_" + str(count) + type)
    shutil.move(path + "_" + str(count) + type, path)


for dir_name in os.listdir(args.image_path):
    # print(dir_name)
    count = 0
    for file in os.listdir(args.image_path + "\\" + dir_name):
        count = count + 1
        if file.endswith(".jpg") or file.endswith(".JPG"):
            renameImageName(args.image_path + "\\" + dir_name, file, count, ".jpg")
        elif file.endswith(".png") or file.endswith(".PNG"):
            renameImageName(args.image_path + "\\" + dir_name, file, count, ".png")
        elif file.endswith(".jpeg") or file.endswith(".JPEG"):
            renameImageName(args.image_path + "\\" + dir_name, file, count, ".jpeg")
        elif file.endswith(".gif") or file.endswith(".GIF"):
            renameImageName(args.image_path + "\\" + dir_name, file, count, ".gif")



