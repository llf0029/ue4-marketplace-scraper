#--------------------------------#
# Testing image downloading      #
#--------------------------------#

from urllib.request import urlretrieve
import os

def download_image(url, save_path):
	urlretrieve(url, save_path)

dl_url = 'https://cdn1.epicgames.com/ue/item/Store_ForestCollection_Thumb-284x284-8c45a54fc00148e5fd677b0335cd0646.png'
save_path = 'images/img.png'
download_image(dl_url, save_path)

