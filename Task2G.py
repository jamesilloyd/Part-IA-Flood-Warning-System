#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 23:23:00 2018

@author: James
"""

from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_river
from floodsystem.flood import stations_level_over_threshold



stations = build_station_list()
update_water_levels(stations)

severe = []
high = []
moderate = []
low = []

'''If river has is in top 20 rivers in terms of how many stations
it has on it, the station severity will be increased by one level for
otherwise moderate and high levels due to potential risk of stations on
that river being flooded as well'''

top_twenty = rivers_by_station_number(stations, 20)

for station in stations:
    river = str(station.river)
    
    for i in top_twenty:
        if i[0] == river:
            in_top_twenty = True
        else:
            in_top_twenty = False
    
    station_level = station.relative_water_level()
    if station_level != 0:
        if station.typical_range_consistent() == True:
            if station.latest_level is not None:
                if station_level > 1.5:
                    severe.append((station,in_top_twenty))
                elif 1.5 >= station_level >1.25:
                    if in_top_twenty is True:
                        severe.append((station,in_top_twenty))
                    else:
                        high.append((station,in_top_twenty))
                        
                elif 1.25 >= station_level > 1:
                    if in_top_twenty is True:
                        high.append((station,in_top_twenty))
                    else:
                        moderate.append((station,in_top_twenty))
                        
                else:
                    low.append((station,in_top_twenty))
                    
#ALERT LOCAL TOWNS (within 10km) OF FLOOD WARNING 
#ALSO ALERT ALL STATIONS ALSO ON SAME RIVER AS FLOODED STATION
                    

stations_on_same_rivers = stations_by_river(stations)
print()
print('STATIONS IN SEVERE CONDITION ARE:')
if severe:

    for station in severe:
        name = station[0].name
        river = station[0].river
        relative_water_level = round(station[0].relative_water_level(),3)
        print()
        print('Station: {}, River: {}, Relative water level: {}'.format(name,river,relative_water_level))
        if station[1] == True:
            print('{} is on a river with the top twenty number of stations'.format(name))
        print()
        
        coord = station[0].coord
        stations_in_local_area_severe = stations_within_radius(stations, coord, 10)
        print('Stations that are within 10km of {} to be alerted are:'.format(name))
        if len(stations_in_local_area_severe) >1:
            for station in stations_in_local_area_severe:
                if station.name != name:
                    print('-{}'.format(station.name))
        else:
            print('No stations to be alerted')
                    
        print()
        print('Other stations on the {} to be alerted are:'.format(river,name))
        if len(stations_on_same_rivers[river]) > 1:
            for station in stations_on_same_rivers[river]:
                if station != name:
                    print('-{}'.format(station))
        else:
            print('No stations to be alerted')
        print()
else:
    print("No stations are in severe condition")

print()
print()
print('STATIONS IN HIGH CONDITION ARE:')
if high:
    
    for station in high:
        name = station[0].name
        river = station[0].river
        relative_water_level = round(station[0].relative_water_level(),3)
        print()
        print('Station: {}, River: {}, Relative water level: {}'.format(name,river,relative_water_level))
        if station[1] == True:
            print('Is on a river with the top twenty number of stations')
        print()
        
        coord = station[0].coord
        stations_in_local_area_high = stations_within_radius(stations, coord, 5)
        print('Stations that are within 5km of {} to be alerted are:'.format(name))
        if len(stations_in_local_area_high)>1:
            for station in stations_in_local_area_high:
                if station.name != name:
                    print('-{}'.format(station.name))
        else:
            print('No stations to be alerted')
                    
        print()
        print('Other stations on the {} to be alerted are: '.format(river,name))
        if len(stations_on_same_rivers[river]) > 1:
            for station in stations_on_same_rivers[river]:
                if station != name:
                    print('-{}'.format(station))
        else:
            print('No stations to be alerted')
        print()
else:
    print('No stations are in severe condition')