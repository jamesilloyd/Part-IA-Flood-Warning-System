#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 22:16:25 2018

@author: Marco
"""

from floodsystem.stationdata import build_station_list
from floodsystem import station

stations = build_station_list()
 
a = station.inconsistent_typical_range_stations(stations)
m =[]
for i in a:
    m.append(i.name)
m.sort()

print(m)
    
