"""
Author	: YIXIANG YANG
Date  	: 23 Jan 2019
Purpose	: Collect single cloud images from the Google, Bing and Flickr.

"""

import sys
from icrawler.builtin import GoogleImageCrawler, BingImageCrawler, FlickrImageCrawler

# the fold that you want to store these images
image_path = sys.argv[1]

# API key for crawing image from Flickr
# Key:
# bff26669f752de80bcc10f69c3d6fb92

# Secret:
# 69e361b8ccd8e185

Flickr_API_Key = 'bff26669f752de80bcc10f69c3d6fb92'

CloudTypesList = open('SingleCloud.txt', 'r')

for cloudTypesName in CloudTypesList:
    cloud_type = cloudTypesName.strip('\n')
    # cloud_type = "single cloud in the sky"
    # imageDir = image_path + '\\' + cloud_type
    print("image path--------------" + image_path)

    # # flicker crawing
    # flickr_crawler = FlickrImageCrawler(Flickr_API_Key, parser_threads=2, downloader_threads=4, storage={'root_dir': image_path})
    # flickr_crawler.crawl(text=cloud_type, max_num=1000, tags=cloud_type)

    # google crawing
    google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4, storage={'root_dir': image_path})
    google_crawler.crawl(keyword=cloud_type, max_num=1000, file_idx_offset='auto')

    # bing crawing
    bing_crawler = BingImageCrawler(parser_threads=2, downloader_threads=4, storage={'root_dir': image_path})
    bing_crawler.crawl(keyword=cloud_type, max_num=1000, file_idx_offset='auto')


print("Image Collection is done")
