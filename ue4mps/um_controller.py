# Imports
import controller
import view
import webpage

import html

from urllib.request import urlopen
from urllib.parse import quote
from urllib.error import HTTPError


# Class definition
class UMController(controller.Controller):
    
    # Constants
    BASE_URL   = 'https://www.unrealengine.com'
    SEARCH_URL = '{}/marketplace/assets?lang=&q={}'
    CAT_URL    = '{}/marketplace/content-cat/assets/{}'

    TAGS_ASSETS = ['a', 'mock-ellipsis-item mock-ellipsis-item-helper']
    TAGS_PRICES = ['span', 'asset-price']
    TAGS_IMGS   = ['div','image-box']
    TAGS_URLS   = ['div','image-box']

    # Settings
    num_of_results = 10

    # Temp data
    temp_result = None


    def __init__(self, view, data_util, analysis_util):
        self.view = view
        self.data_util = data_util
        self.analysis_util = analysis_util


    def search(self, args):
        """Gets the assets from a search query"""
        full_url = self.SEARCH_URL.format(self.BASE_URL, quote(args))
        try:
            results = self.generate_results(full_url)
            self.view.display_items_formatted(results, self.num_of_results)
            self.temp_result = results   # Store results in case of save cmd
        except HTTPError:
            self.view.error('The search query failed')


    def category(self, args):
        """Gets the assets on a category page"""
        full_url = self.CAT_URL.format(self.BASE_URL, quote(args))
        try:
            results = self.generate_results(full_url)
            self.view.display_items_formatted(results, self.num_of_results)
            self.temp_result = results   # Store results in case of save cmd
        except HTTPError:
            self.view.error('The category "{}" was not found'.format(args))


    def generate_results(self, url):
        """Downloads a page and strips the results into components"""
        page = webpage.WebPage(url, self.num_of_results, self.BASE_URL)
        results = {
            'assets':page.find_text (self.TAGS_ASSETS[0], self.TAGS_ASSETS[1]),
            'prices':page.find_price(self.TAGS_PRICES[0], self.TAGS_PRICES[1]),
            'images':page.find_imgs (self.TAGS_IMGS[0], self.TAGS_IMGS[1]),
            'urls'  :page.find_links(self.TAGS_URLS[0], self.TAGS_URLS[1])
        }
        return results


    def display_asset_image(self, asset_index):
        """Displays the image of the specified asset"""
        try:
            if self.temp_result is not None:
                i = int(asset_index) - 1
                if i >= 0:
                    url = self.temp_result['images'][int(asset_index) - 1]
                    img = self.data_util.download_image(html.unescape(url))
                    self.view.display_image(img)
                else:
                    raise ValueError
            else:
                self.view.error('You must run a query first')
        except ValueError:
            self.view.error('The value must be a whole number: ' \
                + 'VIEW_ASSET_IMAGE 4')
        except IndexError:
            self.view.error('Value must be within the previous search results')


    def analyse_results(self):
        """Displays the last query's results in a chart"""
        if self.temp_result is not None:
            img = self.analysis_util.generate_chart(
                self.temp_result['prices'], 
                self.temp_result['assets'], 
                'Price (USD)', 
                '$%.2f'
            )
            self.view.display_image(img)
        else:
            self.view.error('You must run a query first')


    def save_last_query(self):
        """Saves the last query for later use"""
        if self.temp_result is not None:
            self.data_util.save_shelf(self.temp_result)
        else:
            self.view.error('No results to save')


    def load_stored_query(self):
        """Loads the stored query if it exists"""
        try:
            self.temp_result = self.data_util.load_shelf()
            self.view.display_items_formatted(
                self.temp_result, 
                len(self.temp_result['assets'])
            )
        except:
            self.view.error('No saved data to load')


    def set_num_of_results(self, new_value):
        try:
            self.num_of_results = int(new_value)
        except ValueError:
            self.view.error('The value must be a whole number:  RESULTS 10')


# END OF CLASS


if __name__ == '__main__':
    import um_view
    import data_util
    import analysis_util
    
    v = um_view.UMView()
    d = data_util.DataUtil()
    a = analysis_util.AnalysisUtil()
    c = UMController(v, d, a)
    c.search('fire')
