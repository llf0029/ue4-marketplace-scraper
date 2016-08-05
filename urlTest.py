#--------------------------------
# Import
#--------------------------------

# Import regex in order to strip HTML tags, etc
import re

# Import urlopen in order to download HTML source
from urllib.request import urlopen

# Install BeautifulSoup with the following cmd:
# python -m pip install beautifulsoup4
from bs4 import BeautifulSoup


#--------------------------------
# Scrape Webpage
#--------------------------------

# Download the HTML
url = "https://www.unrealengine.com/marketplace/content-cat/assets/materials"
html = urlopen(url)

# Beautify with BeautifulSoup
bs = BeautifulSoup(html.read(), "html.parser")


def find_text_content_by_class(bs, tag, class_name):
    """Generates a list of non-tag text content from an HTML doc"""
	result = []
	for item in bs.find_all(tag, {"class":class_name}):
		item_text = strip_tags(str(item))
		result.append(" ".join(item_text.split()))
	return result


def find_ahref_by_class(tag, class_name):
	"""Generates a list of non-tag hyperlinks from an HTML doc"""
	result = []
	for item in bs.find_all(tag, {"class":class_name}):
		href = str(item.find('a'))
		href = href.split('"')[1]
		result.append(href)
	return result


def find_imgsrc_by_class(tag, class_name):
	"""Generates a list of non-tag image hyperlinks from an HTML doc"""
	result = []
	for item in bs.find_all(tag, {"class":class_name}):
		img = str(item.find('img'))
		img = re.findall(r'src=".*?"', img)[0].split('"')[1]
		result.append(img)
	return result


def strip_tags(initial_string):
	"""Removes all HTML tags from a string, leaving the stuff surrounded"""
	result = re.sub('<[^<]+?>', '', initial_string)
	return result


# Testing BS methods
assets = find_text_content_by_class('a', 'mock-ellipsis-item mock-ellipsis-item-helper')
prices = find_text_content_by_class('span', 'asset-price')
images = find_imgsrc_by_class('div','image-box')
asset_urls = find_ahref_by_class('div','image-box')

# Testing BS method output
print (len(assets))
print (len(prices))
print (len(images))
print (len(asset_urls))
print (images)





#-----------------------#
# OLDDDDD               #
#-----------------------#
"""
from contextlib import closing

# python -m pip install selenium
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait

with closing(Firefox()) as browser:

	# Get URL
	url = 'http://assetstore.unity3d.com/'
	browser.get(url)

	# Wait for page to load
	WebDriverWait(browser, timeout=10).until(
		lambda x: x.find_element_by_id('homePage')
	)

	page_source = browser.page_source

print (page_source)

"""
