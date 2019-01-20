"""
Author	: YIXIANG YANG
Date  	: 15 Jan 2019
Purpose	: Collect cloud images from the Google, Bing and Flickr.

"""

import os
import sys
from datetime import date
from icrawler.builtin import GoogleImageCrawler, BingImageCrawler, FlickrImageCrawler

# the fold that you want to store these images
image_path = sys.argv[1]

# API key for crawing image from Flickr
# Key:
# bff26669f752de80bcc10f69c3d6fb92

# Secret:
# 69e361b8ccd8e185

Flickr_API_Key = 'bff26669f752de80bcc10f69c3d6fb92'

CloudTypesList = open('CloudTypesList.txt', 'r')

for cloudTypesName in CloudTypesList:
    cloud_type = cloudTypesName.strip('\n')
    imageDir = image_path + '/' + cloud_type

    # flicker crawing
    flickr_crawler = FlickrImageCrawler(Flickr_API_Key, parser_threads=2, downloader_threads=4,
                                        storage={'root_dir': imageDir})

    flickr_crawler.crawl(
        text=cloud_type,
        max_num=1000,
        tags=cloud_type,
        min_upload_date=date(2009,1,1))

    # google crawing
    google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                        storage={'root_dir': imageDir})
    # google_crawler.crawl(keyword=cloud_type, max_num=1000)

    google_crawler.crawl(
        keyword=cloud_type,
        filters={'date': ((2010, 1, 1), (2019, 1, 1))},
        max_num=1000,
        file_idx_offset=0)
    google_crawler.crawl(
        keyword=cloud_type,
        filters={'date': ((2003, 1, 1), (2009, 12, 31))},
        max_num=1000,
        file_idx_offset='auto')

    # bing crawing
    bing_crawler = BingImageCrawler(parser_threads=2, downloader_threads=4,
                                    storage={'root_dir': imageDir})
    bing_crawler.crawl(
        keyword=cloud_type,
        filters={'date': ((2012, 1, 1), (2019, 1, 1))},
        max_num=1000,
        file_idx_offset='auto')
    bing_crawler.crawl(
        keyword=cloud_type,
        filters={'date': ((2003, 1, 1), (2011, 12, 31))},
        max_num=1000,
        file_idx_offset='auto')

print("Image Collection is done")