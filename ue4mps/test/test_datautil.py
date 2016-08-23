# Imports
import os
import unittest

import sys
sys.path.append('../')

import data_util


class DataUtilTest(unittest.TestCase):

    TEST = 'test-file'

    def setUp(self):

        self.du = data_util.DataUtil()
        self.remove_test_files(self.du.full_dir)
        self.remove_test_files(self.du.temp_dir)

    @classmethod
    def tearDownClass(cls):
        cls.du = data_util.DataUtil()
        cls.remove_test_files(cls, cls.du.full_dir)
        cls.remove_test_files(cls, cls.du.temp_dir)

    def test_save_shelf_1(self):
        self.du.save_shelf(self.TEST, 'test data')
        success = os.path.exists(
            os.path.join(self.du.full_dir, (self.TEST + '.dat'))
        )
        self.assertTrue(success)

    def test_save_shelf_2(self):
        self.du.save_shelf(self.TEST, ['test data 1', 'test data 2'])
        success = os.path.exists(
            os.path.join(self.du.full_dir, (self.TEST + '.dat'))
        )
        self.assertTrue(success)

    def test_save_shelf_3(self):
        self.du.save_shelf(self.TEST, None)
        success = os.path.exists(
            os.path.join(self.du.full_dir, (self.TEST + '.dat'))
        )
        self.assertTrue(success)

    def test_load_shelf_1(self):
        test_data = 'test data'
        self.du.save_shelf(self.TEST, test_data)
        actual = self.du.load_shelf(self.TEST)
        self.assertEqual(actual, test_data)

    def test_load_shelf_2(self):
        test_data = ['test data 1', 'test data 2']
        self.du.save_shelf(self.TEST, test_data)
        actual = self.du.load_shelf(self.TEST)
        self.assertEqual(actual, test_data)

    def test_load_shelf_3(self):
        test_data = None
        self.du.save_shelf(self.TEST, test_data)
        actual = self.du.load_shelf(self.TEST)
        self.assertEqual(actual, test_data)

    def test_overwrite_shelf(self):
        test_data = 'overwritten!'
        self.du.save_shelf(self.TEST, 'original')
        self.du.save_shelf(self.TEST, test_data)
        actual = self.du.load_shelf(self.TEST)
        self.assertEqual(actual, test_data)

    def test_load_no_shelf(self):
        actual = self.du.load_shelf(self.TEST)
        expected = {
            'assets': [],
            'prices': [],
            'images': [],
            'urls': []
        }
        self.assertEqual(actual, expected)

    def test_reset_shelf(self):
        self.du.save_shelf(self.TEST, 'original')
        self.du.reset_shelf(self.TEST)
        actual = self.du.load_shelf(self.TEST)
        expected = {
            'assets': [],
            'prices': [],
            'images': [],
            'urls': []
        }
        self.assertEqual(actual, expected)

    def test_download_image_1(self):
        url = 'https://c1.staticflickr.com/9/8246/8560552146_6b50021122.jpg'
        actual = self.du.download_image(url)
        expected = os.path.join(self.du.temp_dir, 'image.png')
        self.assertTrue(actual, expected)

    def test_download_image_2(self):
        with self.assertRaises(Exception) as err:
            url = 'https://www.worldof404craft.com/404_ME.jpg'
            self.du.download_image(url)

    def test_download_pil_image_1(self):
        url = 'https://c1.staticflickr.com/9/8246/8560552146_6b50021122.jpg'
        actual = type(self.du.download_pil_image(url))
        expected = 'Image'
        self.assertTrue(actual, expected)

    def test_download_pil_image_2(self):
        with self.assertRaises(Exception) as err:
            url = 'https://www.worldof404craft.com/404_ME.jpg'
            self.du.download_pil_image(url)

    def test_serialize_image(self):
        url = 'https://c1.staticflickr.com/9/8246/8560552146_6b50021122.jpg'
        img = self.du.download_pil_image(url)
        actual = self.du.serialize_image(img)
        expected_size = (300, 300)
        expected_mode = 'RGB'
        expected_pixels_type = type(b'bytes')
        self.assertEqual(actual['size'], expected_size)
        self.assertEqual(actual['mode'], expected_mode)
        self.assertEqual(type(actual['pixels']), expected_pixels_type)

    def test_deserialize_image(self):
        url = 'https://c1.staticflickr.com/9/8246/8560552146_6b50021122.jpg'
        img = self.du.download_pil_image(url)
        serialized_img = self.du.serialize_image(img)
        actual = self.du.deserialize_image(serialized_img, self.TEST)
        success = os.path.exists(
            os.path.join(self.du.temp_dir, (self.TEST + '.png'))
        )
        self.assertTrue(success)

    def remove_test_files(self, directory):
        """Deletes the test files"""
        for file in os.listdir(directory):
            if file.startswith(self.TEST):
                path = os.path.join(directory, file)
                os.remove(path)

if __name__ == '__main__':
    unittest.main()
