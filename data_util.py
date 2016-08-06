# Imports
import shelve
from PIL import Image

# Class definition
class DataUtil(object):

    SHELF_PATH = 'data/saved_query'


    def save_shelf(self, data):
        with shelve.open(self.SHELF_PATH, 'c') as shelf:
            shelf['data'] = data


    def load_shelf(self):
        with shelve.open(self.SHELF_PATH, 'r') as shelf:
            data = shelf['data']
        return data


    def serialize_image(self, image):
        result = {
            'pixels': image.tobytes(),
            'size'  : image.size,
            'mode'  : image.mode
        }
        return result


    def deserialize_image(self, data):
        return Image.frombytes(data['mode'], data['size'], data['pixels'])
