#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 11:47:16 2018

@author: James
"""

from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list


stations = build_station_list()

x = stations_level_over_threshold(stations,5,None)

for i in x:
    print("Station: {} \nRelative water level: {}".format(i[0].name,i[1]))
    print()
