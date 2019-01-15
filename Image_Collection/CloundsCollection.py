"""
Author	: YIXIANG YANG
Date  	: 15 Jan 2019
Purpose	: Collect cloud images from the Google, Bing and Flickr.

"""

import os
import sys
from datetime import date
from icrawler.builtin import GoogleImageCrawler, BingImageCrawler, FlickrImageCrawler

# the first augement is the path of the cloud type files
image_path = sys.argv[1]

# API key for crawing image from Flickr
# Key:
# bff26669f752de80bcc10f69c3d6fb92

# Secret:
# 69e361b8ccd8e185

Flickr_API_Key = 'bff26669f752de80bcc10f69c3d6fb92'

CloudTypesList = open('CloudTypesList.txt','r')

for cloudTypesName in CloudTypesList:
    cloud_type = cloudTypesName.strip('\n')
    imageDir = image_path + '/' + cloud_type

    # google crawing
    google_crawler = GoogleImageCrawler(storage={'root_dir': imageDir})
    google_crawler.crawl(keyword=cloud_type, max_num=1000)

    # flicker crawing 
    flickr_crawler = FlickrImageCrawler(Flickr_API_Key, storage={'root_dir': imageDir})
    flickr_crawler.crawl( text = cloud_type, max_num = 1000, tags = cloud_type)

    # bing crawing
    bing_crawler = BingImageCrawler(downloader_threads=4, storage={'root_dir': imageDir})
	bing_crawler.crawl(keyword=cloud_type, filters=None, offset=0, max_num=1000)


print("Image Collection is done")