# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 03:19:19 2017

@author: user
"""
#inspired by Les Mis
import pandas as pd

import numpy as np
from bokeh.layouts import column
from bokeh.plotting import figure, curdoc
from bokeh.models import HoverTool, ColumnDataSource

df = pd.read_csv('C:\\...\\poslanici_parovi_stats.csv')
ime = df.poslanik1.drop_duplicates().values
filt=df.pivot_table(index='poslanik1', columns='poslanik2', values='indeks_zaj')
povez = filt.values.flatten()/98

nodes = ime
names = [i for i in sorted(ime)]
counts = filt.values.flatten()

xname = []
yname = []

alpha = povez

for i in names:
    for j in names:
        xname.append(i)
        yname.append(j)
        


source = ColumnDataSource(data=dict(xname=xname, yname=yname, alphas=alpha, count=counts))

p = figure(title="Povezanost poslanika na Tviteru",x_axis_location="above",\
                      tools="hover,save", x_range=list(reversed(names)), y_range=names)
p.plot_width = 800
p.plot_height = 800
p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "5pt"
p.axis.major_label_standoff = 0
p.xaxis.major_label_orientation = np.pi/3

p.rect('xname', 'yname', 0.9, 0.9, source=source,
       color='#fdbf6f', alpha='alphas', line_color=None,
       hover_line_color='black', hover_color='#fdbf6f')

p.select_one(HoverTool).tooltips = [
    ('poslanici', '@xname, @yname'),
    ('indeks povezanosti', '@count'),
]

curdoc().add_root(column(p))
