#--------------------------------#
# Turning data into a graph      #
#--------------------------------#

# Using REPORTLAB to create charts
# python -m pip install reportlab
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.lib import colors

# Test Data
prices = [[5.00], [8.00], [24.99], [60.00], [99.00]] # >>> [ Series [Category] ]
categories = ['Price ($USD)']
labels = [
    'Cool Thing', 
    'Medieval Sword', 
    'Fire Effects', 
    'Fantasy Asset Pack', 
    'Sci Fi Megapack'
]
colors = [colors.red, colors.orange, colors.blue, colors.green, colors.purple]


# Create drawing to hold chart + legend (width, height)
d = Drawing(600, 400)

# ------- Create chart -------
chart = VerticalBarChart()      # Create a bar chart
chart.width = 500               # Set the width of the chart itself
chart.height = 200              # Set the height of the chart itself
chart.x = 50                    # Shift chart right by 50px to centre it
chart.y = 150                   # Shift chart up by 150px so legend can sit underneath
chart.valueAxis.valueMin = 0    # Baseline of axes (set to 0)

# Set bar colors
for i in range(len(colors)):
    chart.bars[i].fillColor = colors[i]

# Add data to chart
chart.data = prices
chart.categoryAxis.categoryNames = categories

# Add labels to chart
chart.barLabelFormat = '$%.2f'  # Text to display on label - 2 decimal float
chart.barLabels.nudge = 8       # Nudge labels upwards by 8px


# ------- Create legend -------
legend = Legend()               # Create the legend
legend.boxAnchor = 'sw'         # Set anchor to bottom-left
legend.x = 50                   # Shift legend right to bring in line with chart
legend.y = 50                   # Shift legend up by 50px
legend.alignment = 'right'      # Put labels to the right of color icons

# Set legend colors
legend.colorNamePairs = [(colors[i], '{}  '.format(labels[i])) for i in range(len(colors))]


# Add chart and legend to drawing
d.add(chart)
d.add(legend)

# Export as test_img.png
d.save(fnRoot='test_img', formats=['png'])


#--------------------------------#
# Opening an image from disk     #
#--------------------------------#

# Though we use webbrowser module, it opens in whatever default app for the file type
from webbrowser import open

open('test_img.png')
