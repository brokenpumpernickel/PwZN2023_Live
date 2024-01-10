#poetry run bokeh serve --show .\scripts\Lab009\app.py

import numpy as np
from bokeh.io import output_notebook, curdoc
from bokeh.plotting import figure, show
from bokeh.layouts import row, column, gridplot, layout
from bokeh.models import Slider, Div
from bokeh.util.hex import hexbin
from bokeh.transform import linear_cmap
from bokeh.palettes import all_palettes

n = 10000

xs = np.random.standard_normal(n)
ys = np.random.standard_normal(n)

hb = hexbin(xs, ys, 0.2)

fig = figure(width=400, aspect_ratio=1)
fig.grid.visible = False
fig.background_fill_color = all_palettes['Turbo'][256][0]

cmap = linear_cmap('counts', all_palettes['Turbo'][256], 0, max(hb.counts))
ht = fig.hex_tile(size=0.2, source=hb, fill_color=cmap, line_color=None)

s1 = Slider(start=1000, end=100000, value=10000, step=1000, title='N', width=200)

def update(attr, old, new):
    n = s1.value

    xs = np.random.standard_normal(n)
    ys = np.random.standard_normal(n)

    hb = hexbin(xs, ys, 0.2)

    cmap = linear_cmap('counts', all_palettes['Turbo'][256], 0, max(hb.counts))
    ht.glyph.fill_color = cmap
    ht.glyph.line_color = cmap

    ht.data_source.data = hb

s1.on_change('value_throttled', update)

curdoc().add_root(column(Div(text='<h1>YOLO</h1>'), row(s1, fig)))