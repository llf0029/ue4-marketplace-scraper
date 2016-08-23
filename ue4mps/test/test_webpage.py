# Imports
import unittest

import sys
sys.path.append('../')

import webpage


class WebpageTest(unittest.TestCase):

    def setUp(self):
        base_url = 'https://www.unrealengine.com'
        query_url = base_url + '/marketplace/assets?lang=&q=test'
        self.wp = webpage.WebPage(query_url, base_url)

    # @unittest.skip("Skipping test to speed up execution while writing tests")
    def test_strip_tags(self):
        html = '<a href="example.com/stuff">No tags <i>here</i>, boss</a>'
        actual = self.wp.strip_tags(html)
        expected = 'No tags here, boss'
        self.assertEqual(actual, expected)

    # @unittest.skip("Skipping test to speed up execution while writing tests")
    def test_find_text_1(self):
        tag = 'div'
        class_name = 'page-title'
        actual = self.wp.find_text(tag, class_name)
        expected = ['Content Search']
        self.assertEqual(actual, expected)

    # @unittest.skip("Skipping test to speed up execution while writing tests")
    def test_find_text_2(self):
        tag = 'a'
        class_name = 'mock-ellipsis-item mock-ellipsis-item-helper'
        actual = self.wp.find_text(tag, class_name)
        expected = ['Crash Test Robot Dummy', '32 HDRIs Lighting Environments']
        self.assertEqual(actual, expected)

    # @unittest.skip("Skipping test to speed up execution while writing tests")
    def test_find_price(self):
        tag = 'div'
        class_name = 'price-container'
        actual = self.wp.find_price(tag, class_name)
        expected = [9.99, 14.99]
        self.assertEqual(actual, expected)

    # @unittest.skip("Skipping test to speed up execution while writing tests")
    def test_find_links_1(self):
        tag = 'ul'
        class_name = 'footer-list'
        actual = self.wp.find_links(tag, class_name)
        expected = ['https://www.unrealengine.com/unreal-engine-4']
        self.assertEqual(actual, expected)

    # @unittest.skip("Skipping test to speed up execution while writing tests")
    def test_find_links_2(self):
        tag = 'div'
        class_name = 'image-box'
        actual = self.wp.find_links(tag, class_name)
        expected = [
            self.base_url + '/marketplace/crash-test-robot-dummy',
            self.base_url + '/marketplace/32-hdris-lighting-environments'
        ]
        self.assertEqual(actual, expected)

    # @unittest.skip("Skipping test to speed up execution while writing tests")
    def test_find_images(self):
        tag = 'div'
        class_name = 'image-box'
        actual = self.wp.find_imgs(tag, class_name)
        expected = [
            'https://cdn1.epicgames.com/ue/item/' +
            'CrashTestRD_Thumb-284x284-1dd187177c17232e2fe7da2b4047fd4d.png',
            'https://cdn1.epicgames.com/ue/item/' +
            'HDRIs_Thumbnail-284x284-3e3950364b72f446cd86a64bde521df4.png'
        ]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
