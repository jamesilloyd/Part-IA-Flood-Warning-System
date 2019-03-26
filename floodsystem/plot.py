#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 20:52:51 2018

@author: Marco
"""

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import datetime
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels


stations = build_station_list()
# Station name to find
station_name = "Cam"

    # Find station
station_cam = None
for station in stations:
    if station.name == station_name:
        station_cam = station
        break

    # Check that station could be found. Return if not found.
if not station_cam:
    print("Station {} could not be found".format(station_name))

    
dt = 10
dates, levels = fetch_measure_levels(station_cam.measure_id,
                                     dt=datetime.timedelta(days=dt))

for date, level in zip(dates, levels):
        print(date, level)