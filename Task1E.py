#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 22:55:56 2018

@author: Marco
"""
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number



stations = build_station_list()


print(rivers_by_station_number(stations, 20))


