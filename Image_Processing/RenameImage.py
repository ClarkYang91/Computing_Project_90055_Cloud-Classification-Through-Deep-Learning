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
def renameImageName(path, count):
    # print("previous image " + path + "\\" + dir_name + "\\" + file)
    os.rename(path + "\\" + dir_name + "\\" + file, path + "\\" + dir_name + "_" + str(count) + ".jpg")
    # print("after rename " + path + "\\" + dir_name + "_" + str(count) + ".jpg")
    shutil.move(path + "\\" + dir_name + "_" + str(count) + ".jpg", path + "\\" + dir_name)


for dir_name in os.listdir(args.image_path):
    # print(dir_name)
    count = 0
    for file in os.listdir(args.image_path + '\\' + dir_name):
        count = count + 1
        if ".jpg" or ".JPG" in file:
            renameImageName(args.image_path, count)
        elif ".png" or ".PNG" in file:
            renameImageName(args.image_path, count)
        elif ".jpeg" or ".JPEG" in file:
            renameImageName(args.image_path, count)
        elif ".gif" or ".GIF" in file:
            renameImageName(args.image_path, count)



