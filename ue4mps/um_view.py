# Imports
import view
from PIL import Image
from urllib.request import urlretrieve
from webbrowser import open


# Class definition
class UMView(view.View):


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
                print ('      Link:  {}\n'.format(dict['urls'][i]))
        else:
            self.error('There were no assets found')


    def display_image(self, file_path):
        """Displays a file saved on the local machine"""
        open('file://' + file_path)


# END OF CLASS
