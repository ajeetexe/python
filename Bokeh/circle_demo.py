from bokeh.plotting import figure
from bokeh.io import output_file, show

x = [3, 7, 5, 10]
y = [3, 6, 9, 11]
output_file('circle.html')
f = figure()
f.circle(x, y)
show(f)
