#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 23:36:23 2018

@author: Marco
"""

from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.pyplot as plt
from analysis import polyfit
import numpy as np
import matplotlib

def plot_water_levels(station, dates, levels):
    
    plt.plot(dates, levels, 'g' , label = "Actual Water Level")
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("{}".format(station.name))
    plt.axhline(y=station.typical_range[1], color= 'r')
    plt.axhline(y=station.typical_range[0])
    plt.legend()
    return plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    x= matplotlib.dates.date2num(dates)
    
    poly = polyfit(dates, levels, p)
    
    t = np.linspace(x[0], x[-1],len(dates))
    plt.plot(dates, levels, '.', label = "Original Data Points")
    plt.plot(t, poly(t - x[0]), label = "Best fit polynomial")
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("{}".format(station.name))
    plt.axhline(y=station.typical_range[1], color = 'r')
    plt.axhline(y=station.typical_range[0])
    plt.legend()
    return plt.show()
