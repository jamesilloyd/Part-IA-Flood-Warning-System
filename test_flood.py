#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 18:48:31 2018

@author: James
"""

import pytest
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation


   
s1 = MonitoringStation('Bourton Dickler',
                       None,
                       None,
                       (51.874767, -1.740083),
                       (0.068, 0.42),
                       'River Glen',
                       'Surfleet Seas End')

s1.latest_level=0.42

s2 = MonitoringStation('Hello',
                       None,
                       None,
                       (51.874767, -1.740083),
                       (0.068, 0.42),
                       'River Glen',
                       'Surfleet Seas End')

s2.latest_level=-7

stations= [s1,s2]

    


def test_stations_level_over_threshold():
    m = stations_level_over_threshold(stations,0.8,None)
    assert type(m) == list
    assert len(m) == 1
    assert m[0].name == 'Bourton Dickler'
    for i in range(len(m)):
        assert type(m[i][0])== str
        assert type(m[i][1])== float
        assert type(m[i])== tuple
        
        
def test_stations_highest_rel_level():
    n=stations_highest_rel_level(s1, 10)
    assert type(n) == list
    assert len(n) == 10
    for i in range(len(n)):
        assert type(n[i][0])== str
        assert type(n[i][1])== float
        assert type(n[i])== tuple