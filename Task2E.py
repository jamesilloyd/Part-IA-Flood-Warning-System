#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 23:51:17 2018

@author: Marco
"""

from floodsystem.datafetcher import fetch_measure_levels
import datetime
import matplotlib.pyplot as plt
from plot_actual import plot_water_levels 
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list()

x = stations_highest_rel_level(stations, 5)
l=[]
for i in x:
    l.append(i[0])
m=[]
for i in l:
    station_name = "{}".format(i)

        # Find station
    station_to_plot = None
    for station in stations:
        if station.name == station_name:
            m.append(station)

for i in m:
    dt = 10
    dates, levels = fetch_measure_levels(i.measure_id,
                                     dt=datetime.timedelta(days=dt))
    plot_water_levels(i, dates, levels)


