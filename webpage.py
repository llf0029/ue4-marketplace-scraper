# Imports
import re as regex
from urllib.request import urlopen

# python -m pip install beautifulsoup4
from bs4 import BeautifulSoup

# Class definition
class WebPage(object):

    def __init__(self, url, num_of_results, base_url):
        # Create a BeautifulSoup object from the downloaded web page
        self.bs = BeautifulSoup(urlopen(url), 'html.parser')
        self.num_of_results = num_of_results
        self.base_url = base_url


    def strip_tags(self, html):
        """Removes all HTML tags from a string and returns the result"""
        return regex.sub('<[^<]+?>', '', html)


    def find_text(self, tag, class_name):
        """Generates a list of non-tag text matching the tag & class"""
        result = []
        for item in self.bs.find_all(tag, {'class' : class_name}):
            item_text = self.strip_tags(str(item))
            result.append(" ".join(item_text.split()))
        return result[:self.num_of_results]


    def find_price(self, tag, class_name):
        """Generates a list of currency values matching the tag & class"""
        result = []
        for item in self.find_text(tag, class_name):
            if item == "Free":
                result.append(0.00)
            else:
                f = float(item[1:])
                result.append(f)
        return result


    def find_links(self, tag, class_name):
        """Generates a list of text hyperlinks matching the tag & class"""
        result = []
        for item in self.bs.find_all(tag, {"class" : class_name}):
            href = str(item.find('a'))
            href = href.split('"')[1]
            result.append(self.base_url + href)
        return result[:self.num_of_results]


    def find_imgs(self, tag, class_name):
        """Generates a list of image URLs matching the tag & class"""
        result = []
        for item in self.bs.find_all(tag, {"class" : class_name}):
            img = str(item.find('img'))
            img = regex.findall(r'src=".*?"', img)[0].split('"')[1]
            result.append(img)
        return result[:self.num_of_results]



def safe_print(message):
    print(message.encode('ascii', 'replace').decode())


if __name__ == '__main__':
    # Download the HTML
    url = "https://www.unrealengine.com/marketplace/content-cat/assets/materials"
    wp = WebPage(url)

    # Testing BS methods
    assets = wp.find_text('a', 'mock-ellipsis-item mock-ellipsis-item-helper')
    prices = wp.find_text('span', 'asset-price')
    images = wp.find_imgs('div','image-box')
    asset_urls = wp.find_links('div','image-box')

    # Testing BS method output
    print (assets)
    print (prices)
    print (images)
    print (asset_urls)

    print (len(assets))
    print (len(prices))
    print (len(images))
    print (len(asset_urls))


