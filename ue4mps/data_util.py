# Imports
import os
import shelve

import string
import random

from PIL import Image
from urllib.request import urlopen
from urllib.request import urlretrieve


# Class definition
class DataUtil(object):

    SAVE_PATH = 'data'
    TEMP_PATH = 'data/tmp'


    def __init__(self):
        self.full_dir = self.get_full_dir(self.SAVE_PATH)
        self.temp_dir = self.get_full_dir(self.TEMP_PATH)


    def get_full_dir(self, path):
        """Generates a full directory path from a local path"""
        full_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                path)
        if not os.path.exists(full_dir):
            os.makedirs(full_dir)
        return full_dir


    def save_shelf(self, shelf_name, data):
        """Creates / overwrites the data shelf"""
        shelf_path = os.path.join(self.full_dir, shelf_name)
        with shelve.open(shelf_path, 'c') as shelf:
            shelf['data'] = data


    def load_shelf(self, shelf_name):
        """Loads the data shelf and returns its contents"""
        shelf_path = os.path.join(self.full_dir, shelf_name)

        # Create shelf if not exists
        if not os.path.exists(shelf_path + '.dat'):
            self.reset_shelf(shelf_name)
        
        # Read the shelf and return its contents
        with shelve.open(shelf_path, 'r') as shelf:
            data = shelf['data']
        return data


    def reset_shelf(self, shelf_name):
        """Restores a shelf to its default state"""
        shelf_path = os.path.join(self.full_dir, shelf_name)
        with shelve.open(shelf_path, 'n') as shelf:
            shelf['data'] = {
                'assets' : [],
                'prices' : [],
                'images' : [],
                'urls'   : []
            }



    def download_image(self, url):
        """Downloads an image to a temp location and returns the path"""
        file_path = os.path.join(self.temp_dir, 'image.png')
        urlretrieve(url, file_path)
        return file_path


    def download_pil_image(self, url):
        """Downloads and returns a PIL image"""
        return Image.open(urlopen(url))


    def serialize_image(self, image):
        """Turns a PIL image into a serializable object"""
        result = {
            'pixels': image.tobytes(),
            'size'  : image.size,
            'mode'  : image.mode
        }
        return result


    def deserialize_image(self, data, give_file_name):
        """Restores a PIL image from a serialized obj and returns the path"""
        # Generate a random 8-character name
        # name = "img_" + self.generate_random_name() + ".png"
        name = give_file_name + ".png"
        file_path = os.path.join(self.temp_dir, name)
        img = Image.frombytes(data['mode'], data['size'], data['pixels'])
        img.save(file_path)
        return file_path


    def generate_random_string(self, length):
        result = ''
        result += ''.join(
            random.choice(
                string.ascii_upercase + string.digits
            ) for _ in range(8)
        )
        return result
        

    def clear_tmp_folder(self):
        """Deletes all the files within the ./data/tmp/ directory"""
        for file in os.listdir(self.temp_dir):
            if file.endswith('.png') or file.endswith('.jpg'):
                path = os.path.join(self.temp_dir, file)
                print ('Cleaned up {}'.format(path))
                os.remove(path)