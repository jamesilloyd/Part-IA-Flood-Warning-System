#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 22:59:09 2018

@author: Marco
"""

import pytest
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance 
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number



stations = build_station_list()

def test_stations_by_distance():
    m = stations_by_distance(stations, (52.2053, 0.1218))
    assert type(m) == list
    for i in range(len(m)):
        assert type(m[i][1])== float  
        assert type(m[i])== tuple
        assert m[i][1] > 0
def test_stations_within_radius():
    n=stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert type(n) == list
    assert len(n) >= 0

def test_rivers_with_station():
    b= rivers_with_station(stations) 
    for i in range(len(b)):
        assert type(b[i]) == str
    assert len(b) > 0
    
def test_stations_by_river():
    v = stations_by_river(stations)
    assert type(v) == dict
    assert type(v["Thames"]) ==list 
    
def test_rivers_by_station_number():
    g = rivers_by_station_number(stations, 9)
    assert type(g) == list
    for i in g:
        assert type(i)== tuple

    