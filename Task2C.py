#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 21:41:35 2018

@author: James
"""

from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

stations = build_station_list()

x = stations_highest_rel_level(stations, len(stations)+1)

for i in x:
    print("Station: {} \nRelative water level: {}".format(i[0],i[1]))
    print()