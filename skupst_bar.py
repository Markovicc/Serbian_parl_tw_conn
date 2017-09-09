# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 15:45:59 2017

@author: user
"""

import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models.widgets import Select
from math import pi

df = pd.read_csv('C:\\...\\poslanici_parovi_stats.csv')

def get_data(N):
    return dict(df[df.poslanik1 == N][['poslanik2', 'indeks_zaj']])

source = ColumnDataSource(data= get_data('Aleksandra Jerkov'))

xosa= list(df.poslanik2.unique())

hover = HoverTool(tooltips=[
    ('poslanik', '@poslanik2'),
    ('indeks_zaj', '@indeks_zaj')
])
p1 = figure(plot_width=1000, plot_height=250, tools= [hover], x_range= xosa) 
p1.vbar(source=source, x='poslanik2',width= 0.4, bottom=0, top='indeks_zaj', color='firebrick')
p1.xaxis.major_label_orientation = pi/4

poslanici = list(df.poslanik1.unique())
select = Select(title='Poslanik', value='Aleksandra Jerkov', options=poslanici)

def update_data(attrname, old, new):
    N = select.value
    source.data = get_data(N)
    

select.on_change('value', update_data)

layout = column(row(p1), row(select))

curdoc().add_root(layout)