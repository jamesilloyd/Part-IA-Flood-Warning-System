#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 18:22:24 2018

@author: Heisenberg
"""
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

stations=build_station_list()
p = (52.2053, 0.1218)

x = stations_by_distance(stations, p)

#Find first 10 stations
print("The closest 10 stations are:")
print()

for i in range(10):
    y = x[i][0]
    print(y.name)
    print(y.town)
    print(x[i][1])
    print()
    
#Find first 10 stations
print("The furthest 10 stations are:")
print()

for i in range(10):
    a = len(x) -10 + i
    y = x[a][0]
    print(y.name)
    print(y.town) 
    print(x[a][1])
    print()



