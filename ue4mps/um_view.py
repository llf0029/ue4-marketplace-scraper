# Imports
import view

import sys
import os
from PIL import Image
from urllib.request import urlretrieve
from webbrowser import open


# Class definition
class UMView(view.View):

    def display(self, message):
        print (message.encode('ascii', 'replace').decode())

    def error(self, message):
        print (message.encode('ascii', 'replace').decode())

    def display_items_formatted(self, dict, max_num_of_assets):
        num_of_assets = len(dict['assets'])

        if num_of_assets > 0:
            self.display('Displaying the first {} assets (max {}):\n'
                         .format(num_of_assets, max_num_of_assets))
            for i in range(num_of_assets):
                # Display asset name and number
                num = ('({})'.format(i + 1))
                self.display('{:^6s}{}'.format(num, dict['assets'][i]))

                # Display asset price
                price = dict['prices'][i]
                if price == 0:
                    self.display('      Price: FREE')
                else:
                    self.display('      Price: ${:.2f}'.format(price))

                # Display asset URL
                self.display('      Link:  {}\n'.format(dict['urls'][i]))
        else:
            self.error('There were no assets found')

    def display_image(self, file_path):
        """Displays a file saved on the local machine"""
        if os.path.exists(file_path):
            open('file://' + file_path)
        else:
            self.error('The image at "{}" was not found'.format(file_path))
