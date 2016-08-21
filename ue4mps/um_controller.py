# Imports
import controller
import view
import webpage

import html

from urllib.parse import quote
from urllib.error import HTTPError


# Class definition
class UMController(controller.Controller):
    
    # Constants
    BASE_URL   = 'https://www.unrealengine.com'
    SEARCH_URL = '{}/marketplace/assets?lang=&q={}'
    SEARCH_EXT = '{}&offset={}&max=25'
    CAT_URL    = '{}/marketplace/content-cat/assets/{}'

    TAGS_ASSETS = ['a', 'mock-ellipsis-item mock-ellipsis-item-helper']
    TAGS_PRICES = ['span', 'asset-price']
    TAGS_IMGS   = ['div','image-box']
    TAGS_URLS   = ['div','image-box']
    TAGS_NEXTPAGE = ['a', 'nextLink']

    STORED_QUERY = 'stored-query'
    WISHLIST = 'wishlist'

    # Settings
    search_results = 10

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
            results = self.generate_results(full_url, self.search_results)
            self.view.display_items_formatted(results, self.search_results)
            self.temp_result = results   # Store results in case of save cmd
        except HTTPError as err:
            self.view.error('The search query failed: ' + err.reason)
        except:
            self.view.error('An error occured while contacting the server. \
                Please check your internet connection and try again.')


    def category(self, args):
        """Gets the assets on a category page"""
        full_url = self.CAT_URL.format(self.BASE_URL, quote(args))
        try:
            results = self.generate_results(full_url, 25)
            self.view.display_items_formatted(results, 25)
            self.temp_result = results   # Store results in case of save cmd
        except HTTPError:
            self.view.error('The category "{}" was not found'.format(args))
        except:
            self.view.error('An error occured while contacting the server. \
                Please check your internet connection and try again.')


    def generate_results(self, url, num_of_results):
        """Downloads a page and strips the results into components"""
        assets = []
        prices = []
        images = []
        urls = []
        
        # Use original url for first time
        next_page_url = url
        
        # Loop until got enough results, or we run out of results
        while True:
            # Get next page object
            page = webpage.WebPage(next_page_url, self.BASE_URL)

            # Generate and append results
            assets += page.find_text (self.TAGS_ASSETS[0], self.TAGS_ASSETS[1])
            prices += page.find_price(self.TAGS_PRICES[0], self.TAGS_PRICES[1])
            images += page.find_imgs (self.TAGS_IMGS[0],   self.TAGS_IMGS[1])
            urls   += page.find_links(self.TAGS_URLS[0],   self.TAGS_URLS[1])

            # Check for results maxed out
            if len(assets) >= num_of_results:
                assets = assets[:num_of_results]
                prices = prices[:num_of_results]
                images = images[:num_of_results]
                urls   = urls[:num_of_results]
                break;

            # Check for more pages
            try:
                next_page_url = page.find_links(
                    self.TAGS_NEXTPAGE[0],
                    self.TAGS_NEXTPAGE[1]
                )
                next_page_url = str(next_page_url[0])
            except:
                next_page_url = None
            finally:
                if next_page_url is None:
                    break

        # Lastly, return results object
        return {
            'assets': assets,
            'prices': prices,
            'images': images,
            'urls': urls
        }


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
            self.data_util.save_shelf(self.STORED_QUERY, self.temp_result)
        else:
            self.view.error('No results to save')


    def load_stored_query(self):
        """Loads the stored query if it exists"""
        try:
            self.temp_result = self.data_util.load_shelf(self.STORED_QUERY)
            self.view.display_items_formatted(
                self.temp_result, 
                len(self.temp_result['assets'])
            )
        except:
            self.view.error('No saved data to load')


    def set_search_results(self, new_value):
        try:
            self.search_results = int(new_value)
        except ValueError:
            self.view.error('The value must be a whole number:  RESULTS 10')


    def wishlist_add(self, asset_index):
        try:
            if self.temp_result is not None:
                i = int(asset_index) - 1
                if i >= 0:
                    url = self.temp_result['images'][i]
                    img = self.data_util.download_pil_image(html.unescape(url))
                    serialized_img = self.data_util.serialize_image(img)

                    wishlist = self.data_util.load_shelf(self.WISHLIST)
                    wishlist['assets'].append(self.temp_result['assets'][i])
                    wishlist['prices'].append(self.temp_result['prices'][i])
                    wishlist['images'].append(serialized_img)
                    wishlist['urls'].append(self.temp_result['urls'][i])
                    self.data_util.save_shelf(self.WISHLIST, wishlist)
                else:
                    raise ValueError
            else:
                self.view.error('You must run a query first')
        except ValueError:
            self.view.error('The value must be a whole number: ' \
                + 'WISHLIST_ADD 4')
        except IndexError:
            self.view.error('Value must be within the previous search results')


    def wishlist_view(self):
        try:
            wishlist = self.data_util.load_shelf(self.WISHLIST)
            self.view.display_items_formatted(wishlist, len(wishlist['assets']))
            for i in range(len(wishlist['images'])):
                img = self.data_util.deserialize_image(
                    wishlist['images'][i],
                    wishlist['assets'][i]
                )
                self.view.display_image(img)
        except:
            self.view.error('No saved data to load')


    def wishlist_clear(self):
        self.data_util.reset_shelf(self.WISHLIST)


    def clear_tmp_folder(self):
        self.data_util.clear_tmp_folder()



# END OF CLASS


if __name__ == '__main__':
    import cmd_view
    import data_util
    import analysis_util
    
    v = um_view.UMView()
    d = data_util.DataUtil()
    a = analysis_util.AnalysisUtil()
    c = UMController(v, d, a)
    c.search('fire')
