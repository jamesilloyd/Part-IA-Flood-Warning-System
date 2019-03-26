#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:32:07 2018

@author: Heisenberg
"""

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



#Create list of severe risk stations
for station in stations_level_over_threshold(stations,1.5,None):
    severe.append((station[0]))

#Create list of high risk stations
for station in stations_level_over_threshold(stations,1.25,1.5):
        high.append((station[0]))

#Create list of moderate risk stations
for station in stations_level_over_threshold(stations,1,1.25):
        moderate.append((station[0]))

#Create list of low risk stations
for station in stations_level_over_threshold(stations,0,1):
    low.append((station[0]))

    
                    
#ALERT LOCAL TOWNS (within 10km) OF FLOOD WARNING 
#ALSO ALERT ALL STATIONS ALSO ON SAME RIVER AS FLOODED STATION
                    

stations_on_same_rivers = stations_by_river(stations)
print()
print('STATIONS IN SEVERE CONDITION ARE:')
if severe:

    for station in severe:
        name = station.name
        river = station.river
        relative_water_level = round(station.relative_water_level(),3)
        print()
        print('Station: {}, River: {}, Relative water level: {}'.format(name,river,relative_water_level))
        print()
        
        coord = station.coord
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
        name = station.name
        river = station.river
        relative_water_level = round(station.relative_water_level(),3)
        print()
        print('Station: {}, River: {}, Relative water level: {}'.format(name,river,relative_water_level))
        print()
        
        coord = station.coord
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