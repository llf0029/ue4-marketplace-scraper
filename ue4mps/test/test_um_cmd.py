# Imports
import sys
import unittest
from io import StringIO

sys.path.append('../')

import um_view
import data_util
import analysis_util
import um_controller
import um_cmd


class UMCmdTest(unittest.TestCase):

    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output

        v = um_view.UMView()
        d = data_util.DataUtil()
        a = analysis_util.AnalysisUtil()
        c = um_controller.UMController(v, d, a)
        self.cmd = um_cmd.UMCmd(c)
        

    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_search_1(self):
        self.cmd.do_search('blueprints')
        expected = 'Displaying the first 10 assets (max 10):'
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)


    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_search_2(self):
        self.cmd.do_search('fire effects')
        expected = 'Displaying the first 6 assets (max 10):'
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)


    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_category_1(self):
        self.cmd.do_category('blueprints')
        expected = 'Displaying the first 10 assets (max 10):'
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)


    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_category_2(self):
        self.cmd.do_category('fire effects')
        expected = 'The category "fire effects" was not found'
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)


    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_results_1(self):
        self.cmd.do_results(1)
        self.cmd.do_search('blueprints')
        expected = 'Displaying the first 1 assets (max 1):'
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)


    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_view_asset_image_1(self):
        self.cmd.do_search('fire effects')
        self.reset_output()
        self.cmd.do_view_asset_image(1)
        expected = ''
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)


    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_view_asset_image_2(self):
        self.cmd.do_search('fire effects')
        self.reset_output()
        self.cmd.do_view_asset_image(99)
        expected = 'Value must be within the previous search results'
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)


    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_view_asset_image_3(self):
        self.cmd.do_view_asset_image(1)
        expected = 'You must run a query first'
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)    


    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_analyse_results_1(self):
        self.cmd.do_search('fire effects')
        self.cmd.do_analyse_results('')
        expected = ''
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)


    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_analyse_results_2(self):
        self.cmd.do_analyse_results('')
        expected = 'You must run a query first'
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)


    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_save_1(self):
        self.cmd.do_search('fire effects')
        self.cmd.do_save('')
        expected = ''
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)


    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_save_2(self):
        self.cmd.do_save('')
        expected = 'No results to save'
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)


    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_load_1(self):
        self.cmd.do_search('fire effects')
        self.cmd.do_save('')
        self.reset_output()
        self.cmd.do_load('')
        expected = 'Displaying the first 6 assets (max 6):'
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)



    def reset_output(self):
        """Clears the output buffer"""
        self.output.seek(0)
        self.output.truncate(0)



if __name__ == '__main__':
    unittest.main()