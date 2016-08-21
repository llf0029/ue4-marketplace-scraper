# Imports
import re as regex
from urllib.request import urlopen

# python -m pip install beautifulsoup4
from bs4 import BeautifulSoup

# Class definition
class WebPage(object):

    def __init__(self, url, base_url):
        # Create a BeautifulSoup object from the downloaded web page
        self.bs = BeautifulSoup(urlopen(url), 'html.parser')
        self.base_url = base_url


    def strip_tags(self, html):
        """Removes all HTML tags from a string and returns the result"""
        return regex.sub('<[^<]+?>', '', html)


    def find_text(self, tag, class_name):
        """Generates a list of non-tag text matching the tag & class"""
        results = []
        for item in self.bs.find_all(tag, {'class' : class_name}):
            item_text = self.strip_tags(str(item))
            results.append(" ".join(item_text.split()))
        return results


    def find_price(self, tag, class_name):
        """Generates a list of currency values matching the tag & class"""
        results = []
        for item in self.find_text(tag, class_name):
            # Filter price as float
            if item == "Free":
                f = 0.00
            elif item.count('$') == 2:
                # If price is discounted (looks like '$10.00 $5.00')
                # Get last occurence of '$' onwards
                f = float(item[(item.rindex('$') + 1):])
            else:
                # Otherwise, skip '$' and get the rest
                f = float(item[1:])
                
            results.append(f)
        return results


    def find_links(self, tag, class_name):
        """Generates a list of text hyperlinks matching the tag & class"""
        results = []
        for item in self.bs.find_all(tag, {"class" : class_name}):
            # Try to get the href property of item
            href = item.get('href')

            # If href property wasn't found, check sub-items
            if href == None:
                href = str(item.find('a')['href'])

            results.append(self.base_url + href)
        return results


    def find_imgs(self, tag, class_name):
        """Generates a list of image URLs matching the tag & class"""
        results = []
        for item in self.bs.find_all(tag, {"class" : class_name}):
            img = str(item.find('img'))
            img = regex.findall(r'src=".*?"', img)[0].split('"')[1]
            results.append(img)
        return results



if __name__ == '__main__':
    # Download the HTML
    url = "https://www.unrealengine.com/marketplace/content-cat/assets/materials"
    base_url = "https://www.unrealengine.com"
    wp = WebPage(url, base_url)

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


