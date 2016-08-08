# Imports
import view
from PIL import Image
from urllib.request import urlretrieve
from webbrowser import open
import os


# Class definition
class CmdView(view.View):

    SAVE_PATH = 'data/tmp'

    def __init__(self):
        pass


    def display(self, message):
        print (message)


    def error(self, message):
        print (message)


    def display_items_formatted(self, dict, max_num_of_assets):
        num_of_assets = len(dict['assets'])

        if num_of_assets > 0:
            print ('Displaying the first {} assets (max {}):\n'\
                .format(num_of_assets, max_num_of_assets))
            for i in range(num_of_assets):
                num = ('({})'.format(i + 1))
                print ('{:^6s}{}'.format(num, dict['assets'][i]))
                print ('      Price: ', end='')
                if dict['prices'][i] == 0:
                    print ('FREE')
                else:
                    print ('${:.2f}'.format(dict['prices'][i]))
                print ('      Link:  {}'.format(dict['urls'][i]))
                print () # Blank line
        else:
            self.error('There were no assets found')


    def display_image(self, url):
        """Downloads an image to a temp location and opens it"""
        file_path = '{}/image.png'.format(self.SAVE_PATH)
        
        if not os.path.exists(self.SAVE_PATH):
            os.mkdir(self.SAVE_PATH)

        urlretrieve(url, file_path)
        open('file://' + os.path.realpath(file_path))


# END OF CLASS
