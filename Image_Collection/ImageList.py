from icrawler.builtin import UrlListCrawler

# download 900 images from ImageList.txt
urllist_crawler1 = UrlListCrawler(downloader_threads=4,
                                 storage={'root_dir': 'd:\Cloud\dataset\list1'})
urllist_crawler1.crawl('ImageList.txt')

# download other images form ImageList2.txt
urllist_crawler2 = UrlListCrawler(downloader_threads=4,
                                 storage={'root_dir': 'd:\Cloud\dataset\list2'})
urllist_crawler2.crawl('ImageList2.txt')