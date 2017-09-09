# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 02:46:58 2017

@author: user
"""
import pandas as pd

from bokeh.layouts import column
from bokeh.models import HoverTool, CustomJS,  ColumnDataSource
from bokeh.layouts import widgetbox
from bokeh.models.widgets import RadioButtonGroup
from bokeh.plotting import figure, curdoc
from math import pi

df = pd.read_csv('C:\...\\prati_stats.csv')
source = ColumnDataSource(df)

xosa= list(df.poslanik1)

hover = HoverTool(tooltips=[
    ('poslanik', '@poslanik1')
    ])
p1 = figure(plot_width=800, plot_height=300, x_range= xosa)

a = p1.vbar(source=source, width=0.5, bottom=0,x='poslanik1',
       top='pracen', color="firebrick")

b = p1.vbar(source=source, width=0.5, bottom=0,x='poslanik1',
       top='prati', color="navy")
 
c = p1.vbar(source = source, width=0.5, bottom=0,x='poslanik1', 
       top='np', color="#B3DE69")

p1.xaxis.major_label_orientation = pi/4

radio_button_group = RadioButtonGroup(
        labels=['Broj pratilaca', 'Prati', 'NP'], active=0)

radio_button_group.callback = CustomJS(args=dict(bar0=a, bar1=b, bar2=c), code="""   
    bar0.visible = false;
    bar1.visible = false;
    bar2.visible = false;

    if (cb_obj.active == 0) {
        bar0.visible = true;
    } else if (cb_obj.active == 1) {
        bar1.visible = true;
    } else if (cb_obj.active == 2) {
        bar2.visible = true;
    }
""")

layout= column(widgetbox(radio_button_group), p1)
curdoc().add_root(layout)