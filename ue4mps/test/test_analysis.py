# Imports
import unittest
from io import StringIO

import sys
sys.path.append('../')

import analysis_util


class AnalysisUtilTest(unittest.TestCase):

    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output

        self.au = analysis_util.AnalysisUtil()

    def test_chart_1(self):
        data = [5, 10.00, 19.95]
        labels = ['Test Item 1', 'Test Item 2', 'Test Item 3']
        y_label = 'Cost $$$'
        d_format = '$%.2f'

        self.au.generate_chart(data, labels, y_label, d_format)
        expected = ''
        actual = self.output.getvalue().strip()[:len(expected)]
        self.assertEqual(actual, expected)

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
