# Imports
import os
import random

# python -m pip install reportlab
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.lib import colors

from reportlab.lib.validators import Auto


# Class definition
class AnalysisUtil(object):

    TEMP_PATH = 'data/tmp'

    W = 1024
    H = 768
    MARGIN = 64


    def generate_chart(self, data, x_labels, y_label, d_format):
        """Generates and saves a chart to disk, returning its local path"""
        # Create drawing to hold chart and legend (width, height)
        d = Drawing(self.W, self.H)

        # Create chart and legend
        cols = self.create_colors(len(data))
        c = self.create_chart(data, y_label, d_format, cols)
        l = self.create_legend(x_labels, cols)

        # Add chart and legend to drawing
        d.add(c)
        d.add(l)

        # Get/Create full file path
        full_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                self.TEMP_PATH)
        if not os.path.exists(full_dir):
            os.makedirs(full_dir)

        # Export image as png and return save path
        save_path = os.path.join(full_dir, 'image.png')
        d.save(fnRoot=save_path, formats=['png'])
        return save_path


    def create_chart(self, data, y_label, d_format, cols):
        """Generates and returns a bar chart object"""
        chart = VerticalBarChart()                  # Create a bar chart
        chart.width = self.W - (self.MARGIN * 2)    # Set chart width
        chart.height = self.H / 2                   # Set chart height
        chart.x = self.MARGIN                       # Shift right to centre
        chart.y = (self.H / 2) - self.MARGIN        # Shift up to near top
        chart.valueAxis.valueMin = 0    # Baseline of axes (set to 0)

        # Set bar colors
        for i in range(len(data)):
            chart.bars[i].fillColor = cols[i]

        # Add data to chart
        formatted_data = []
        for data_item in data:
            formatted_data.append([data_item])
        chart.data = formatted_data

        # Add labels to chart
        chart.categoryAxis.categoryNames = [y_label]
        chart.barLabelFormat = d_format # Format of text to display on labels
        chart.barLabels.nudge = 8       # Nudge labels upwards by 8px

        return chart


    def create_legend(self, x_labels, cols):
        """Generates and returns a legend object"""
        legend = Legend()               # Create the legend
        legend.boxAnchor = 'sw'         # Set anchor to bottom-left
        legend.x = self.MARGIN          # Shift right to be inline with chart
        legend.y = self.MARGIN / 2      # Shift up by 50px
        legend.alignment = 'right'      # Put labels on right of color icons
        legend.columnMaximum = 12
        
        # Set legend colors
        legend.colorNamePairs = [(
            cols[i], 
            '{}  '.format(
                (x_labels[i][:30] + '...') 
                if len(x_labels[i]) > 32 
                else x_labels[i]
            ))
            for i in range(len(x_labels))
        ]

        return legend


    def create_colors(self, num_of_colors):
        """Generates and returns an array of colors"""
        cols = []
        for i in range(num_of_colors):
            r = random.uniform(0, 1)
            g = random.uniform(0, 1)
            b = random.uniform(0, 1)
            cols.append(colors.Color(red=r,green=g,blue=b))
        return cols