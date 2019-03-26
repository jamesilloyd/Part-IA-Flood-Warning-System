#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:10:26 2018

@author: James
"""
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import update_water_levels



def stations_level_over_threshold(stations, low_tol,high_tol):
    '''This function returns a sorted list of all stations in order of relative water level
    between the the two thersholds'''
    update_water_levels(stations)
    l = []
    for i in stations:
        x = i.relative_water_level()
        if x != 0:
            if i.typical_range_consistent() == True:
                if i.latest_level is not None:
                    if high_tol == None:
                        if x > low_tol:
                            y = (i,x)
                            l.append(y)
                    elif high_tol >= x > low_tol:
                        y = (i,x)
                        l.append(y)
                        
    l=sorted_by_key(l,1, reverse =True)
    return l


def stations_highest_rel_level(stations, N):
    '''This function creates a sorted list of all stations in order of relative water level
    it then returns the highest N values from that list'''
    
    if N >= len(stations):
        l = [("list is shorter than range","soz")]
        return l
        
    else:
        update_water_levels(stations)
        l = []
        for i in stations:
            x = i.relative_water_level()
            name = str(i.name)
            if x != 0:
                if i.typical_range_consistent() == True:
                    if i.latest_level is not None:
                            y = (name,x)
                            l.append(y)
                            
        l=sorted_by_key(l,1, reverse =True)
        highest_rel_range = []
        
        for i in range(N):
            highest_rel_range.append(l[i])
            
        return highest_rel_range
