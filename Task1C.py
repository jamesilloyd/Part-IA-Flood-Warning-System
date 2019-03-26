#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:24:57 2018

@author: Marco
"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.geo import stations_by_distance

stations = build_station_list()
x = stations_within_radius(stations, (52.2053, 0.1218), 10)
y= []
for i in x:
    y.append(i.name)
y.sort()
print(y)

