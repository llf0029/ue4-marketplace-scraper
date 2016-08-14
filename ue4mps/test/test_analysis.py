# Imports
import sys
import unittest
from io import StringIO

sys.path.append('../')

import analysis_util


class UMCmdTest(unittest.TestCase):

    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output

        self.au = analysis_util.AnalysisUtil()
        

    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_chart_1(self):
        data = [5, 10.00, 19.95]
        labels = ['Test Item 1', 'Test Item 2', 'Test Item 3']
        y_label = 'Cost $$$'
        d_format = '$%.2f'

        self.au.generate_chart(data, labels, y_label, d_format)
        expected = ''
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)


    #@unittest.skip("Skipping test to speed up execution while writing tests")
    def test_chart_2(self):
        data = [0, 0.00, -0.1234]
        labels = ['Test Item 1', 'Test Item 2', 'Test Item 3']
        y_label = 'Cost $$$'
        d_format = '$%.2f'

        self.au.generate_chart(data, labels, y_label, d_format)
        expected = ''
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)




if __name__ == '__main__':
    unittest.main()