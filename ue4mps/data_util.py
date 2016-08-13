# Imports
import os
import shelve
from PIL import Image


# Class definition
class DataUtil(object):

    SAVE_PATH = 'data'
    TEMP_PATH = 'data/tmp'


    def __init__(self):
        full_dir = self.get_full_dir(self.SAVE_PATH)
        self.shelf_path = os.path.join(full_dir, 'saved_query.dat')


    def get_full_dir(self, path):
        """Generates a full directory path from a local path"""
        full_dir = os.path.join(os.path.dirname(__file__), path)
        if not os.path.exists(full_dir):
            os.makedirs(full_dir)
        return full_dir


    def save_shelf(self, data):
        """Creates / overwrites the data shelf"""
        with shelve.open(self.shelf_path, 'c') as shelf:
            shelf['data'] = data


    def load_shelf(self):
        """Loads the data shelf and returns its contents"""
        with shelve.open(self.shelf_path, 'r') as shelf:
            data = shelf['data']
        return data


    def download_image(self, url):
        """Downloads an image to a temp location and returns the path"""
        full_dir = get_full_dir(self.TEMP_PATH)
        file_path = os.path.join(full_dir, 'image.png')
        urlretrieve(url, file_path)
        return file_path


    def serialize_image(self, image):
        """Turns a PIL image into a serializable object"""
        result = {
            'pixels': image.tobytes(),
            'size'  : image.size,
            'mode'  : image.mode
        }
        return result


    def deserialize_image(self, data):
        """Restores a PIL image from a serializable object"""
        return Image.frombytes(data['mode'], data['size'], data['pixels'])

