from motion_detector import df
from bokeh.plotting import figure, show, output_file
from datetime import datetime as dt
from bokeh.models import HoverTool, ColumnDataSource

# We'll do some formatting in our df for displaying it on hover
df['Entry_string'] = df['Entry'].dt.strftime("%Y-%m-%d  %H:%M:%S")
df['Exit_string'] = df['Exit'].dt.strftime("%Y-%m-%d  %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type = 'datetime', height = 300 ,sizing_mode = "scale_width", title = "Motion Graph")

p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

"""
desired_num_ticks¶

    property type: Int

    A desired target number of major tick positions to generate across the plot range.
"""

hover = HoverTool(tooltips = [("Entry ", "@Entry_string"), ("Exit ", "@Exit_string")])
p.add_tools(hover)

q = p.quad(source = cds,left = "Entry",right = "Exit",bottom=0,top = 1, color = "green")

output_file("motion_graph.html")

show(p)
